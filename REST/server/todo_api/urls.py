# todo_api/urls.py

from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

urlpatterns = {
    re_path(r'^todos/$', CreateView.as_view(), name="create"),
    re_path(r'^todos/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
