import requests

__version__ = '0.3.1'

class Person(object):

    def __init__(self, name):
        user_agent = 'Person/{}'.format(__version__)
        self.name = name
        self.session = requests.Session()
        self.session.headers = {'User-Agent': user_agent}

    def __repr__(self):
        return 'Object from <Person Class> (name: {}, session.headers: {})'.format(self.name, self.session.headers)

    def get_gender(self):
        # https://genderize.io/
        params = {'name': self.name}
        response = self.session.get('https://api.genderize.io', params=params)
        
        if 'application/json' not in response.headers.get('content-type', ''):
            status = "server responded with {http_code}: {reason}".format(
                http_code=response.status_code, reason=response.reason)
            return {'error': 'response not in JSON format ({status})'.format(status=status)}

        decoded = response.json()
        if response.ok:
            return {'gender': decoded}
        else:
            return {'error': {'status_code': response.status_code, 'headers': response.headers}}

    def get_nationality(self):
        # https://nationalize.io/
        params = {'name': self.name}
        response = self.session.get('https://api.nationalize.io', params=params)
        
        if 'application/json' not in response.headers.get('content-type', ''):
            status = "server responded with {http_code}: {reason}".format(
                http_code=response.status_code, reason=response.reason)
            return {'error': 'response not in JSON format ({status})'.format(status=status)}

        decoded = response.json()
        if response.ok:
            return {'nationality': decoded}
        else:
            return {'error': {'status_code': response.status_code, 'headers': response.headers}}

    def get_age(self):
        # https://agify.io/
        params = {'name': self.name}
        response = self.session.get('https://api.agify.io', params=params)
        
        if 'application/json' not in response.headers.get('content-type', ''):
            status = "server responded with {http_code}: {reason}".format(
                http_code=response.status_code, reason=response.reason)
            return {'error': 'response not in JSON format ({status})'.format(status=status)}

        decoded = response.json()
        if response.ok:
            return {'age': decoded}
        else:
            return {'error': {'status_code': response.status_code, 'headers': response.headers}}

