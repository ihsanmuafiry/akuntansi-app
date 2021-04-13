from django.forms import ModelForm
from .models import Transaksi

class TransaksiForm(ModelForm):
    class Meta:
        model = Transaksi
        fields = ['nomorDokumen','desc','akun','tipeAkun','price']

