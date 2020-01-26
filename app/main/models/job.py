from .. import db, ma


class Job(db.Model):
	"""Job model for storing job related details"""
	__tablename__ = "job"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(255), unique=True, nullable=False)
	fee = db.Column(db.Integer, nullable=False)
	job_status = db.Column(db.Integer, nullable=False)
	created = db.Column(db.DateTime, nullable=False)
	status = db.Column(db.Integer, nullable=False)

	def __init__(self, title, fee, job_status, created, status):
		self.title = title
		self.fee = fee
		self.job_status = job_status
		self.created = created
		self.status = status

	def __repr__(self):
		return "<Job '{}'>".format(self.title)