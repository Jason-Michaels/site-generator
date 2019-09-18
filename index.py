import responder

api = responder.API(debug=True, static_dir='.',templates_dir='.')

@api.route("/api/{greeting}")
async def greet_world(req, resp, *, greeting):
    resp.text = f"{greeting}, world!"

@api.route("/{path}")
def hello_html(req, resp, *, path):
    # if path.split('.')[-1] == '':
    #     url = f"{path}/index.html"
    # else:
    #     url = path
    url = path
    print(url)
    resp.html = api.template(url, url=url)


if __name__ == '__main__':
    api.run()