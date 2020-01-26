import datetime

from app.main import db
from app.main.models.freelancer import Freelancer


def get_all_freelancers():
	return Freelancer.query.filter_by(status=1).all()

def get_a_freelancer(id):
	return Freelancer.query.filter_by(id=id, status=1).first()

def get_all_freelancers_p(page, name):
	search = "%{}%".format(name)
	query = Freelancer.query
	if name:
		query = query.filter(Freelancer.name.like(search))
	freelancers = query.filter_by(status=1).paginate(page=page, per_page=5, error_out=False)
	return freelancers

def save_new_freelancer(data):
	freelancer = Freelancer.query.filter_by(name=data['name']).first()
	if not freelancer:
		new_freelancer = Freelancer(
			name = data['name'],
			created = datetime.datetime.utcnow(),
			status = 1
		)
		db.session.add(new_freelancer)
		db.session.commit()

		response_object = {
			'status': 'success',
			'message': 'Successfuly created'
		}

		return response_object, 201
	else:
		response_object = {
			'status': 'failed',
			'message': 'Freelancer already exist with name {}'.format(data['name'])
		}
		return response_object, 409

def update_a_freelancer(id, data):
	freelancer = Freelancer.query.filter_by(id=id, status=1).first()
	if not freelancer:
		response_object = {
			'status': 'failed',
			'message': 'Freelancer not found. cannot update'
		}
	else:
		freelancer.name = data['name']
		db.session.commit()
		response_object = {
			'status': 'success',
			'message': 'Successfuly updated'
		}
		return response_object, 201

def delete_a_freelancer(id):
	freelancer = Freelancer.query.filter_by(id=id, status=1).first()
	if not freelancer:
		response_object = {
			'status': 'failed',
			'message': 'Freelancer not found. cannot delete'
		}
	else:
		freelancer.status = 0
		db.session.commit()
		response_object = {
			'status': 'success',
			'message': 'freelancer deleted'
		}
		return response_object, 204