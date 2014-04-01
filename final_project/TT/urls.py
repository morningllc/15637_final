from django.conf.urls import patterns, include, url


from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homework3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'TT.views.home', name = 'home'),

    # url(r'^manage', 'blog.views.manage', name = 'manage'),
    # url(r'^add-post', 'blog.views.add_post'),
    # url(r'^delete-post/(?P<id>\d+)$', 'blog.views.delete_post'),
    # url(r'^photo/(?P<id>\d+)$', 'blog.views.get_photo', name='photo'),
    
    # url(r'^login$', 'blog.views.login', name='login'),
    # url(r'^logout$', 'blog.views.logout', name='logout'),
    # url(r'^registration$', 'blog.views.registration'),
    # url(r'^confirm/(?P<confirmation_key>.*)$', 'blog.views.confirm'),

    # url(r'^read/(?P<user_id>\d+)$', 'blog.views.read'),
    # url(r'^follow/(?P<user_id>\d+)$', 'blog.views.follow'),
    # url(r'^unfollow/(?P<user_id>\d+)$', 'blog.views.unfollow'),
    # url(r'^get-list$', 'blog.views.get_list'),
    # url(r'^get-list-loggedin$', 'blog.views.get_list_loggedin'),
)

