from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('shopnow.apps.profile.views',
        url(r'^login/$', 'view_login', name='login_view'),
        url(r'^logout/$', 'view_logout', name='logout_view'),
        url(r'^register/user/$', 'view_register', name='register_view'),
        url(r'^profile/$', 'view_profile', name='profile_view'),
)



