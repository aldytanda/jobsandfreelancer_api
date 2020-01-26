from flask import request, jsonify
from flask_restplus import Resource, reqparse
from marshmallow import pprint

from app.main.util.freelancer_dto import FreelancerDto, FreelancerSchema, PaginationSchema
from app.main.util.pagination_dto import Pagination
from app.main.services.freelancer_service import (save_new_freelancer, get_all_freelancers, get_a_freelancer,
													delete_a_freelancer, update_a_freelancer, get_all_freelancers_p)

api = FreelancerDto.api
_freelancer = FreelancerDto.freelancer
freelancer_schema = FreelancerSchema()
freelancers_schema = FreelancerSchema(many=True)
pagination_schema = PaginationSchema()

@api.route('/')
class FreelancerList(Resource):
	@api.doc('list_of_freelancers')
	# @api.response()
	# @api.marshall_list_with(_freelancer)
	def get(self):
		"""List all registered freelancers"""
		output = freelancers_schema.dump(get_all_freelancers())
		return makeResponseSuccess(output)

	@api.doc('register a new freelancer')
	@api.response(201, 'Freelancer successfully registered.')
	@api.expect(_freelancer, validate=True)
	def post(self):
		"""Add a new Freelancer"""
		data = request.json
		return save_new_freelancer(data=data)


@api.route('/page/<int:page>')
@api.param('name', 'Freelancer name')
@api.param('page', 'Page number')
class PaginatedFreelancerList(Resource):
	@api.doc('paginated_list_of_freelancers')
	def get(self, page):
		"""List of registered freelancers with pagination"""
		args = reqparse.RequestParser().add_argument('name').parse_args()
		data = get_all_freelancers_p(page, args['name'])
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
		return makeResponseSuccess(output)

@api.route('/<id>')
@api.param('id', 'The Freelancer identifier')
@api.response(404, 'Freelancer not found.')
class Freelancer(Resource):
	@api.doc('get a freelancer')
	# @api.marshal_with(_freelancer)
	def get(self, id):
		"""get a freelancer given its identifier"""
		freelancer = get_a_freelancer(id)
		output = freelancer_schema.dump(freelancer)
		if not freelancer:
			return makeResponseNotFound()
		else:
			return makeResponseSuccess(output)

	@api.doc('update a freelancer')
	@api.response(201, 'Freelancer successfuly updated.')
	@api.expect(_freelancer, validate=True)
	def put(self, id):
		"""Update a freelancer"""
		data = request.json
		return update_a_freelancer(id, data=data)

	@api.doc('delete a freelancer')
	def delete(self, id):
		"""delete a freelancer given its identifier"""
		return delete_a_freelancer(id)

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
