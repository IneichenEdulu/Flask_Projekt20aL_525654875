from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.job import Job #job_list


class JobListResource(Resource):
    def get(self):
        data = []
        for job in Job.get_all_published():
            data.append(job.data)
        return {'data': data}, HTTPStatus.OK
        """ for job in job_list:
            if job.is_published is True:
                data.append(job.data)
        return {'data': data}, HTTPStatus.OK """

    def post(self):
        data = request.get_json()
        job = Job(title=data['title'], 
                  description=data['description'], 
                  salary=data['salary'])
        job.save()
        # job_list.append(job)
        return job.data, HTTPStatus.CREATED


class JobResource(Resource):
    def get(self, job_id):
        job = Job.get_by_id(job_id=job_id)
        # job = next((job for job in job_list if job.id == job_id and job.is_published is True), None)  # noqa: E501
        if job is None:
            return {'message': 'job not found'}, HTTPStatus.NOT_FOUND
        
        if job.is_published is False:
            return {'message': 'job not published'}, HTTPStatus.FORBIDDEN
        
        return job.data, HTTPStatus.OK

    def put(self, job_id):
        data = request.get_json()
        job = Job.get_by_id(job_id=job_id)
        # job = next((job for job in job_list if job.id == job_id), None)
        if job is None:
            return {'message': 'job not found'}, HTTPStatus.NOT_FOUND
        job.title = data['title']
        job.description = data['description']
        job.salary = data['salary']
        job.save()
        return job.data, HTTPStatus.OK

    def delete(self, job_id):
        job = Job.get_by_id(job_id=job_id)
        # job = next((job for job in job_list if job.id == job_id), None)
        if job is None:
            return {'message': 'job not found'}, HTTPStatus.NOT_FOUND
        job.delete()
        # job_list.remove(job)
        return {}, HTTPStatus.NO_CONTENT


class JobPublishResource(Resource):
    def put(self, job_id):
        job = Job.get_by_id(job_id=job_id)
        # job = next((job for job in job_list if job.id == job_id), None)
        if job is None:
            return {'message': 'job not found'}, HTTPStatus.NOT_FOUND
        job.is_published = True
        job.save()
        return {}, HTTPStatus.OK

    def delete(self, job_id):
        job = Job.get_by_id(job_id=job_id)
        # job = next((job for job in job_list if job.id == job_id), None)
        if job is None:
            return {'message': 'job not found'}, HTTPStatus.NOT_FOUND
        job.is_published = False
        job.save()
        return {}, HTTPStatus.OK