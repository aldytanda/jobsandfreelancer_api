import datetime

from app.main import db
from app.main.models.job import Job
from app.main.models.assignment import Assignment


def get_all_jobs():
	return Job.query.filter_by(status=1).all()

def get_a_job(id):
	job = Job.query.filter_by(id=id, status=1).first()
	return job

def get_a_job_by_title(title):
	search = "upper(%{}%)".format(title)
	job = Job.query.filter(Job.title.ilike(search)).filter_by(status=1).all()
	return job

def get_all_jobs_p(page, title):
	search = "%{}%".format(title)
	query = Job.query
	if title:			
		query = query.filter(Job.title.like(search))
	jobs = query.filter_by(status=1).paginate(page=page, per_page=5, error_out=False)
	return jobs

def save_new_job(data):
	job = Job.query.filter_by(title=data['title']).first()
	if not job:
		new_job = Job(
			title = data['title'],
			fee = data['fee'],
			job_status = 1,
			created = datetime.datetime.utcnow(),
			status = 1
		)
		db.session.add(new_job)
		db.session.commit()
		response_object = {
			'status': 'success',
			'message': 'Successfully created'
		}
		return response_object, 201
	else:
		response_object = {
			'status': 'failed',
			'message': 'Job already exists. Please specify new title'
		}
		return response_object, 409


def update_a_job(id, data):
	job = Job.query.filter_by(id=id, status=1).first()
	if not job:
		response_object = {
			'status': 'failed',
			'message': 'Job not found. cannot update'
		}
		return response_object, 404
	else:
		job.title = data['title']
		job.fee = data['fee']
		db.session.commit()
		response_object = {
			'status': 'success',
			'message': 'Successfuly updated'
		}
		return response_object, 201

def delete_a_job(id):
	job = Job.query.filter_by(id=id, status=1).first()
	if job:
		job.status = 0
		db.session.commit()
		response_object = {
			'status': 'success',
			'message': 'job deleted'
        }
		return response_object, 201
	else:
		response_object = {            'status': 'failed',
			'message': 'Job not found. cannot delete'
        }
		return response_object, 409


def assign_job(job_id, data):
	assignment = Assignment.query.filter_by(job_id=job_id, freelancer_id=data['freelancer_id']).first()
	print(assignment)
	if not assignment:
		new_assignment = Assignment(
            job_id=job_id,
            freelancer_id=data['freelancer_id'],
            created=datetime.datetime.utcnow(),
            status=1
        )
		db.session.add(new_assignment)
		db.session.commit()
		response_object = {
				'status': 'success',
				'message': 'Successfully assigned job'
			}
		return response_object, 201
	else:
		response_object = {
            'status': 'failed',
			'message': 'Freelancer already assigned to this job'
        }
		return response_object, 409
