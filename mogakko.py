class mogakko(object):
    def __init__(self):
        super(mogakko, self).__init__()
        self.payload = {
            'assignee': '',
            'task': [
                {'name': '',
                 'due': '',
                 'status': ''},
            ],
            'date': 'YYYY-MM-DD',
            'id': 1
        }
        self.daily_task = []

    def list(self, query):
        """
        List all to-do lists queried by either date, id, or assignee
        :param query:
        :return:
        """
        return sorted(self.daily_task, key=query)

    def create(self, data):
        # Get today's to-do list
        self.daily_task.append(data)

    def update(self, payload):
        """
        Update mogakko to-do with post request
        :param payload:
        :return:
        """
        try:
            list(filter(lambda x: x.id == payload.id, self.daily_task))[0] = payload
        except ValueError:
            print('nothing found')

    def findListById(self, id):
        return list(filter(lambda x: x.id == id, self.daily_task))[0]

    def delete(self, id):
        """
        Delete mogakko to-do by id
        :param id:
        :void:
        """
