from flask import Flask
from flask_restful import Api

from resources.job import JobListResource, JobPublishResource, JobResource

app = Flask(__name__)
api = Api(app)

api.add_resource(JobListResource, '/jobs')
api.add_resource(JobResource, '/jobs/<int:job_id>')
api.add_resource(JobPublishResource, '/jobs/<int:job_id>/publish')

if __name__ == "__main__":
    app.run(port=5000, debug=True)