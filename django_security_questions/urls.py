from django.urls import include, re_path

from .views import add, change

urlpatterns = [
    re_path(r'^questions/add/$', add, name='questions_add'),
    re_path(r'^questions/chagne/$/', change, name='questions_change'),
]
urlpatterns = patterns('',
    url(
        regex=r'^questions/add/$',
        view='add',
        name='questions_add'
    ),
    url(
        regex=r'^questions/change/$',
        view='change',
        name='questions_change'
    ),
)
