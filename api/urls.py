from api.models import EventResource, CategoryResource, UserResource
from tastypie.api import Api
from django.urls import path, include

event_resource = EventResource()
category_resource = CategoryResource()
user_resource = UserResource()
api = Api(api_name='v1')
api.register(category_resource)
api.register(event_resource)
api.register(user_resource)

urlpatterns = [
    path('', include(api.urls), name="index")
]