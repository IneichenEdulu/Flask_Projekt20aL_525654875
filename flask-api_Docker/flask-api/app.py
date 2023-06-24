from config import Config
from extensions import db
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from resources.job import JobListResource
from resources.job import JobPublishResource
from resources.job import JobResource


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

api.add_resource(JobListResource, '/jobs')
api.add_resource(JobResource, '/jobs/<int:job_id>')
api.add_resource(JobPublishResource, '/jobs/<int:job_id>/publish')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
