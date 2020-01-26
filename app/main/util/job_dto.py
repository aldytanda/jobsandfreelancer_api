from flask_restplus import Namespace, fields
from marshmallow import fields as mafields

from .. import ma
from app.main.models.job import Job


class JobDto:
	api = Namespace('job', description='job related operations')
	job = api.model('job', {
		# 'id': fields.Integer(description='job id'),
		'title': fields.String(required=True, description='job title'),
		'fee': fields.Integer(required=True, description='job fee'),
		# 'job_status': fields.Integer(description='job progress'),
		# 'created': fields.DateTime(description='job create time'),
		# 'status': fields.Integer(description='status')
	})
	assignment = api.model('assignment', {
		# 'job_id': fields.Integer(description='job id'),
		'freelancer_id': fields.Integer(description='freelancer_id')
	})
	# jobP = api.model('jobp', {
	# 	'has_prev': fields.Boolean(description='True if a previous page exit'),
	# 	'has_next': fields.Boolean(description='True if a next page exit'),
	# 	'total': fields.Integer(description='Total number of jobs'),
	# 	'jobs': fields.List(fields.Nested(job))
	# })

class JobSchema(ma.Schema):
	class Meta:
		fields = ('id', 'title', 'fee', 'job_status', 'created', 'status')


class PaginationSchema(ma.Schema):
	class Meta:
		fields = ('items', 'has_prev', 'next_num', 'prev_num', 'page', 'pages', 'has_next', 'total')
	items = mafields.List(mafields.Nested(JobSchema))
