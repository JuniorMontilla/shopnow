from django.conf.urls.defaults import  patterns,url

urlpatterns = patterns('shopnow.apps.index.views',
        url(r'^$', 'view_index', name='index_view'),
)
