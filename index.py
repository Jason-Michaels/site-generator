from starlette.applications import Starlette
from starlette.responses import JSONResponse

app = Starlette(debug=True)

@app.route('/{path}')
async def homepage(request, path):
    return JSONResponse({'hello': path})