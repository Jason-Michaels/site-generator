from starlette.applications import Starlette
from starlette.responses import JSONResponse

app = Starlette(debug=True)

@app.route('/{path}')
async def homepage(request):
    return JSONResponse({'hello': path})