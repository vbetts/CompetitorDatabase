from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^globalmarket/$', views.globalmarket, name='globalmarket'),
    url(r'^verticalmarket/$', views.verticalmarket, name='verticalmarket'),
    url(r'^technology/$', views.technology, name='technology'),
    url(r'^channels/$', views.channels, name='channels'),
    url(r'^revenue/$', views.revenue, name='revenue'),
    url(r'^features/$', views.features, name='features'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^details/$', views.details, name='details'),
    url(r'^print/$', views.printpage, name='printpage'),
    url(r'^competitordocs/$', views.competitordocs, name='competitordocs'),
    url(r'^salesdocs/$', views.salesdocs, name='salesdocs'),
    url(r'^change/$', views.changepassword, name='changepassword')
]