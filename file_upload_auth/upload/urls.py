from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^with-hawk/$', views.UploadWithHawk().as_view()),
]
