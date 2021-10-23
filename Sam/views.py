from django.shortcuts import render, redirect
from Sam.models import Customer, CustomerInvoice, Expences, Income, ItemInvoice, Liabilities, Supplier, Group, Ledger, Item, Job, Asset, SupplierInvoice
from .forms import ItemForm, JobForm


def go(request):
    return render(request,'Sam/dashboard.html')

def custinvoice(request):
    return render(request,'Sam/customer invoice.html')
def cinvocreate(request):
    c = CustomerInvoice(report_date=request.POST['report_date'],invoice_no=request.POST['invoice_no'],cusomer_id=request.POST['cusomer_id'],customer_name=request.POST['customer_name'],)
    c.save()
    return redirect( '/')

def supinvoice(request):
    return render(request,'Sam/supplier invoice.html')

def sinvocreate(request):
    c = SupplierInvoice(supplier_id=request.POST['supplier_id'],supplier_name=request.POST['supplier_name'],report_date=request.POST['report_date'],invoice_no=request.POST['invoice_no'],)
    c.save()
    return redirect( '/')

def iteminvoice(request):
    return render(request,'Sam/item invoice.html')

def itemcreate(request):
    c = ItemInvoice(item_id=request.POST['item_id'],item_name=request.POST['item_name'],date=request.POST['date'],period=request.POST['period'],)
    c.save()
    return redirect( '/')







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
    return render(request,'Sam/group.html')
def groupcreate(request):
    grp2 = Group(group_name=request.POST['group_name'],category=request.POST['category'],)
    grp2.save()
    return redirect( '/')
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
    return render(request,'Sam/ledger.html')
def ledgercreate(request):
    ldg2 = Ledger(ledger_name=request.POST['ledger_name'],group_name=request.POST['group_name'],category=request.POST['category'],opening_bal=request.POST['opening_bal'],)
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
def goaccount(request):
    return render(request,'Sam/chart of account.html')
def goasset(request):
    return render(request,'Sam/Add new asset.html')

def assetcreate(request):
    ast2 = Asset(asset_parent=request.POST['asset_parent'],asset_child=request.POST['asset_child'],)
    ast2.save()
    return redirect( '/')

def goliability(request):
    return render(request,'Sam/Add new liability.html')
def liabilitycreate(request):
    lbt2 = Liabilities(liability_parent=request.POST['liability_parent'],liability_child=request.POST['liability_child'],)
    lbt2.save()
    return redirect( '/')
def goincome(request):
    return render(request,'Sam/Add new income.html')
def incomecreate(request):
    inm2 = Income(income_parent=request.POST['income_parent'],income_child=request.POST['income_child'],)
    inm2.save()
    return redirect( '/')
def goexpences(request):
    return render(request,'Sam/Add new expences.html')
def expencescreate(request):
    exp2 = Expences(expenses_parent=request.POST['expenses_parent'],expenses_child=request.POST['expenses_child'],)
    exp2.save()
    return redirect( '/')

def gosales(request):
    return render(request, 'Sam/Sales.html')
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
def cashview(request):
    csh1 = Cash.objects.all()
    context = {'csh': csh1}
    return render(request,'Sam/show cash sales.html', context)
def editcash(request,id):
    csh1 = Cash.objects.get(id=id)
    context = {'csh': csh1}
    return render(request,'Sam/edit cash sales.html', context)
def updatecash(request,id):
    csh = Cash.objects.get(id=id)
    csh.invoice_number = request.POST['invoice_number']
    csh.date = request.POST['date']
    csh.internal_ref_no = request.POST['internal_ref_no']
    csh.cash = request.POST['cash']
    csh.user_id = request.POST['user_id']
    csh.account = request.POST['account'],
    csh.customer_id = request.POST['customer_id']
    csh.customer_name = request.POST['customer_name']
    csh.item_id1 = request.POST['item_id1']
    csh.item_id2 = request.POST['item_id2']
    csh.item_details1 = request.POST['item_details1']
    csh.item_details2 = request.POST['item_details2']
    csh.price1_1 = request.POST['price1_1']
    csh.price1_2 = request.POST['price1_2']
    csh.quantity1 = request.POST['quantity1']
    csh.quantity2 = request.POST['quantity2']
    csh.price2_1 = request.POST['price2_1']
    csh.price2_2 = request.POST['price2_2']
    csh.quantity3 = request.POST['quantity3']
    csh.quantity4 = request.POST['quantity4']
    csh.amount1 = request.POST['amount1']
    csh.amount2 = request.POST['amount2']
    csh.sales_ex1 = request.POST['sales_ex1']
    csh.sales_ex2 = request.POST['sales_ex2']
    csh.job1 = request.POST['job1']
    csh.job2 = request.POST['job2']
    csh.labour_charge = request.POST['labour_charge']
    csh.other_charge = request.POST['other_charge']
    csh.total1 = request.POST['total1']
    csh.total2 = request.POST['total2']
    csh.total3 = request.POST['total3']
    csh.total4 = request.POST['total4']
    csh.total5 = request.POST['total5']
    csh.total6 = request.POST['total6']
    csh.discount = request.POST['discount']
    csh.tax = request.POST['tax']
    csh.save()
    return render(request, 'Sam/Sales.html')
