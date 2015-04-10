from django.conf.urls import patterns, url, include


urlpatterns = patterns(
    '',

    # API V1
    url(r'^api/v1/$', include('{{ cookiecutter.app_name }}.api.v1.urls', namespace='v1')),
)
