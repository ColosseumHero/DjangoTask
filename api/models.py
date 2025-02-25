from tastypie.resources import ModelResource
from events.models import Category, Event
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication
from tastypie.models import ApiKey
from django.contrib.auth.models import User

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']

class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'events'
        allowed_methods = ['get', 'post', 'delete', 'update']
        excludes = ['description', 'location']
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        allowed_methods = ['get', 'post']
        authentication = CustomAuthentication()
        authorization = Authorization()
        always_return_data = True

    def obj_create(self, bundle, **kwargs):
        bundle = super().obj_create(bundle, **kwargs)
        bundle.obj.set_password(bundle.data.get('password'))
        bundle.obj.save()
        ApiKey.objects.get_or_create(user=bundle.obj)
        return bundle