def deletecash(request, id):
    csh = Cash.objects.get(id=id)
    csh.delete()
    return render(request, 'Sam/Sales.html')


def gocreditsale(request):
    return render(request, 'Sam/credit sales.html')
def creditcreate(request):
    crd2 = Credit(invoice_number=request.POST['invoice_number'],date=request.POST['date'],
                internal_ref_no=request.POST['internal_ref_no'],due_on=request.POST['due_on'],
                user_id=request.POST['user_id'],credit_limit_amt=request.POST['credit_limit_amt'],
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
    crd2.save()
    return redirect( '/')
def creditview(request):
    crd1 = Credit.objects.all()
    context = {'crd': crd1}
    return render(request,'Sam/show credit sales.html', context)
def editcredit(request,id):
    crd1 = Credit.objects.get(id=id)
    context = {'crd': crd1}
    return render(request,'Sam/edit credit sales.html', context)
def updatecredit(request,id):
    crd = Credit.objects.get(id=id)
    crd.invoice_number = request.POST['invoice_number']
    crd.date = request.POST['date']
    crd.internal_ref_no = request.POST['internal_ref_no']
    crd.due_on = request.POST['due_on']
    crd.user_id = request.POST['user_id']
    crd.credit_limit_amt = request.POST['credit_limit_amt'],
    crd.customer_id = request.POST['customer_id']
    crd.customer_name = request.POST['customer_name']
    crd.item_id1 = request.POST['item_id1']
    crd.item_id2 = request.POST['item_id2']
    crd.item_details1 = request.POST['item_details1']
    crd.item_details2 = request.POST['item_details2']
    crd.price1_1 = request.POST['price1_1']
    crd.price1_2 = request.POST['price1_2']
    crd.quantity1 = request.POST['quantity1']
    crd.quantity2 = request.POST['quantity2']
    crd.price2_1 = request.POST['price2_1']
    crd.price2_2 = request.POST['price2_2']
    crd.quantity3 = request.POST['quantity3']
    crd.quantity4 = request.POST['quantity4']
    crd.amount1 = request.POST['amount1']
    crd.amount2 = request.POST['amount2']
    crd.sales_ex1 = request.POST['sales_ex1']
    crd.sales_ex2 = request.POST['sales_ex2']
    crd.job1 = request.POST['job1']
    crd.job2 = request.POST['job2']
    crd.labour_charge = request.POST['labour_charge']
    crd.other_charge = request.POST['other_charge']
    crd.total1 = request.POST['total1']
    crd.total2 = request.POST['total2']
    crd.total3 = request.POST['total3']
    crd.total4 = request.POST['total4']
    crd.total5 = request.POST['total5']
    crd.total6 = request.POST['total6']
    crd.discount = request.POST['discount']
    crd.tax = request.POST['tax']
    crd.save()
    return render(request, 'Sam/Sales.html')
def deletecredit(request, id):
    crd = Credit.objects.get(id=id)
    crd.delete()
    return render(request, 'Sam/Sales.html')


def gosreturnsale(request):
    return render(request, 'Sam/sales return.html')
def sreturncreate(request):
    rtn2 = Sales_Return(invoice_number=request.POST['invoice_number'],date=request.POST['date'],
                internal_ref_no=request.POST['internal_ref_no'],
                user_id=request.POST['user_id'],
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
    rtn2.save()
    return redirect( '/')
def sreturnview(request):
    rtn1 = Sales_Return.objects.all()
    context = {'rtn': rtn1}
    return render(request,'Sam/show sales return.html', context)
def editsreturn(request,id):
    rtn1 = Sales_Return.objects.get(id=id)
    context = {'rtn': rtn1}
    return render(request,'Sam/edit sales return.html', context)
def updatesreturn(request,id):
    rtn = Sales_Return.objects.get(id=id)
    rtn.invoice_number = request.POST['invoice_number']
    rtn.date = request.POST['date']
    rtn.internal_ref_no = request.POST['internal_ref_no']
    rtn.user_id = request.POST['user_id']
    rtn.customer_id = request.POST['customer_id']
    rtn.customer_name = request.POST['customer_name']
    rtn.item_id1 = request.POST['item_id1']
    rtn.item_id2 = request.POST['item_id2']
    rtn.item_details1 = request.POST['item_details1']
    rtn.item_details2 = request.POST['item_details2']
    rtn.price1_1 = request.POST['price1_1']
    rtn.price1_2 = request.POST['price1_2']
    rtn.quantity1 = request.POST['quantity1']
    rtn.quantity2 = request.POST['quantity2']
    rtn.price2_1 = request.POST['price2_1']
    rtn.price2_2 = request.POST['price2_2']
    rtn.quantity3 = request.POST['quantity3']
    rtn.quantity4 = request.POST['quantity4']
    rtn.amount1 = request.POST['amount1']
    rtn.amount2 = request.POST['amount2']
    rtn.sales_ex1 = request.POST['sales_ex1']
    rtn.sales_ex2 = request.POST['sales_ex2']
    rtn.job1 = request.POST['job1']
    rtn.job2 = request.POST['job2']
    rtn.labour_charge = request.POST['labour_charge']
    rtn.other_charge = request.POST['other_charge']
    rtn.total1 = request.POST['total1']
    rtn.total2 = request.POST['total2']
    rtn.total3 = request.POST['total3']
    rtn.total4 = request.POST['total4']
    rtn.total5 = request.POST['total5']
    rtn.total6 = request.POST['total6']
    rtn.discount = request.POST['discount']
    rtn.tax = request.POST['tax']
    rtn.save()
    return render(request, 'Sam/Sales.html')
def deletesreturn(request, id):
    rtn = Sales_Return.objects.get(id=id)
    rtn.delete()
    return render(request, 'Sam/Sales.html')


def goreceipt(request):
    return render(request, 'Sam/Receipt.html')
def receiptcreate(request):
    rpt2 = Receipt(receipt_number=request.POST['receipt_number'], date=request.POST['date'], internal_ref_no=request.POST['internal_ref_no'],
    due_on=request.POST['due_on'], credit_limit_amt=request.POST['credit_limit_amt'], user_id=request.POST['user_id'],
    customer_id=request.POST['customer_id'], customer_name = request.POST['customer_name'],invoice_no1 = request.POST['invoice_no1'],
    invoice_no2 = request.POST['invoice_no2'],invoice_no3 = request.POST['invoice_no3'],invoice_date1 = request.POST['invoice_date1'],
    invoice_date2 = request.POST['invoice_date2'],invoice_date3 = request.POST['invoice_date3'],duedate1 = request.POST['duedate1'],
    duedate2 = request.POST['duedate2'],duedate3 = request.POST['duedate3'],invoice_amt1 = request.POST['invoice_amt1'],
    invoice_amt2 = request.POST['invoice_amt2'],invoice_amt3 = request.POST['invoice_amt3'],received_amt1 = request.POST['received_amt1'],
    received_amt2 = request.POST['received_amt2'],received_amt3 = request.POST['received_amt3'],outstanding1 = request.POST['outstanding1'],
    outstanding2 = request.POST['outstanding2'],outstanding3 = request.POST['outstanding3'],discount1 = request.POST['discount1'],discount2 = request.POST['discount2'],
    discount3 = request.POST['discount3'],balance_amt1 = request.POST['balance_amt1'],balance_amt2 = request.POST['balance_amt2'],balance_amt3 = request.POST['balance_amt3'],
    tick_space1 = request.POST['tick_space1'],tick_space2 = request.POST['tick_space2'],tick_space3 = request.POST['tick_space3'],partial1 = request.POST['partial1'],
    partial2 = request.POST['partial2'],partial3 = request.POST['partial3'],total1 = request.POST['total1'],total2 = request.POST['total2'],
    total3 = request.POST['total3'],total4 = request.POST['total4'],total5 = request.POST['total5'],total6 = request.POST['total6'],
    on_account = request.POST['on_account'],discount = request.POST['discount'],)
    rpt2.save()
    return redirect('/')


def receiptview(request):
    rpt1 = Receipt.objects.all()
    context = {'rpt': rpt1}
    return render(request,'Sam/Show receipt.html', context)
def editreceipt(request,id):
    rpt1 = Receipt.objects.get(id=id)
    context = {'rpt': rpt1}
    return render(request,'Sam/edit receipt.html', context)
def updatereceipt(request,id):
    rpt = Receipt.objects.get(id=id)
    rpt.receipt_number=request.POST['receipt_number']
    rpt.date = request.POST['date']
    rpt.internal_ref_no = request.POST['internal_ref_no']
    rpt.due_on = request.POST['due_on']
    rpt.credit_limit_amt = request.POST['credit_limit_amt']
    rpt.user_id = request.POST['user_id']
    rpt.customer_id = request.POST['customer_id']
    rpt.customer_name = request.POST['customer_name']
    rpt.invoice_no1 = request.POST['invoice_no1']
    rpt.invoice_no2 = request.POST['invoice_no2']
    rpt.invoice_no3 = request.POST['invoice_no3']
    rpt.invoice_date1 = request.POST['invoice_date1']
    rpt.invoice_date2 = request.POST['invoice_date2']
    rpt.invoice_date3 = request.POST['invoice_date3']
    rpt.duedate1 = request.POST['duedate1']
    rpt.invoice_amt2 = request.POST['invoice_amt2']
    rpt.invoice_amt3 = request.POST['invoice_amt3']
    rpt.received_amt1 = request.POST['received_amt1']
    rpt.received_amt2 = request.POST['received_amt2']
    rpt.received_amt3 = request.POST['received_amt3']
    rpt.outstanding1 = request.POST['outstanding1']
    rpt.outstanding2 = request.POST['outstanding2']
    rpt.outstanding3 = request.POST['outstanding3']
    rpt.discount1 = request.POST['discount1']
    rpt.discount2 = request.POST['discount2']
    rpt.discount3 = request.POST['discount3']
    rpt.balance_amt1 = request.POST['balance_amt1']
    rpt.balance_amt2 = request.POST['balance_amt2']
    rpt.balance_amt3 = request.POST['balance_amt3']
    rpt.tick_space1 = request.POST['tick_space1']
    rpt.tick_space2 = request.POST['tick_space2']
    rpt.tick_space3 = request.POST['tick_space3']
    rpt.partial1 = request.POST['partial1']
    rpt.partial2 = request.POST['partial2']
    rpt.partial3 = request.POST['partial3']
    rpt.total1 = request.POST['total1']
    rpt.total2 = request.POST['total2']
    rpt.total3 = request.POST['total3']
    rpt.total4 = request.POST['total4']
    rpt.total5 = request.POST['total5']
    rpt.total6 = request.POST['total6']
    rpt.on_account = request.POST['on_account']
    rpt.discount = request.POST['discount']

    rpt.save()
    return render(request, 'Sam/Sales.html')
def deletereceipt(request, id):
    rpt = Receipt.objects.get(id=id)
    rpt.delete()
    return render(request, 'Sam/Sales.html')






def gopsales(request):
    return render(request, 'Sam/purchase.html')
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
def pcashview(request):
    csh1 = PCash.objects.all()
    context = {'csh': csh1}
    return render(request,'Sam/show cash purchase.html', context)
def editpcash(request,id):
    csh1 = PCash.objects.get(id=id)
    context = {'csh': csh1}
    return render(request,'Sam/edit cash purchase.html', context)
def updatepcash(request,id):
    csh = PCash.objects.get(id=id)
    csh.invoice_number = request.POST['invoice_number']
    csh.date = request.POST['date']
    csh.internal_ref_no = request.POST['internal_ref_no']
    csh.cash = request.POST['cash']
    csh.user_id = request.POST['user_id']
    csh.account = request.POST['account'],
    csh.supp_id = request.POST['supp_id']
    csh.supp_name = request.POST['supp_name']
    csh.item_id1 = request.POST['item_id1']
    csh.item_id2 = request.POST['item_id2']
    csh.item_details1 = request.POST['item_details1']
    csh.item_details2 = request.POST['item_details2']
    csh.price1_1 = request.POST['price1_1']
    csh.price1_2 = request.POST['price1_2']
    csh.quantity1 = request.POST['quantity1']
    csh.quantity2 = request.POST['quantity2']
    csh.price2_1 = request.POST['price2_1']
    csh.price2_2 = request.POST['price2_2']
    csh.quantity3 = request.POST['quantity3']
    csh.quantity4 = request.POST['quantity4']
    csh.amount1 = request.POST['amount1']
    csh.amount2 = request.POST['amount2']
    csh.sales_ex1 = request.POST['sales_ex1']
    csh.sales_ex2 = request.POST['sales_ex2']
    csh.job1 = request.POST['job1']
    csh.job2 = request.POST['job2']
    csh.labour_charge = request.POST['labour_charge']
    csh.other_charge = request.POST['other_charge']
    csh.total1 = request.POST['total1']
    csh.total2 = request.POST['total2']
    csh.total3 = request.POST['total3']
    csh.total4 = request.POST['total4']
    csh.total5 = request.POST['total5']
    csh.total6 = request.POST['total6']
    csh.discount = request.POST['discount']
    csh.tax = request.POST['tax']
    csh.save()
    return render(request, 'Sam/purchase.html')
def deletepcash(request, id):
    csh = PCash.objects.get(id=id)
    csh.delete()
    return render(request, 'Sam/purchase.html')


def gopcreditsale(request):
    return render(request, 'Sam/credit purchase.html')
def pcreditcreate(request):
    crd2 = PCredit(invoice_number=request.POST['invoice_number'],date=request.POST['date'],
                internal_ref_no=request.POST['internal_ref_no'],due_on=request.POST['due_on'],
                user_id=request.POST['user_id'],credit_limit_amt=request.POST['credit_limit_amt'],
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
    crd2.save()
    return redirect( '/')
def pcreditview(request):
    crd1 = PCredit.objects.all()
    context = {'crd': crd1}
    return render(request,'Sam/show credit puchase.html', context)
def editpcredit(request,id):
    crd1 = PCredit.objects.get(id=id)
    context = {'crd': crd1}
    return render(request,'Sam/edit credit purchase.html', context)
def updatepcredit(request,id):
    crd = PCredit.objects.get(id=id)
    crd.invoice_number = request.POST['invoice_number']
    crd.date = request.POST['date']
    crd.internal_ref_no = request.POST['internal_ref_no']
    crd.due_on = request.POST['due_on']
    crd.user_id = request.POST['user_id']
    crd.credit_limit_amt = request.POST['credit_limit_amt'],
    crd.supp_id = request.POST['supp_id']
    crd.supp_name = request.POST['supp_name']
    crd.item_id1 = request.POST['item_id1']
    crd.item_id2 = request.POST['item_id2']
    crd.item_details1 = request.POST['item_details1']
    crd.item_details2 = request.POST['item_details2']
    crd.price1_1 = request.POST['price1_1']
    crd.price1_2 = request.POST['price1_2']
    crd.quantity1 = request.POST['quantity1']
    crd.quantity2 = request.POST['quantity2']
    crd.price2_1 = request.POST['price2_1']
    crd.price2_2 = request.POST['price2_2']
    crd.quantity3 = request.POST['quantity3']
    crd.quantity4 = request.POST['quantity4']
    crd.amount1 = request.POST['amount1']
    crd.amount2 = request.POST['amount2']
    crd.sales_ex1 = request.POST['sales_ex1']
    crd.sales_ex2 = request.POST['sales_ex2']
    crd.job1 = request.POST['job1']
    crd.job2 = request.POST['job2']
    crd.labour_charge = request.POST['labour_charge']
    crd.other_charge = request.POST['other_charge']
    crd.total1 = request.POST['total1']
    crd.total2 = request.POST['total2']
    crd.total3 = request.POST['total3']
    crd.total4 = request.POST['total4']
    crd.total5 = request.POST['total5']
    crd.total6 = request.POST['total6']
    crd.discount = request.POST['discount']
    crd.tax = request.POST['tax']
    crd.save()
    return render(request, 'Sam/purchase.html')
def deletepcredit(request, id):
    crd = PCredit.objects.get(id=id)
    crd.delete()
    return render(request, 'Sam/purchase.html')


def gopsreturnsale(request):
    return render(request, 'Sam/purchase return.html')
def psreturncreate(request):
    rtn2 = PRSales_Return(invoice_number=request.POST['invoice_number'],date=request.POST['date'],
                internal_ref_no=request.POST['internal_ref_no'],
                user_id=request.POST['user_id'],due_on=request.POST['due_on'], credit_limit_amt=request.POST['credit_limit_amt'],
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
    rtn2.save()
    return redirect( '/')
def psreturnview(request):
    rtn1 = PRSales_Return.objects.all()
    context = {'rtn': rtn1}
    return render(request,'Sam/show purchase return.html', context)
def editpsreturn(request,id):
    rtn1 = PRSales_Return.objects.get(id=id)
    context = {'rtn': rtn1}
    return render(request,'Sam/edit purchase return.html', context)
def updatepsreturn(request,id):
    rtn = PRSales_Return.objects.get(id=id)
    rtn.invoice_number = request.POST['invoice_number']
    rtn.date = request.POST['date']
    rtn.internal_ref_no = request.POST['internal_ref_no']
    rtn.user_id = request.POST['user_id']
    rtn.due_on = request.POST['due_on']
    rtn.credit_limit_amt = request.POST['credit_limit_amt'],
    rtn.supp_id = request.POST['supp_id']
    rtn.supp_name = request.POST['supp_name']
    rtn.item_id1 = request.POST['item_id1']
    rtn.item_id2 = request.POST['item_id2']
    rtn.item_details1 = request.POST['item_details1']
    rtn.item_details2 = request.POST['item_details2']
    rtn.price1_1 = request.POST['price1_1']
    rtn.price1_2 = request.POST['price1_2']
    rtn.quantity1 = request.POST['quantity1']
    rtn.quantity2 = request.POST['quantity2']
    rtn.price2_1 = request.POST['price2_1']
    rtn.price2_2 = request.POST['price2_2']
    rtn.quantity3 = request.POST['quantity3']
    rtn.quantity4 = request.POST['quantity4']
    rtn.amount1 = request.POST['amount1']
    rtn.amount2 = request.POST['amount2']
    rtn.sales_ex1 = request.POST['sales_ex1']
    rtn.sales_ex2 = request.POST['sales_ex2']
    rtn.job1 = request.POST['job1']
    rtn.job2 = request.POST['job2']
    rtn.labour_charge = request.POST['labour_charge']
    rtn.other_charge = request.POST['other_charge']
    rtn.total1 = request.POST['total1']
    rtn.total2 = request.POST['total2']
    rtn.total3 = request.POST['total3']
    rtn.total4 = request.POST['total4']
    rtn.total5 = request.POST['total5']
    rtn.total6 = request.POST['total6']
    rtn.discount = request.POST['discount']
    rtn.tax = request.POST['tax']
    rtn.save()
    return render(request, 'Sam/purchase.html')
def deletepsreturn(request, id):
    rtn = PRSales_Return.objects.get(id=id)
    rtn.delete()
    return render(request, 'Sam/purchase.html')


def gopreceipt(request):
    return render(request, 'Sam/purchase receipt.html')
def preceiptcreate(request):
    rpt2 = PReceipt(receipt_number=request.POST['receipt_number'], date=request.POST['date'], internal_ref_no=request.POST['internal_ref_no'],
    due_on=request.POST['due_on'], credit_limit_amt=request.POST['credit_limit_amt'], user_id=request.POST['user_id'],
    supp_id=request.POST['supp_id'], supp_name = request.POST['supp_name'],invoice_no1 = request.POST['invoice_no1'],
    invoice_no2 = request.POST['invoice_no2'],invoice_no3 = request.POST['invoice_no3'],invoice_date1 = request.POST['invoice_date1'],
    invoice_date2 = request.POST['invoice_date2'],invoice_date3 = request.POST['invoice_date3'],duedate1 = request.POST['duedate1'],
    duedate2 = request.POST['duedate2'],duedate3 = request.POST['duedate3'],invoice_amt1 = request.POST['invoice_amt1'],
    invoice_amt2 = request.POST['invoice_amt2'],invoice_amt3 = request.POST['invoice_amt3'],received_amt1 = request.POST['received_amt1'],
    received_amt2 = request.POST['received_amt2'],received_amt3 = request.POST['received_amt3'],outstanding1 = request.POST['outstanding1'],
    outstanding2 = request.POST['outstanding2'],outstanding3 = request.POST['outstanding3'],discount1 = request.POST['discount1'],discount2 = request.POST['discount2'],
    discount3 = request.POST['discount3'],balance_amt1 = request.POST['balance_amt1'],balance_amt2 = request.POST['balance_amt2'],balance_amt3 = request.POST['balance_amt3'],
    tick_space1 = request.POST['tick_space1'],tick_space2 = request.POST['tick_space2'],tick_space3 = request.POST['tick_space3'],partial1 = request.POST['partial1'],
    partial2 = request.POST['partial2'],partial3 = request.POST['partial3'],total1 = request.POST['total1'],total2 = request.POST['total2'],
    total3 = request.POST['total3'],total4 = request.POST['total4'],total5 = request.POST['total5'],total6 = request.POST['total6'],
    on_account = request.POST['on_account'],discount = request.POST['discount'],)
    rpt2.save()
    return redirect('/')


def preceiptview(request):
    rpt1 = PReceipt.objects.all()
    context = {'rpt': rpt1}
    return render(request,'Sam/show purchase receipt.html', context)
def editpreceipt(request,id):
    rpt1 = PReceipt.objects.get(id=id)
    context = {'rpt': rpt1}
    return render(request,'Sam/edit purchase receipt.html', context)
def updatepreceipt(request,id):
    rpt = PReceipt.objects.get(id=id)
    rpt.receipt_number=request.POST['receipt_number']
    rpt.date = request.POST['date']
    rpt.internal_ref_no = request.POST['internal_ref_no']
    rpt.due_on = request.POST['due_on']
    rpt.credit_limit_amt = request.POST['credit_limit_amt']
    rpt.user_id = request.POST['user_id']
    rpt.supp_id = request.POST['supp_id']
    rpt.supp_name = request.POST['supp_name']
    rpt.invoice_no1 = request.POST['invoice_no1']
    rpt.invoice_no2 = request.POST['invoice_no2']
    rpt.invoice_no3 = request.POST['invoice_no3']
    rpt.invoice_date1 = request.POST['invoice_date1']
    rpt.invoice_date2 = request.POST['invoice_date2']
    rpt.invoice_date3 = request.POST['invoice_date3']
    rpt.duedate1 = request.POST['duedate1']
    rpt.invoice_amt2 = request.POST['invoice_amt2']
    rpt.invoice_amt3 = request.POST['invoice_amt3']
    rpt.received_amt1 = request.POST['received_amt1']
    rpt.received_amt2 = request.POST['received_amt2']
    rpt.received_amt3 = request.POST['received_amt3']
    rpt.outstanding1 = request.POST['outstanding1']
    rpt.outstanding2 = request.POST['outstanding2']
    rpt.outstanding3 = request.POST['outstanding3']
    rpt.discount1 = request.POST['discount1']
    rpt.discount2 = request.POST['discount2']
    rpt.discount3 = request.POST['discount3']
    rpt.balance_amt1 = request.POST['balance_amt1']
    rpt.balance_amt2 = request.POST['balance_amt2']
    rpt.balance_amt3 = request.POST['balance_amt3']
    rpt.tick_space1 = request.POST['tick_space1']
    rpt.tick_space2 = request.POST['tick_space2']
    rpt.tick_space3 = request.POST['tick_space3']
    rpt.partial1 = request.POST['partial1']
    rpt.partial2 = request.POST['partial2']
    rpt.partial3 = request.POST['partial3']
    rpt.total1 = request.POST['total1']
    rpt.total2 = request.POST['total2']
    rpt.total3 = request.POST['total3']
    rpt.total4 = request.POST['total4']
    rpt.total5 = request.POST['total5']
    rpt.total6 = request.POST['total6']
    rpt.on_account = request.POST['on_account']
    rpt.discount = request.POST['discount']

    rpt.save()
    return render(request, 'Sam/purchase.html')
def deletepreceipt(request, id):
    rpt = PReceipt.objects.get(id=id)
    rpt.delete()
    return render(request, 'Sam/purchase.html')












