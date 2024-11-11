from ninja import NinjaAPI
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

api = NinjaAPI(title="My Project API", version="1.0")

@api.get("/test-route")
@method_decorator(login_required)
def hello(request):
    return {"message": "test-route-message"}
