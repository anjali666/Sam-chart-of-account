from django.shortcuts import render, redirect
from Sam.models import Customer, Expences, Income, Liabilities, Supplier, Group, Ledger, Item, Job, Asset
from .forms import ItemForm, JobForm


def go(request):
    return render(request,'Sam/dashboard.html')


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











