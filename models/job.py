from extensions import db
job_list = []


""" def get_last_id():
    last_job = 1

    if job_list:
        last_job = job_list[-1].id + 1 

    return last_job
 """

class Job(db.Model): #
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True)  # noqa: A003
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    salary = db.Column(db.Integer)
    is_published = db.Column(db.Boolean, default=False)
    """ def __init__(self, title, description, salary):
        self.id = get_last_id()
        self.title = title
        self.description = description
        self.salary = salary
        self.is_published = False """

    @property
    def data(self):
        return {'id': self.id, 
                'title': self.title, 
                'description': self.description, 
                'salary': self.salary}
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_published(cls):
        return cls.query.filter_by(is_published=True).all()

    @classmethod
    def get_by_id(cls, job_id):
        return cls.query.filter_by(id=job_id).first()