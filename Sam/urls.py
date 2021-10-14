from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import viewsets

from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.go, name='go'),
    url(r'^go$', views.go, name='go'),
    url(r'^gocust$', views.gocust, name='gocust'),
    url(r'^cutomercreate$', views.cutomercreate, name='cutomercreate'),
    url(r'^custview$', views.custview, name='custview'),
    url(r'^editcust/(?P<id>\d+)$', views.editcust, name='editcust'),
    url(r'^editcust/updatecust/(?P<id>\d+)$', views.updatecust, name='updatecust'),
    url(r'^deletecust/(?P<id>\d+)$', views.deletecust, name='deletecust'),

    url(r'^gosupp$', views.gosupp, name='gosupp'),
    url(r'^suppcreate$', views.suppcreate, name='suppcreate'),
    url(r'^suppview$', views.suppview, name='suppview'),
    url(r'^editsupp/(?P<id>\d+)$', views.editsupp, name='editsupp'),
    url(r'^editsupp/updatesupp/(?P<id>\d+)$', views.updatesupp, name='updatesupp'),
    url(r'^deletesupp/(?P<id>\d+)$', views.deletesupp, name='deletesupp'),


    url(r'^goitem$', views.goitem, name='goitem'),
    url(r'^createitem$', views.createitem, name='createitem'),
    url(r'^itemview$', views.itemview, name='itemview'),
    url(r'^edititem/(?P<id>\d+)$', views.edititem, name='edititem'),
    url(r'^edititem/updateitem/(?P<id>\d+)$', views.updateitem, name='updateitem'),
    url(r'^deleteitem/(?P<id>\d+)$', views.deleteitem, name='deleteitem'),


    url(r'^gojob$', views.gojob, name='gojob'),
    url(r'^createjob$', views.createjob, name='createjob'),
    url(r'^jobview$', views.jobview, name='jobview'),
    url(r'^editjob/(?P<id>\d+)$', views.editjob, name='editjob'),
    url(r'^editjob/updatejob/(?P<id>\d+)$', views.updatejob, name='updatejob'),
    url(r'^deletejob/(?P<id>\d+)$', views.deletejob, name='deletejob'),



    url(r'^gogroup$', views.gogroup, name='gogroup'),
    url(r'^groupcreate$', views.groupcreate, name='groupcreate'),
    url(r'^groupview$', views.groupview, name='groupview'),
    url(r'^editgroup/(?P<id>\d+)$', views.editgroup, name='editgroup'),
    url(r'^editgroup/updategroup/(?P<id>\d+)$', views.updategroup, name='updategroup'),
    url(r'^deletegroup/(?P<id>\d+)$', views.deletegroup, name='deletegroup'),


    url(r'^goledger$', views.goledger, name='goledger'),
    url(r'^ledgercreate$', views.ledgercreate, name='ledgercreate'),
    url(r'^ledgerview$', views.ledgerview, name='ledgerview'),
    url(r'^editledger/(?P<id>\d+)$', views.editledger, name='editledger'),
    url(r'^editledger/updateledger/(?P<id>\d+)$', views.updateledger, name='updateledger'),
    url(r'^deleteledger/(?P<id>\d+)$', views.deleteledger, name='deleteledger'),

    url(r'^goemp$', views.goemp, name='goemp'),
    url(r'^goaccount$', views.goaccount, name='goaccount'),
    url(r'^goasset$', views.goledger, name='goasset'),
    url(r'^assetcreate$', views.assetcreate, name='assetcreate'),
    url('asset/add', views.addnewasset, name='addnewasset'),
    url(r'^asset/edit/(?P<id>\d+)$', views.edit_asset, name='assetedit'),
    url(r'^asset/delete/(?P<id>\d+)$', views.delete_asset, name='assetdelete'),
    url('category',views.Category,name='category'),
    url('subcategory',views.SubCategory,name='subcategory'),


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)