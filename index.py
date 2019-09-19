from sanic import Sanic
from sanic.views import CompositionView
from sanic.response import text
import os

app = Sanic(__name__)

#because we don't know where we are...
dir_path = os.path.dirname(os.path.realpath(__file__))

def get_handler(request):
    #print(os.path.dirname(os.path.realpath(__file__)))
    return text('I am a get method')

view = CompositionView()
view.add(['GET'], get_handler)
view.add(['POST', 'PUT'], lambda request: text('I am a post/put method'))

# Use the new view to handle requests to the base URL
app.add_route(view, '/api')

app.static('/', dir_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)