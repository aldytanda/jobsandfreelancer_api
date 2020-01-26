from .. import db
from ..models.job import Job
from ..models.freelancer import Freelancer

class Assignment(db.Model):
	"""Association model for relationship between Jobs and Freelancers"""
	__tablename__ = 'job_assignment'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
	freelancer_id = db.Column(db.Integer, db.ForeignKey('freelancer.id'))
	created = db.Column(db.DateTime)
	status = db.Column(db.Integer)

	job = db.relationship('Job',
		backref = db.backref('job_assignments')
	)

	freelancer = db.relationship('Freelancer',
		backref = db.backref('job_assignments')
	)

	def __init__(self, job_id, freelancer_id, created, status):
		self.job_id = job_id
		self.freelancer_id = freelancer_id
		self.created = created
		self.status = status