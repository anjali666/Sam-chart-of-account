from django.shortcuts import render, redirect
from django.core import serializers
from django.http import JsonResponse
from Sam.models import Customer, ItemInvoice,Ledger_Statement,Trial_Balance,Cash,PCash,Customers,Supplier,Suppliers,CustomerInvoice,SupplierInvoice,Group, Ledger, Item, Job, Asset,Category,SubCategory,ChildCategory
from .forms import ItemForm, JobForm,SupplierForm,CustomerInvoiceForm
from rest_framework import viewsets
from .serializers import CategorySerializer,SubCategorySerializer
from django.contrib import messages
from django.db import connection
from itertools import chain
def tablesjoin(request):
   queryset = CustomerInvoice.objects.all().select_related('customer_name').select_related('name')
def iteminvoice(request):
    return render(request,'Sam/item invoice.html')

def itemcreate(request):
    c = ItemInvoice(item_id=request.POST['item_id'],item_name=request.POST['item_name'],date=request.POST['date'],period=request.POST['period'],)
    c.save()
    return redirect( '/')
def go(request):
    return render(request,'Sam/dashboard.html')

def gocusts(request):
    return render(request,'Sam/customers.html')
def gocust(request):
    return render(request,'Sam/customer.html')
def cutomercreate(request):
    cust2 = Customer(customer_name=request.POST['customer_name'],vat_reg_no=request.POST['vat_reg_no'],cr_no=request.POST['cr_no'],expired_on=request.POST['expired_on'],land_phone=request.POST['land_phone'],mobile=request.POST['mobile'],contact_person=request.POST['contact_person'],contact_mobile=request.POST['contact_mobile'],email=request.POST['email'],address=request.POST['address'],open_balance=request.POST['open_balance'],credit_lim_am=request.POST['credit_lim_am'],credit_lim_dur=request.POST['credit_lim_dur'],)
    cust2.save()
    return redirect( '/')
def custview(request):
    cust1 = Customer.objects.all()
    context = {'cust': cust1}
    return render(request,'Sam/customer view.html', context)
def editcust(request,id):
    cust1 = Customer.objects.get(id=id)
    context = {'cust': cust1}
    return render(request,'Sam/edit customer.html',context)
def updatecust(request,id):
    cust = Customer.objects.get(id=id)
    cust.customer_name=request.POST['customer_name']
    cust.vat_reg_no = request.POST['vat_reg_no']
    cust.cr_no = request.POST['cr_no']
    cust.expired_on = request.POST['expired_on']
    cust.land_phone = request.POST['land_phone']
    cust.mobile = request.POST['mobile']
    cust.contact_person = request.POST['contact_person']
    cust.contact_mobile = request.POST['contact_mobile']
    cust.email = request.POST['email']
    cust.address = request.POST['address']
    cust.open_balance = request.POST['open_balance']
    cust.credit_lim_am = request.POST['credit_lim_am']
    cust.credit_lim_dur = request.POST['credit_lim_dur']

    cust.save()
    return render(request, 'Sam/dashboard.html')
def deletecust(request, id):
    cust = Customer.objects.get(id=id)
    cust.delete()
    return render(request, 'Sam/dashboard.html')




def gosupp(request):
    return render(request,'Sam/supplier.html')
def suppcreate(request):
    supp2 = Supplier(customer_name=request.POST['customer_name'],vat_reg_no=request.POST['vat_reg_no'],cr_no=request.POST['cr_no'],expired_on=request.POST['expired_on'],land_phone=request.POST['land_phone'],mobile=request.POST['mobile'],contact_person=request.POST['contact_person'],contact_mobile=request.POST['contact_mobile'],email=request.POST['email'],address=request.POST['address'],open_balance=request.POST['open_balance'],credit_lim_am=request.POST['credit_lim_am'],credit_lim_dur=request.POST['credit_lim_dur'],bank_acc_name=request.POST['bank_acc_name'],bank_acc_no=request.POST['bank_acc_no'],)
    supp2.save()
    return redirect( '/')
