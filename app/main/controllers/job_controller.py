from flask import request, jsonify
from flask_restplus import Resource, reqparse
from marshmallow import pprint

from ..util.job_dto import JobDto, JobSchema, PaginationSchema
from ..util.pagination_dto import Pagination
from ..services.job_service import (save_new_job, get_all_jobs, get_a_job, delete_a_job, 
									update_a_job, get_all_jobs_p, get_a_job_by_title,
									assign_job)

api = JobDto.api
_job = JobDto.job
_assignment = JobDto.assignment
# _jobP = JobDto.jobP
job_schema = JobSchema()
jobs_schema = JobSchema(many=True)
pagination_schema = PaginationSchema()

@api.route('/')
class JobList(Resource):
	@api.doc('list_of_jobs')
	# @api.marshal_list_with(_job)
	def get(self):
		"""List all registered jobs"""
		output = jobs_schema.dump(get_all_jobs())
		return makeResponseSuccess(output)


	@api.doc('create a new job')
	@api.response(201, 'Job successfully created.')
	@api.expect(_job, validate=True)
	def post(self):
		"""Creates a new Job """
		data = request.json
		return save_new_job(data=data)

@api.route('/page/<int:page>')
@api.param('title', 'Job title')
@api.param('page', 'Page number')
class PaginatedJobList(Resource):
	@api.doc('paginated_list_of_jobs')
	# @api.marshal_with(_jobP)
	def get(self, page):
		"""List of registered jobs with pagination"""
		parser = reqparse.RequestParser()
		parser.add_argument('title')
		args = parser.parse_args()
		# data = get_a_job_by_title(args['title'])
		data = get_all_jobs_p(page, args['title'])
		pagination = Pagination(
			items = data.items,
			has_prev = data.has_prev,
            next_num = data.next_num,
            prev_num = data.prev_num,
            page = data.page,
            pages = data.pages,
            has_next = data.has_next,
            total = data.total
		)
		output = pagination_schema.dump(pagination)
		# pprint(output)
		# return api.marshal(p, _jobP)
		return makeResponseSuccess(output)


@api.route('/<id>')
@api.param('id', 'The Job identifier')
@api.response(404, 'Job not found.')
class Job(Resource):
	@api.doc('get_a_job')
	# @api.marshal_with(_job)
	def get(self, id):
		"""get a job given its identifier"""
		job = get_a_job(id)
		# print(job_schema.jsonify(job))
		# print(job_schema.dump(job))
		output = job_schema.dump(job)
		if not job:
			return makeResponseNotFound()
		else:
			return makeResponseSuccess(output)
	
	@api.doc('assign_a_job')
	@api.response(201, 'Job successfully assigned.')
	@api.response(409, 'Freelancer already assigned to this job')
	@api.expect(_assignment, validate=True)
	def post(self, id):
		"""Assign a freelancer to the Job """
		data = request.json
		return assign_job(job_id=id, data=data)

	# @api.doc('create a new job')
	# @api.response(201, 'Job successfully created.')
	# @api.expect(_job, validate=True)
	# def post(self):
	# 	"""Creates a new Job """
	# 	data = request.json
	# 	return save_new_job(data=data)

	@api.doc('update a job')
	@api.response(201, 'Job successfuly updated.')
	@api.expect(_job, validate=True)
	def put(self, id):
		"""Update a job"""
		data = request.json
		return update_a_job(id, data=data)

	@api.doc('delete a job')
	def delete(self, id):
		"""delete a job given its identifier"""
		return delete_a_job(id)


def makeResponseSuccess(data):
	return makeResponse(201, data)

def makeResponseNotFound():
	return makeResponse(400, None)

def makeResponse(response_status, data):
	responseList = {
		'200': 'success',
		'201': 'success',
		'400': 'not found',
		'404': 'data not found'
	}

	resp = {
		'code': response_status,
		'description': responseList[str(response_status)],
		'data': data
	}
	return jsonify(resp)
