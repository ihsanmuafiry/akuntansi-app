from django.db import models

# Create your models here.
class Cabang(models.Model):
    namaCabang = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.namaCabang


class Akun(models.Model):

    def __str__(self):
        return self.namaAkun

    namaAkun = models.CharField(max_length=200, null=True)
    coaAwal = models.CharField(max_length=200,null=True)
    coaAkun = models.CharField(max_length=200, null=True)


class Transaksi(models.Model):
    def __str__(self):
        return self.desc

    TIPE = (
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),)
    cabang = models.ForeignKey(Cabang, null=True, on_delete=models.SET_NULL)
    nomorDokumen = models.CharField(max_length=200, null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)
    desc = models.CharField(max_length=400, null=True)

    akun = models.ForeignKey(Akun, null=True, on_delete=models.SET_NULL)
    tipeAkun = models.CharField(max_length=200, choices=TIPE, null=True)
    price = models.FloatField(max_length=100, default=0)

    saldoCredit1 = models.FloatField(max_length=100, default=0)
    saldoDebit1 = models.FloatField(max_length=100, default=0)

    saldoCredit2 = models.FloatField(max_length=100, default=0)
    saldoDebit2 = models.FloatField(max_length=100, default=0)

    saldoCredit3 = models.FloatField(max_length=100, default=0)
    saldoDebit3 = models.FloatField(max_length=100, default=0)

    saldoCredit4 = models.FloatField(max_length=100, default=0)
    saldoDebit4 = models.FloatField(max_length=100, default=0)

    saldoCredit5 = models.FloatField(max_length=100, default=0)
    saldoDebit5 = models.FloatField(max_length=100, default=0)

    saldoCredit6 = models.FloatField(max_length=100, default=0)
    saldoDebit6 = models.FloatField(max_length=100, default=0)

    saldoCredit7 = models.FloatField(max_length=100, default=0)
    saldoDebit7 = models.FloatField(max_length=100, default=0)

    saldoCredit8 = models.FloatField(max_length=100, default=0)
    saldoDebit8 = models.FloatField(max_length=100, default=0)

    saldoCredit9 = models.FloatField(max_length=100, default=0)
    saldoDebit9 = models.FloatField(max_length=100, default=0)











