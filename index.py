import responder

app = responder.API(debug=True, static_dir='.',templates_dir='.')

@app.route("/api/{greeting}")
async def greet_world(req, resp, *, greeting):
    resp.text = f"{greeting}, world!"

@app.route("/{path}")
def hello_html(req, resp, *, path):
     if path.split('.')[-1] == '':
         url = f"{path}/index.html"
     else:
         url = path
    #url = path
    print(url)
    resp.html = app.template(url, url=url)


if __name__ == '__main__':
    app.run()