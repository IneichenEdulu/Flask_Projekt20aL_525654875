job_list = []


def get_last_id():
    last_job = 1

    if job_list:
        last_job = job_list[-1].id + 1 

    return last_job


class Job: #
    def __init__(self, title, description, salary):
        self.id = get_last_id()
        self.title = title
        self.description = description
        self.salary = salary
        self.is_published = False

    @property
    def data(self):
        return {'id': self.id, 'title': self.title, 
                'description': self.description, 
                'salary': self.salary}
