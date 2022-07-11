from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from BPapp.models import *
from frontapp.models import signp, lo, cart, order, ordercart,chkp,checkoutm
from django.contrib import messages


from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def home(request):
    data = cat.objects.all()
    if 'signo' in request.session:
        c_user = request.session['signo']
        param = {'c_user': c_user}
        return render(request, 'home.html', param)
    else:
        return render(request, 'home.html', {'data': data})


def log(request):
    return render(request, "login.html")


def sign(request):
    return render(request, "signup.html")


def signpost(request):
    if request.method == 'POST':
        sin = request.POST.get('signname')
        sie = request.POST.get('signemail')
        sip = request.POST.get('signpass')
        signo = signp(signname=sin, signemail=sie, signpass=sip)
        signo.save()
        messages.success(request, 'Registration Successfull!')
    return redirect(sign)


def login(request):
    if request.method == 'POST':
        signname = request.POST.get('signname')
        signpass = request.POST.get('signpass')
        if signp.objects.filter(signname=signname, signpass=signpass).exists():
            data = signp.objects.filter(signname=signname, signpass=signpass).values('signname', 'signemail'
                                                                                     ).first()
            request.session['signname'] = data['signname']
            request.session['signpass'] = signpass
            request.session['signemail'] = data['signemail']
            return redirect('frontend')
        else:
            from django.http import HttpResponse
            return HttpResponse('invalid email or password')
    return render(request, 'login.html')


def logout(request):
    del request.session['signname']
    del request.session['signpass']
    del request.session['signemail']
    return redirect('log')


def booking(request):
    if 'signname' in request.session.keys():
        co = request.session.get('signname')
        cartob = cart.objects.filter(signname=co)
        c = cart.objects.filter(signname=co).count()
        facetotal = cart.objects.filter(signname=co).aggregate(Sum('cprice'))
        mtotal = cart.objects.filter(signname=co).aggregate(Sum('mprice'))
        htotal = cart.objects.filter(signname=co).aggregate(Sum('hprice'))
        fs = facetotal['fprice__sum']
        ms = mtotal['mprice__sum']
        hs = htotal['hprice__sum']
        fservices = face.objects.all()
        mservices = makeup.objects.all()
        hservices = hair.objects.all()
        user = signp.objects.get(signname=co)
        return render(request, 'cart.html', {'cartob': cartob, 'fs': fs, 'ms': ms, 'hs': hs, 'c ': c, 'fservices': fservices, 'hservices': hservices, 'mservices': mservices, 'user': user})


def frontend(request):
    c = cat.objects.all()
    data = {'cat': c}
    return render(request, "home.html", data)


def servicedis(request):
    s = cat.objects.all()
    fdata = {'cat': s}
    return render(request, "services.html", fdata)


def homedis(request):
    return render(request, "home.html")


def facecare(request):
    return render(request, "facecares.html")


def staffdis(request):
    name = request.session['signname']
    email = request.session['signemail']
    user = signp.objects.get(signname=name, signemail=email)
    print(user)
    products = cart.objects.filter(userid=user).count()
    x = staff.objects.all()
    xdata = {'staff': x, 'products': products}
    return render(request, "staff.html", xdata)


def facedisp(request):
    name = request.session['signname']
    email = request.session['signemail']
    user = signp.objects.get(signname=name, signemail=email)
    print(user)
    products = cart.objects.filter(userid=user).count()
    face = cat.objects.get(sname='Facial Care')
    o = Product.objects.filter(category=face)
    odata = {'face': o, 'products': products}
    return render(request, "facecares.html", odata)


def haircare(request):
    return render(request, "haircares.html")


def hairdisp(request):
    name = request.session['signname']
    email = request.session['signemail']
    user = signp.objects.get(signname=name, signemail=email)
    print(user)
    products = cart.objects.filter(userid=user).count()
    face = cat.objects.get(sname='Hair Care')
    h = Product.objects.filter(category=face)
    hdata = {'hair': h, 'products': products}
    return render(request, "haircares.html", hdata)


def make(request):
    return render(request, "makeup.html")


def makeupdisp(request):
    name = request.session['signname']
    email = request.session['signemail']
    user = signp.objects.get(signname=name, signemail=email)
    print(user)
    products = cart.objects.filter(userid=user).count()
    face = cat.objects.get(sname='Makeup Services')
    m = Product.objects.filter(category=face)
    mdata = {'makeup': m, 'products': products}
    return render(request, "makeup.html", mdata)


def branchs(request):
    return render(request, "branches.html")


def branchd(request):
    name = request.session['signname']
    email = request.session['signemail']
    user = signp.objects.get(signname=name, signemail=email)
    print(user)
    products = cart.objects.filter(userid=user).count()
    i = branch.objects.all()
    bdata = {'branch': i, 'products': products}
    return render(request, "branches.html", bdata)


def pass_reset(request):
    return render(request, "password.html")


# new
def addCart(request, pk):
    try:
        name = request.session['signname']
        email = request.session['signemail']
        user = signp.objects.get(signname=name, signemail=email)
    except:
        user = None

    product = Product.objects.get(id=pk)
    c = cart.objects.create(itemid=product, userid=user)
    c.save()
    print(c)
    return redirect('cart')


def cartMain(request):
    name = request.session['signname']
    email = request.session['signemail']
    user = signp.objects.get(signname=name, signemail=email)
    print(user)
    products = cart.objects.filter(userid=user)
    total = 0
    for p in products:
        total = total+p.itemid.price
    context = {'products': products, 'total': total}
    return render(request, 'cartMain.html', context)


def deletecart(request, pk):
    c = cart.objects.get(id=pk)
    c.delete()
    return redirect('cart')

def check(request):
    return render(request, "checkout.html")

def checkout(request):
    name = request.session['signname']
    email = request.session['signemail']
    user = signp.objects.get(signname=name, signemail=email)
    print(user)
    products = cart.objects.filter(userid=user)
    total = 0
    for p in products:
        total = total+p.itemid.price
    context = {'products': products, 'total': total}
    return render(request, 'checkout.html', context)

def checkoutpost(request):
    if request.method == 'POST':
        cn = request.POST.get('firstname')
        ce = request.POST['email']
        ca = request.POST['address']
        cc = request.POST['city']
        ccard = request.POST['cardname']
        cnum = request.POST['cardnumber']
        cm = request.POST['expmonth']
        cy = request.POST['expyear']
        cv = request.POST['cvv']
        cp = checkoutm(firstname=cn, email=ce, address=ca, city=cc, cardname=ccard, cardnumber=cnum, expmonth=cm, expyear=cy, cvv=cv)
        cp.save()
        messages.success(request, 'Payment Done successfully.')
    return redirect(cartMain)

def chk(request):
    name = request.session['signname']
    email = request.session['signemail']
    user = signp.objects.get(signname=name, signemail=email)
    print(user)
    products = cart.objects.filter(userid=user).count()
    i = branch.objects.all()
    bdata = {'branch': i, 'products': products}
    return render(request, "check.html", bdata)

def chkpost(request):
    if request.method == 'POST':
        f = request.POST.get('fname')
        l = request.POST['lname']
        obj = chkp(fname=f, lname=l)
        obj.save()
    return redirect(chk)

