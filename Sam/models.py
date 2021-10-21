from django.db import models
import datetime
import os

# Create your models here.


def filepath(request, filename):
    old_fname   =   filename
    timeNow     =   datetime.datetime.now().strftime('%Y%m%d%H%M%s')
    filename    =   "%s%s", (timeNow, old_fname)
    return os.path.join('uploads/', filename)


class Item(models.Model):
    item_name       =   models.TextField(max_length=100)
    item_desc       =   models.TextField(max_length=500, null=True)
    item_barcode    =   models.TextField(max_length=50)
    item_category   =   models.TextField(max_length=50)
    item_unit_prim  =   models.TextField(max_length=100)
    item_unit_sec   =   models.TextField(max_length=100)
    open_balance    =   models.TextField(max_length=100)
    buying_price    =   models.TextField(max_length=50)
    sell_price      =   models.TextField(max_length=50)
    image1          =   models.ImageField(upload_to='images/', null=True,verbose_name='')
    image2          =   models.ImageField(upload_to='images/', null=True,verbose_name='')
    image3          =   models.ImageField(upload_to='images/', null=True,verbose_name='')
    image4          =   models.ImageField(upload_to='images/', null=True,verbose_name='')


class Customer(models.Model):
    customer_name   =   models.TextField(max_length=100)
    vat_reg_no      =   models.TextField(max_length=100)
    cr_no           =   models.TextField(max_length=100)
    expired_on      =   models.TextField(max_length=100)
    land_phone      =   models.TextField(max_length=100)
    mobile          =   models.TextField(max_length=100)
    contact_person  =   models.TextField(max_length=100)
    contact_mobile  =   models.TextField(max_length=100)
    email           =   models.TextField(max_length=100)
    address         =   models.TextField(max_length=100)
    open_balance    =   models.TextField(max_length=100)
    credit_lim_am   =   models.TextField(max_length=100)
    credit_lim_dur  =   models.TextField(max_length=100)

class Supplier(models.Model):
    customer_name   =   models.TextField(max_length=100)
    vat_reg_no      =   models.TextField(max_length=100)
    cr_no           =   models.TextField(max_length=100)
    expired_on      =   models.TextField(max_length=100)
    land_phone      =   models.TextField(max_length=100)
    mobile          =   models.TextField(max_length=100)
    contact_person  =   models.TextField(max_length=100)
    contact_mobile  =   models.TextField(max_length=100)
    email           =   models.TextField(max_length=100)
    address         =   models.TextField(max_length=100)
    open_balance    =   models.TextField(max_length=100)
    credit_lim_am   =   models.TextField(max_length=100)
    credit_lim_dur  =   models.TextField(max_length=100)
    bank_acc_name   =   models.TextField(max_length=100)
    bank_acc_no     =   models.TextField(max_length=100)



class User(models.Model):
    mobile_no   =   models.TextField(max_length=100)
    username    =   models.TextField(max_length=100)
    password    =   models.TextField(max_length=100)


class Login(models.Model):
    username    =   models.TextField(max_length=100)
    password    =   models.TextField(max_length=100)

class Job(models.Model):
    job_name    =   models.TextField(max_length=100)
    job_desc    =   models.TextField(max_length=500,null=True)
    imag1       =   models.ImageField(upload_to='images/', null=True,blank=True)
    imag2       =   models.ImageField(upload_to='images/', null=True,blank=True)
    imag3       =   models.ImageField(upload_to='images/', null=True,blank=True)
    imag4       =   models.ImageField(upload_to='images/', null=True,blank=True)

class Employee(models.Model):
    emp_name     =    models.TextField(max_length=100)
    nationality  =    models.TextField(max_length=100)
    birth_date   =    models.TextField(max_length=100)
    joining_date =    models.TextField(max_length=100)
    designation  =    models.TextField(max_length=100)
    department   =    models.TextField(max_length=100)
    salary_categ =    models.TextField(max_length=100)
    passport_no  =    models.TextField(max_length=100)
    expir        =    models.TextField(max_length=100)
    id_no        =    models.TextField(max_length=100)
    id_expir     =    models.TextField(max_length=100)
    img1         =   models.ImageField(upload_to='images/', null=True,blank=True)
    img2         =   models.ImageField(upload_to='images/', null=True,blank=True)
    img3         =   models.ImageField(upload_to='images/', null=True,blank=True)
    img4         =   models.ImageField(upload_to='images/', null=True,blank=True)
    basic        =    models.TextField(max_length=100)
    housing      =    models.TextField(max_length=100)
    transportation =    models.TextField(max_length=100)
    food         =    models.TextField(max_length=100)
    mobile       =    models.TextField(max_length=100)
    other        =    models.TextField(max_length=100)
    netpay       =    models.TextField(max_length=100)


class Group(models.Model):
    group_name    =    models.TextField(max_length=100)
    category      =    models.TextField(max_length=100)


class Ledger(models.Model):
    ledger_name    =    models.TextField(max_length=100)
    group_name     =    models.TextField(max_length=100)
    category       =    models.TextField(max_length=100)
    opening_bal    =    models.TextField(max_length=100)


class Asset(models.Model):
    asset_parent   =   models.TextField(max_length=100)
    asset_child    =   models.TextField(max_length=100)
class Liabilities(models.Model):
    liability_parent   =   models.TextField(max_length=100)
    liability_child    =   models.TextField(max_length=100)
class Income(models.Model):
    income_parent   =   models.TextField(max_length=100)
    income_child    =   models.TextField(max_length=100)
class Expences(models.Model):
    expenses_parent   =   models.TextField(max_length=100)
    expenses_child    =   models.TextField(max_length=100)
class CustomerInvoice(models.Model):
    customer_invoice   =   models.TextField(max_length=100)
    report_date      =   models.TextField(max_length=100)
    invoice_no           =   models.TextField(max_length=100)
    cusomer_id      =   models.TextField(max_length=100)
    customer_name      =   models.TextField(max_length=100)
    si_no1          =   models.TextField(max_length=100)
    si_no2          =   models.TextField(max_length=100)
    date1  =   models.TextField(max_length=100)
    date2  =   models.TextField(max_length=100)
    ref_no1           =   models.TextField(max_length=100)
    ref_no2         =   models.TextField(max_length=100)
    description1    =   models.TextField(max_length=100)
    description2   =   models.TextField(max_length=100)
    item1  =   models.TextField(max_length=100)
    item2   =   models.TextField(max_length=100)
    qty1     =   models.TextField(max_length=100) 
    qty2     =   models.TextField(max_length=100)
    job1     =   models.TextField(max_length=100) 
    job2     =   models.TextField(max_length=100)
    sales_staff1     =   models.TextField(max_length=100) 
    sales_staff2     =   models.TextField(max_length=100) 
    amount     =   models.TextField(max_length=100) 
    balance_amount     =   models.TextField(max_length=100)     





    
