from django.db import models

class invntor(models.Model):
    name=models.CharField(max_length=500,verbose_name="اسم المنتج")
    quntity=models.IntegerField(verbose_name="الكميه المنصرفه")
    importer=models.CharField(max_length=500,verbose_name="المنصرف له")
    data=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'المخزن'
        verbose_name_plural = 'المخزن'

class items(models.Model):
    name=models.CharField(max_length=500,verbose_name="اسم المنتج")
    quntity=models.IntegerField(verbose_name="الكميه ")
    exporter=models.CharField(max_length=1000,verbose_name="المورد ")
    class Meta:
        verbose_name = 'المنتجات'
        verbose_name_plural = 'المنتجات'