def suppview(request):
    supp1 = Supplier.objects.all()
    context = {'supp': supp1}
    return render(request,'Sam/supplier view.html', context)
def customersview(request):
    supp2 = Customers.objects.all()
    context = {'supp': supp2}
    return render(request,'Sam/chart_of_accounts.html', context)
def editsupp(request,id):
    supp1 = Supplier.objects.get(id=id)
    context = {'supp': supp1}
    return render(request,'Sam/edit supplier.html', context)
def updatesupp(request,id):
    supp = Supplier.objects.get(id=id)
    supp.customer_name=request.POST['customer_name']
    supp.vat_reg_no = request.POST['vat_reg_no']
    supp.cr_no = request.POST['cr_no']
    supp.expired_on = request.POST['expired_on']
    supp.land_phone = request.POST['land_phone']
    supp.mobile = request.POST['mobile']
    supp.contact_person = request.POST['contact_person']
    supp.contact_mobile = request.POST['contact_mobile']
    supp.email = request.POST['email']
    supp.address = request.POST['address']
    supp.open_balance = request.POST['open_balance']
    supp.credit_lim_am = request.POST['credit_lim_am']
    supp.credit_lim_dur = request.POST['credit_lim_dur']
    supp.bank_acc_name = request.POST['bank_acc_name']
    supp.bank_acc_no = request.POST['bank_acc_no']

    supp.save()
    return render(request, 'Sam/dashboard.html')
def deletesupp(request, id):
    supp = Supplier.objects.get(id=id)
    supp.delete()
    return render(request, 'Sam/dashboard.html')
def gotrialbalance(request):
    result=Ledger.objects.all()
    groups=Group.objects.all()
    category=Category.objects.all()
    cash_sale=Cash.objects.all()
    pcash=PCash.objects.all()
    
    return render(request,'Sam/Trial Balance.html',{"result": result,
        "groups":groups,
        "category": category,
        "cash_sale":cash_sale,"pcash":pcash,})
def trialbalancecreate(request):
    bln2 = Trial_Balance(date=request.POST['date'], reportdate=request.POST['reportdate'], )
    bln2.save()
    return redirect('/')

def goitem(request):
    return render(request,'Sam/item.html')
def createitem(request):
    if request.method == "POST":
        item_name = request.POST['item_name']
        item_desc = request.POST['item_desc']
        item_barcode = request.POST['item_barcode']
        item_category = request.POST['item_category']
        item_unit_prim = request.POST['item_unit_prim']
        item_unit_sec = request.POST['item_unit_sec']
        open_balance = request.POST['open_balance']
        buying_price = request.POST['buying_price']
        sell_price = request.POST['sell_price']
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')

        itm = Item.objects.create(item_name=item_name, item_desc=item_desc, item_barcode=item_barcode,
                                     item_category=item_category, item_unit_prim=item_unit_prim,item_unit_sec=item_unit_sec,
                                  open_balance=open_balance, buying_price=buying_price,
                                     sell_price=sell_price, image1=image1, image2=image2, image3=image3, image4=image4,)

        return redirect('go')





def itemview(request):
    itm = Item.objects.all()
    return render(request, 'Sam/item view.html', {'itmview': itm})
def edititem(request,id):
    itm = Item.objects.get(id=id)
    context = {'itmview': itm}
    return render(request,'Sam/edit item.html', context)
def updateitem(request,id):
    itm = Item.objects.get(id=id)
    form = ItemForm(request.POST, instance=itm)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'Sam/dashboard.html', {'itmview': itm})
def deleteitem(request, id):
    itm = Item.objects.get(id=id)
    itm.delete()
    return render(request, 'Sam/dashboard.html')



def gojob(request):
    return render(request,'Sam/job.html')
