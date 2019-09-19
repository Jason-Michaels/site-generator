import responder
#import sys

app = responder.API(debug=True, static_dir='.',templates_dir='.')

@app.route("/api/{greeting}")
async def greet_world(req, resp, *, greeting):
    resp.text = f"{greeting}, world!"

@app.route("/{path}")
def hello_html(req, resp, *, path):
    #if len(path) == 0:
    ##   url = "index.html"
    #elif path.split('.')[-1] == '':
        #url = f"{path}/index.html"
    # else:
        # url = path
    url = path
    print(url)
    try:
        resp.html = app.template(url, url=url)
    except Exception as e:
        print("Error occurred: ", e) 


#if __name__ == '__main__':
    #app.run()