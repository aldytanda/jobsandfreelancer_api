from app.main import db, ma

class Freelancer(db.Model):
	"""Freelancer model for storing freelancers related details"""
	__tablename__ = "freelancer"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(255), unique=True, nullable=False)
	created = db.Column(db.DateTime, nullable=False)
	status = db.Column(db.Integer, nullable=False)

	def __init__(self, name, created, status):
		self.name = name
		self.created = created
		self.status = status

	def __repr__(self):
		return "<Freelancer '{}'>".format(self.name)