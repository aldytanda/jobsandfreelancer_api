from flask_restplus import Api
from flask import Blueprint

from app.main.controllers.job_controller import api as job_ns
from app.main.controllers.freelancer_controller import api as freelancer_ns

blueprint = Blueprint('api', __name__)

api = Api(
	blueprint,
	title = 'FLASK RESTFUL API FOR JOB AND FREELANCER APP',
	version = '1.0',
	description = 'an exercise for flask restful api'
)

api.add_namespace(job_ns, path='/job')
api.add_namespace(freelancer_ns, path='/freelancer')