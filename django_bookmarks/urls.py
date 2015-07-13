#from django.conf.urls.defaults import *
from django.conf.urls import patterns
#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#)

from bookmarks.views import *
urlpatterns = patterns('',
	(r'^$', main_page),
	(r'^user/(\w+)/$', user_page),
#	(r'^$', user_page),
)

