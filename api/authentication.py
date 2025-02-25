from tastypie.authentication import ApiKeyAuthentication

class CustomAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        print(f"Request: {request.method} - {request.path}")
        if request.method == 'GET':
            return True
        elif request.method == 'POST' and request.path == '/api/v1/users/':
            print("Enable")
            return True
        return super().is_authenticated(request, **kwargs)

