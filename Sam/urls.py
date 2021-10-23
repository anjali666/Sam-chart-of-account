from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

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
    url(r'^goasset$', views.goasset, name='goasset'),
    url(r'^assetcreate$', views.assetcreate, name='assetcreate'),

    url(r'^goliability$', views.goliability, name='goliability'),
    url(r'^liabilitycreate$', views.liabilitycreate, name='liabilitycreate'),
    url(r'^goincome$', views.goincome, name='goincome'),
    url(r'^incomecreate$', views.incomecreate, name='incomecreate'),
    url(r'^goexpences$', views.goexpences, name='goexpences'),
    url(r'^expencescreate$', views.expencescreate, name='expencescreate'),

    url(r'^gosales$', views.gosales, name='gosales'),
    url(r'^gocashsale$', views.gocashsale, name='gocashsale'),
    url(r'^cashcreate$', views.cashcreate, name='cashcreate'),
    url(r'^cashview$', views.cashview, name='cashview'),
    url(r'^editcash/(?P<id>\d+)$', views.editcash, name='editcash'),
    url(r'^editcash/updatecash/(?P<id>\d+)$', views.updatecash, name='updatecash'),
    url(r'^deletecash/(?P<id>\d+)$', views.deletecash, name='deletecash'),

    url(r'^gocreditsale$', views.gocreditsale, name='gocreditsale'),
    url(r'^creditcreate$', views.creditcreate, name='creditcreate'),
    url(r'^creditview$', views.creditview, name='creditview'),
    url(r'^editcredit/(?P<id>\d+)$', views.editcredit, name='editcredit'),
    url(r'^editcredit/updatecredit/(?P<id>\d+)$', views.updatecredit, name='updatecredit'),
    url(r'^deletecredit/(?P<id>\d+)$', views.deletecredit, name='deletecredit'),

    url(r'^gosreturnsale$', views.gosreturnsale, name='gosreturnsale'),
    url(r'^sreturncreate$', views.sreturncreate, name='sreturncreate'),
    url(r'^sreturnview$', views.sreturnview, name='sreturnview'),
    url(r'^editsreturn/(?P<id>\d+)$', views.editsreturn, name='editsreturn'),
    url(r'^editsreturn/updatesreturn/(?P<id>\d+)$', views.updatesreturn, name='updatesreturn'),
    url(r'^deletesreturn/(?P<id>\d+)$', views.deletesreturn, name='deletesreturn'),

    url(r'^goreceipt$', views.goreceipt, name='goreceipt'),
    url(r'^receiptcreate$', views.receiptcreate, name='receiptcreate'),
    url(r'^receiptview$', views.receiptview, name='receiptview'),
    url(r'^editreceipt/(?P<id>\d+)$', views.editreceipt, name='editreceipt'),
    url(r'^editreceipt/updatereceipt/(?P<id>\d+)$', views.updatereceipt, name='updatereceipt'),
    url(r'^deletereceipt/(?P<id>\d+)$', views.deletereceipt, name='deletereceipt'),

    url(r'^gopsales$', views.gopsales, name='gopsales'),
    url(r'^gopcashsale$', views.gopcashsale, name='gopcashsale'),
    url(r'^pcashcreate$', views.pcashcreate, name='pcashcreate'),
    url(r'^pcashview$', views.pcashview, name='pcashview'),
    url(r'^editpcash/(?P<id>\d+)$', views.editpcash, name='editpcash'),
    url(r'^editpcash/updatepcash/(?P<id>\d+)$', views.updatepcash, name='updatepcash'),
    url(r'^deletepcash/(?P<id>\d+)$', views.deletepcash, name='deletepcash'),

    url(r'^gopcreditsale$', views.gopcreditsale, name='gopcreditsale'),
    url(r'^pcreditcreate$', views.pcreditcreate, name='pcreditcreate'),
    url(r'^pcreditview$', views.pcreditview, name='pcreditview'),
    url(r'^editpcredit/(?P<id>\d+)$', views.editpcredit, name='editpcredit'),
    url(r'^editpcredit/updatepcredit/(?P<id>\d+)$', views.updatepcredit, name='updatepcredit'),
    url(r'^deletepcredit/(?P<id>\d+)$', views.deletepcredit, name='deletepcredit'),

    url(r'^gopsreturnsale$', views.gopsreturnsale, name='gopsreturnsale'),
    url(r'^psreturncreate$', views.psreturncreate, name='psreturncreate'),
    url(r'^psreturnview$', views.psreturnview, name='psreturnview'),
    url(r'^editpsreturn/(?P<id>\d+)$', views.editpsreturn, name='editpsreturn'),
    url(r'^editpsreturn/updatepsreturn/(?P<id>\d+)$', views.updatepsreturn, name='updatepsreturn'),
    url(r'^deletepsreturn/(?P<id>\d+)$', views.deletepsreturn, name='deletepsreturn'),

    url(r'^gopreceipt$', views.gopreceipt, name='gopreceipt'),
    url(r'^preceiptcreate$', views.preceiptcreate, name='preceiptcreate'),
    url(r'^preceiptview$', views.preceiptview, name='preceiptview'),
    url(r'^editpreceipt/(?P<id>\d+)$', views.editpreceipt, name='editpreceipt'),
    url(r'^editpreceipt/updatepreceipt/(?P<id>\d+)$', views.updatepreceipt, name='updatepreceipt'),
    url(r'^deletepreceipt/(?P<id>\d+)$', views.deletepreceipt, name='deletepreceipt'),



]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)