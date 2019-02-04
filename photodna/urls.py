from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^testtest865679', views.photoload, name='photoload'),
    url(r'^handler', views.process_image, name='process_image'),
    url(r'^$', views.FrontendAppView.as_view())

]