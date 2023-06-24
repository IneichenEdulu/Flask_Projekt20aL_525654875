from http import HTTPStatus

from flask import request
from flask_restful import Resource
from models.job import Job
from models.job import job_list


class JobListResource(Resource):
    def get(self):
        data = []
        for job in Job.get_all_published():
            data.append(job.data)
        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()
        job = Job(title=data['title'], 
                  description=data['description'], 
                  salary=data['salary'])
        job.save()
        return job.data, HTTPStatus.CREATED


class JobResource(Resource):
    def get(self, job_id):
        job = Job.get_by_id(job_id=job_id)
        if job is None:
            return {'message': 'job not found'}, HTTPStatus.NOT_FOUND

        if job.is_published is False:
            return {'message': 'job not published'}, HTTPStatus.FORBIDDEN
        return job.data, HTTPStatus.OK

    def put(self, job_id):
        data = request.get_json()
        job = Job.get_by_id(job_id=job_id)
        if job is None:
            return {'message': 'job not found'}, HTTPStatus.NOT_FOUND
        job.title = data['title']
        job.description = data['description']
        job.salary = data['salary']
        job.save()
        return job.data, HTTPStatus.OK

    def delete(self, job_id):
        job = Job.get_by_id(job_id=job_id)
        if job is None:
            return {'message': 'job not found'}, HTTPStatus.NOT_FOUND
        job.delete()
        return {}, HTTPStatus.NO_CONTENT


class JobPublishResource(Resource):
    def put(self, job_id):
        job = Job.get_by_id(job_id=job_id)
        if job is None:
            return {'message': 'job not found'}, HTTPStatus.NOT_FOUND
        job.is_published = True
        job.save()
        return {}, HTTPStatus.OK

    def delete(self, job_id):
        job = Job.get_by_id(job_id=job_id)
        if job is None:
            return {'message': 'job not found'}, HTTPStatus.NOT_FOUND
        job.is_published = False
        job.save()
        return {}, HTTPStatus.OK
