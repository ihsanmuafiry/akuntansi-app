from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404






# Create your views here.

def home(request):
    cabangs = Cabang.objects.all()

    context={
        'cabangs':cabangs
    }
    return render(request,'akuntabelapp/home.html',context)


def addBranch(request):

    if request.method == 'POST':
        nama = request.POST.get('nama','')

        cabang = Cabang(namaCabang=nama)
        cabang.save()
        return  redirect('/')

    context={

    }
    return render(request,'akuntabelapp/tambahcabang.html',context)

def branch(request,pk):

    cabang = Cabang.objects.get(id=pk)
    trans = Transaksi.objects.all()

    #get last id of db to get the length of db
    temp0 = Transaksi.objects.filter(desc__isnull=False).values_list('id',flat=True)
    ntrans = temp0.count()

    for i in range(ntrans): #needs improvement on account +/- attachement
        val =temp0[i]
        temp = Transaksi.objects.get(id=val)
        if temp.tipeAkun == "Debit": #bug here, reversed settings
            if temp.akun.coaAwal == "1":
                temp.saldoCredit1 = temp.price
                temp.saldoDebit1 = 0
        elif temp.tipeAkun == "Credit":
            if temp.akun.coaAwal == "1":
                temp.saldoDebit1 = temp.price*-1
                temp.saldoCredit1 = 0

        temp.save()
        print(type(temp.price))





    # akun = Akun.objects.all()
    # aklen = len(akun) - 1
    # ak = akun[aklen].namaAkun
    #
    # for i in range(translen):
    #     if trans[i].akun == ak[j].namaAkun:
    #         print('hello')


    # # orders = customer.order_set.all()
    # order_count = orders.count()

    # myFilter = OrderFilter(request.GET, queryset=orders)
    # orders = myFilter.qs

    context={
        'cabang':cabang,'trans':trans
             }
    return render(request,'akuntabelapp/cabang.html',context)




def account(request):
    akuns = Akun.objects.all()

    context={
        'akuns':akuns
    }
    return render(request,'akuntabelapp/akun.html',context)

def addAccount(request):

    if request.method == 'POST':
        nama = request.POST.get('namaAkun', '')
        coaAwal = request.POST.get('coaAkun', '')[0]
        # request.POST.get('coaAwal', '')
        coa = request.POST.get('coaAkun', '')[1:]
        namafull = coaAwal + '-' + coa + ' ' +nama
        coatemp = int(coaAwal)
        if type(coatemp) == int:
            akunT = Akun(namaAkun=namafull, coaAwal=coaAwal, coaAkun=coa)
            akunT.save()
            return redirect('/akun/')
        else:
            return HttpResponse('<h3>Pastikan kode dan nama akun sudah benar</h3>')
    context = {

    }
    return render(request,'akuntabelapp/tambahakun.html',context)

class updateAccount(UpdateView):
    model = Akun
    template_name = 'akuntabelapp/editakun.html'
    context_object_name = 'akun'
    fields = ('__all__')
    success_url = reverse_lazy('account')

class deleteAccount(DeleteView):
    model = Akun
    template_name = 'akuntabelapp/deleteakun.html'
    context_object_name = 'akun'
    fields = ('__all__')
    success_url = reverse_lazy('account')

@csrf_protect
def addTrans(request, pk):
    nAkun1 = 2
    # nAkun = int(request.GET.get('nAkun'))
    #
    # print('nagak',nAkun)
    # print(type(nAkun))


    TransFormSet = inlineformset_factory(Cabang, Transaksi, fields=('nomorDokumen','desc','akun','tipeAkun','price'),can_delete=False,extra=nAkun1)
    cabang = Cabang.objects.get(id=pk)
    if request.method =="POST":
        formset = TransFormSet(request.POST, instance=cabang)


        if formset.is_valid():
            formset.save()
        return redirect('/cabang/'+pk)
    formset = TransFormSet()

    context = {
        'formset':formset, 'cabang':cabang
    }
    return render(request, 'akuntabelapp/tambahtrans.html', context)


class updateTrans(UpdateView):
    model = Transaksi
    template_name = 'akuntabelapp/edittrans.html'
    context_object_name = 'trans'
    fields = ('__all__')
    success_url = reverse_lazy('home')

class deleteTrans(DeleteView):
    model = Transaksi
    template_name = 'akuntabelapp/deletetrans.html'
    context_object_name = 'trans'
    fields = ('__all__')
    success_url = reverse_lazy('home')