from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout
from django.contrib import admin
from project.views import *

admin.autodiscover()

urlpatterns = patterns('',
		# Examples:
		# url(r'^$', 'minilog.views.home', name='home'),
					

                       
    				url(r'^home/$','project.views.home'),
  	                        url(r'^$','project.views.home'),
      				url(r'^about/$','project.views.about'),
    				url(r'^login/$','project.views.loginuser'),
    				url(r'^signup/$','project.views.signup'),
           	                url(r'^children/$','project.views.children'),
                    	        url(r'^children1/$','project.views.children1'),
                       		url(r'^contact/$','project.views.contact'),
				url(r'^update/$','project.views.update'),
				url(r'^symptoms/$','project.views.sympt'),			
				url(r'^doct1/$','project.views.doct1'),			
				url(r'^patget/$','project.views.patget'),			
				url(r'^child/$','project.views.child'),			
								
				url(r'^docres/$','project.views.docres'),									
				url(r'logout/$',logout,kwargs={'next_page':'/login/'},name='loginuser'),
                       		url(r'^admin/', include(admin.site.urls)),
						
)

