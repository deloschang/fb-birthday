from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'webapp.views.home', name='home'),
     url(r'', include('social_auth.urls')),
     url(r'^pull_facebook', 'webapp.views.pull_facebook', name='pull_facebook'),
     url(r'^searching', 'webapp.views.search', name='search'),

    # url(r'^birthday/', include('birthday.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
