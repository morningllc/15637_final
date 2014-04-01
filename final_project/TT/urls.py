from django.conf.urls import patterns, include, url


from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'TT.views.home', name = 'home'),

    url(r'^login$','django.contrib.auth.views.login',{'template_name':'TT/login.html'},name='login'),
    url(r'^logout$','django.contrib.auth.views.logout_then_login',name='logout'),
    url(r'^register$','TT.views.register',name='register'),
    url(r'^confirm$','TT.views.confirmEmail',name='confirm'),

)

