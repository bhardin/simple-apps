import falcon

class RootResource:
    def on_get(self, req, resp):
        """Handles GET requests on root"""
        body = {
            "code": 200,
            "status": "success"
        }

        resp.media = body

api = falcon.API()
api.add_route("/", RootResource())