def createjob(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect(request, 'Sam/dashboard.html')
            except:
                pass

    else:
        form = JobForm()
    return render(request, 'Sam/dashboard.html', {'form': form})
def createcustomer(request):
    if request.method == "POST":
        form = CustomerInvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect(request, 'Sam/dashboard.html')
            except:
                pass

    else:
        form = CustomerInvoiceForm()
    return render(request, 'Sam/customer invoice.html', {'form': form})
def jobview(request):
    job = Job.objects.all()
    return render(request, 'Sam/job view.html', {'jobview': job})
def editjob(request,id):
    job = Job.objects.get(id=id)
    context = {'jobview': job}
    return render(request,'Sam/edit job.html', context)
def updatejob(request,id):
    job = Job.objects.get(id=id)
    form = JobForm(request.POST, instance=job)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'Sam/dashboard.html', {'jobview': job})
def deletejob(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    return render(request, 'Sam/dashboard.html')



def gogroup(request):
    category=Category.objects.all()
    return render(request,'Sam/group.html',{"category":category})
def groupcreate(request):
    
    if request.method == "POST":

        category_id = request.POST.get('category_id', None)
        grp2 = Group(group_name=request.POST['group_name'])
        results = Group(
            group_name=request.POST['group_name'],
            category_id=category_id,
            type = request.POST.get('type', "dynamic"), 
            status = request.POST.get('status', 1),
        )
        results.save()

        category = Category.objects.all()
        return render(request,'Sam/group.html',{"category":category})
def groupview(request):
    grp1 = Group.objects.all()
    context = {'grp': grp1}
    return render(request,'Sam/group view.html', context)
def editgroup(request,id):
    grp1 = Group.objects.get(id=id)
    context = {'grp': grp1}
    return render(request,'Sam/edit group.html', context)
def updategroup(request,id):
    grp = Group.objects.get(id=id)
    grp.group_name=request.POST['group_name']
    grp.category = request.POST['category']

    grp.save()
    return render(request, 'Sam/dashboard.html')
def deletegroup(request, id):
    grp = Group.objects.get(id=id)
    grp.delete()
    return render(request, 'Sam/dashboard.html')




def goledger(request):
    if request.method == "POST":
        group_id = request.POST.get('group_id', None)

        Group(group_id=group_id, group_name=request.POST['group_name'], status=1, type='dynamic').save()

        return redirect( '/Sam/goaccount')

    groups = Group.objects.all()
    ledgers=Ledger.objects.all()
    return render(request,'Sam/ledger.html',{"groups":groups,"ledgers":ledgers})
def gocashsale(request):
    return render(request, 'Sam/cash sale.html')
def cashcreate(request):
    csh2 = Cash(invoice_number=request.POST['invoice_number'],date=request.POST['date'],
                internal_ref_no=request.POST['internal_ref_no'],cash=request.POST['cash'],
                user_id=request.POST['user_id'],account=request.POST['account'],
                customer_id=request.POST['customer_id'],customer_name=request.POST['customer_name'],
                item_id1=request.POST['item_id1'],item_id2=request.POST['item_id2'],
                item_details1=request.POST['item_details1'],item_details2=request.POST['item_details2'],
                price1_1=request.POST['price1_1'],price1_2=request.POST['price1_2'],
                quantity1=request.POST['quantity1'],quantity2=request.POST['quantity2'],
                price2_1=request.POST['price2_1'], price2_2=request.POST['price2_2'],
                quantity3=request.POST['quantity3'], quantity4=request.POST['quantity4'],
                amount1=request.POST['amount1'], amount2=request.POST['amount2'],
                sales_ex1=request.POST['sales_ex1'], sales_ex2=request.POST['sales_ex2'],
                job1=request.POST['job1'], job2=request.POST['job2'],
                labour_charge=request.POST['labour_charge'], other_charge=request.POST['other_charge'],
                total1=request.POST['total1'], total2=request.POST['total2'],
                total3=request.POST['total3'], total4=request.POST['total4'],
                total5=request.POST['total5'], total6=request.POST['total6'],
                discount=request.POST['discount'], tax=request.POST['tax'],)
    csh2.save()
    return redirect( '/')
def gopcashsale(request):
    return render(request, 'Sam/cash purchase.html')
def pcashcreate(request):
    csh2 = PCash(invoice_number=request.POST['invoice_number'],date=request.POST['date'],
                internal_ref_no=request.POST['internal_ref_no'],cash=request.POST['cash'],
                user_id=request.POST['user_id'],account=request.POST['account'],
                supp_id=request.POST['supp_id'],supp_name=request.POST['supp_name'],
                item_id1=request.POST['item_id1'],item_id2=request.POST['item_id2'],
                item_details1=request.POST['item_details1'],item_details2=request.POST['item_details2'],
                price1_1=request.POST['price1_1'],price1_2=request.POST['price1_2'],
                quantity1=request.POST['quantity1'],quantity2=request.POST['quantity2'],
                price2_1=request.POST['price2_1'], price2_2=request.POST['price2_2'],
                quantity3=request.POST['quantity3'], quantity4=request.POST['quantity4'],
                amount1=request.POST['amount1'], amount2=request.POST['amount2'],
                sales_ex1=request.POST['sales_ex1'], sales_ex2=request.POST['sales_ex2'],
                job1=request.POST['job1'], job2=request.POST['job2'],
                labour_charge=request.POST['labour_charge'], other_charge=request.POST['other_charge'],
                total1=request.POST['total1'], total2=request.POST['total2'],
                total3=request.POST['total3'], total4=request.POST['total4'],
                total5=request.POST['total5'], total6=request.POST['total6'],
                discount=request.POST['discount'], tax=request.POST['tax'],)
    csh2.save()
    return redirect( '/')
def ledgercreate(request):
    group_id = request.POST.get('group_id', None)
    parent_id=request.POST.get('parent_id', None)
    
    ldg2 = Ledger(ledger_name=request.POST['ledger_name'],group_id=group_id,parent_id=parent_id,category=request.POST['category'],opening_bal=request.POST['opening_bal'],)
    ldg2.save()
    return redirect( '/')
def ledgerview(request):
    ldg1 = Ledger.objects.all()
    context = {'ldg': ldg1}
    return render(request,'Sam/ledger view.html', context)
def editledger(request,id):
    ldg1 = Ledger.objects.get(id=id)
    context = {'ldg': ldg1}
    return render(request,'Sam/edit ledger.html', context)
def updateledger(request,id):
    ldg = Ledger.objects.get(id=id)
    ldg.ledger_name = request.POST['ledger_name']
    ldg.group_name = request.POST['group_name']
    ldg.category = request.POST['category']
    ldg.opening_bal = request.POST['opening_bal']

    ldg.save()
    return render(request, 'Sam/dashboard.html')
def deleteledger(request, id):
    ldg = Ledger.objects.get(id=id)
    ldg.delete()
    return render(request, 'Sam/dashboard.html')



def goemp(request):
    return render(request,'Sam/employee.html')

def find_child_category(ledgers, parent_id, parent_index):
    children = []
    groups=[]
    ledgers=[]
    index = 1;
    for cat in groups:
        if cat.parent_id == parent_id:
            children.append({
                "sl_no": parent_index + ' . ' + str(index),
                "id": cat.id,
                "name": cat.ledger_name,
                "type": cat.type,
                "status": cat.status,
                "children": find_child_category(ledgers, cat.id, parent_index + ' . ' + str(index))
            })
            index += 1

    return ledgers

def goaccount(request):
    groups=Group.objects.all()
    category=Category.objects.all()
    ledgers = Ledger.objects.filter(parent_id__isnull=True)
    subLedgers = Ledger.objects.exclude(parent_id__isnull=True)
    sundry_debtors = Customer.objects.all()
    sundry_creditors = Supplier.objects.all()
    closing_stock=Item.objects.all()
    # ledgers=[]
    # index = 1;
    # for cat in ledgersAll:
    #     if not cat.parent_id:
    #         ledgers.append({
    #             "sl_no": index,
    #             "id": cat.id,
    #             "name": cat.ledger_name,
            
    #             "children": find_child_category(ledgers, cat.id, str(index))
    #         })
    #         index += 1;
    
    return render(request,'Sam/chart_of_account.html', {
        "groups": groups,
        "ledgers":ledgers,
        "subLedgers": subLedgers,
        "category":category,
        "ledgers":ledgers,
        "sundry_debtors": sundry_debtors,
        "sundry_creditors": sundry_creditors,
        "closing_stock": closing_stock,
        "blank_data": []
    })
def goledgerstmt(request):
    result=Ledger.objects.all()
    groups=Group.objects.all()
    category=Category.objects.all()
    cash_sale=Cash.objects.all()
    pcash=PCash.objects.all()
    a=123
    b=12
    c=12
    d=(b+c)
    return render(request,'Sam/ledgers.html',{"result":result,"category":category,"groups":groups,"category":category,"cash_sale":cash_sale,"pcash":pcash})
def ldgrstmtcreate(request):
    ldgr2 = Ledger_Statement(date=request.POST['date'],ledger_name=request.POST['ledger_name'],ledger_id=request.POST['ledger_id'],period=request.POST['period'],)
    ldgr2.save()
    return redirect( '/')
# def goledgerjournal(request):
#     return render(request,'Sam/All Journal Entry.html')
# def ldgrjournalcreate(request):
#     ldgr2 = Ledger_Journal(date=request.POST['date'],reportdate=request.POST['reportdate'],)
#     ldgr2.save()
#     return redirect( '/')
def goasset(request):
    results=Group.objects.all()

    return render(request,'Sam/chart_of_account.html',{Group:results,})

def find_child_assets(request):
    if request.is_ajax and request.method == "GET":

        parent_id = request.GET.get("parent_id", None)
        assets = Asset.objects.filter(parent_id=parent_id)

        children = serializers.serialize('json', [assets])
        return JsonResponse({"children": children}, status=200)

    return JsonResponse({}, status = 400)

def addnewasset(request):
      if request.method == "POST":

        parent_id = request.POST.get('parent_id', None)

        results = Category(
            category_name=request.POST['category_name'],
            parent_id=parent_id,
            type = request.POST.get('type', "dynamic"), 
            status = request.POST.get('status', 1),
        )
        results.save()

      result = Category.objects.all()
      return render(request,'Sam/add_new_asset.html',{"result":result})
def custinvoice(request):
    return render(request,'Sam/customer invoice.html')
def cinvocreate(request):
    c = CustomerInvoice(cusomer_id=request.POST['cusomer_id'],customer_name=request.POST['customer_name'],report_date=request.POST['report_date'],invoice_no=request.POST['invoice_no'],)
    c.save()
    return redirect( '/')


def supinvoice(request):
    return render(request,'Sam/supplier invoice.html')
def sinvocreate(request):
    c = SupplierInvoice(supplier_id=request.POST['supplier_id'],supplier_name=request.POST['supplier_name'],report_date=request.POST['report_date'],invoice_no=request.POST['invoice_no'],)
    c.save()
    return redirect( '/')
def edit_asset(request):
    
 
    result= Ledger(ledger_name=request.POST.get('ledger_name',None))
    result.save()
    results = Ledger.objects.all()
    
    return render(request,'Sam/edit_asset.html', {"results": results,})

def delete_asset(request, id):
    Category.objects.filter(parent_id=id).delete()
    Category.objects.filter(id=id).delete()

    return redirect( '/Sam/goaccount')

def assetcreate(request):
    ast2 = Asset(asset_parent=request.POST['asset_parent'],asset_child=request.POST['asset_child'],new_child=request.POST['new_child'],child=request.POST['child'])
    ast2.save()
    return redirect( '/')


class CategoryClass():

    serializer_class = CategorySerializer
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user is not None:
                if user.is_active and user.is_superuser:
                    return Category.objects.all()

class SubCategory():

  def get_queryset(self):
    id_child = self.request.query_params.get('id_child')
    queryset = super().get_queryset()
    if id_child:
        queryset = queryset.filter(id_parent=id_child)
    return queryset
class ChildCategory():

  def get_queryset(self):
    id_child = self.request.query_params.get('id_child')
    queryset = super().get_queryset()
    if id_child:
        queryset = queryset.filter(id_child=id_child)
    return queryset


    serializer_class = SubCategorySerializer













