import falcon
import os
import json


class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = '{"hello":"world"}'

class TestStuff(object):
    def on_get(self, req, resp):
        get_os_value = {'test': os.getenv('MY_VARIABLE', 'no_value'), 'test_2': os.getenv('another_one', 'no_value')}
        resp.body = json.dumps(get_os_value)


# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/' URL path
app.add_route('/', things)
app.add_route('/test_stuff_2', TestStuff())