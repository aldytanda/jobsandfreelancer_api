from flask_restplus import Namespace, fields
from marshmallow import fields as mafields

from app.main import ma
from app.main.models.freelancer import Freelancer


class FreelancerDto:
	api = Namespace('freelancer', description='freelancer related operations')
	freelancer = api.model('freelancer', {
		'id': fields.Integer(description='freelancer id'),
		'name': fields.String(required=True, description='freelancer name'),
		'created': fields.DateTime(description='freelancer create time'),
		'status': fields.Integer(description='status')
	})


class FreelancerSchema(ma.Schema):
	class Meta:
		fields = ('id', 'name', 'created', 'status')


class PaginationSchema(ma.Schema):
	class Meta:
		fields = ('items', 'has_prev', 'next_num', 'prev_num', 'page', 'pages', 'has_next', 'total')
	items = mafields.List(mafields.Nested(FreelancerSchema))
