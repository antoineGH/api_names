import requests

__version__ = '0.3.1'

class Genderize(object):

    def __init__(self, timeout=30.0):
        user_agent = 'Genderize/{}'.format(__version__)
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers = {'User-Agent': user_agent}

    def get_name(self, name):
        print(name)
        response = self.session.get('https://api.genderize.io/', params=name, timeout=self.timeout)
        print(response)
        pass

    def say_hello(self):
        print('hello')

