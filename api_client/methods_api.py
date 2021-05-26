from requests import Session


class ApiClient:
    def __init__(self):
        self.session = Session()

    def get(self, url, **kwargs):
        response = self.session.get(url, **kwargs)
        return response

    def put(self, url, **kwargs):
        response = self.session.put(url, **kwargs)
        return response

    def post(self, url, **kwargs):
        response = self.session.post(url, **kwargs)
        return response

    def delete(self, url, **kwargs):
        response = self.session.delete(url, **kwargs)
        return response
