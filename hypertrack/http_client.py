import json
from urlparse import urljoin

import requests

from .version import VERSION


class HyperTrackAPI(object):
    '''
    Wrapper around the HyperTrack API
    '''
    def __init__(self, secret_key, publishable_key,
                 base_url='https://app.hypertrack.io'):
        self.secret_key = secret_key
        self.publishable_key = publishable_key
        self.base_url = base_url
        self.urls = {
            'customer': '/api/v1/customers/',
            'destination': '/api/v1/destinations/',
            'hub': '/api/v1/hubs/',
            'fleet': '/api/v1/fleets/',
            'driver': '/api/v1/drivers/',
            'task': '/api/v1/tasks/',
            'trip': '/api/v1/trips/',
            'events': '/api/v1/events/',
        }

    def _get_url(self, method):
        url_fragment = self.urls.get(method)
        url = urljoin(self.base_url, url_fragment)
        return url

    def _get_user_agent(self):
        user_agent = 'HyperTrack/v1 PythonBindings/{version}'.format(
            version=VERSION)
        return user_agent

    def _get_headers(self):
        headers = {
            'Authorization': 'token %s' % self.secret_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': self._get_user_agent(),
        }
        return headers

    def _post_request(self, method, data, url_params=None):
        url = self.get_url(method)

        if url_params:
            url = url.format(**url_params)

        headers = self.get_headers()
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response

    def create_trip(self, driver_id, vehicle_type, tasks, start_location):
        data = {
            'driver_id': driver_id,
            'tasks': tasks,
            'start_location': start_location,
        }
        response = self.post_request('start_trip', data)
        return response.json()

    def get_trip(self, trip_id, end_location):
        data = {'end_location': end_location}
        response = self.post_request('end_trip', data,
                                     url_params={'trip_id': trip_id})
        return response.json()

    def get_trips(self, trip_id, end_location):
        data = {'end_location': end_location}
        response = self.post_request('end_trip', data,
                                     url_params={'trip_id': trip_id})
        return response.json()

    def create_task(self):
        pass

    def get_task(self):
        pass

    def get_tasks(self):
        pass

    def create_customer(self):
        pass

    def get_customer(self):
        pass

    def get_customerts(self):
        pass

    def create_destination(self):
        pass

    def get_destination(self):
        pass

    def get_destinations(self):
        pass

    def create_driver(self):
        pass

    def get_driver(self):
        pass

    def get_drivers(self):
        pass

    def create_hub(self):
        pass

    def get_hub(self):
        pass

    def get_hubs(self):
        pass

    def create_fleet(self):
        pass

    def get_fleet(self):
        pass

    def get_fleets(self):
        pass
