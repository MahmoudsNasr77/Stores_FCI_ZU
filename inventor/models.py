from django.db import models
from django.utils import timezone
class items(models.Model):
    name=models.CharField(max_length=500,verbose_name="اسم المنتج")
    quntity=models.IntegerField(verbose_name="الكميه ")
    exporter=models.CharField(max_length=1000,verbose_name="المورد ")
    data=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'المنتجات'
        verbose_name_plural = 'المنتجات'
    def __str__(self) -> str:
        return self.name
class paydata(models.Model):
    payer_name=models.CharField(max_length=5000,verbose_name="اسم المستلم")
    quntity=models.IntegerField(verbose_name="الكميه")
    items=models.ForeignKey(items,on_delete=models.PROTECT,verbose_name="المنتج")
    exporter=models.CharField(max_length=5000,verbose_name="اسم المسلم")
    data=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'الاذونات'
        verbose_name_plural = 'الاذونات'
    def __str__(self) -> str:
        return self.items
class invntor(models.Model):
    items=models.ForeignKey(items,on_delete=models.PROTECT,verbose_name="المنتج")
    quntity=models.IntegerField(verbose_name="الكميه المنصرفه")
    importer=models.CharField(max_length=500,verbose_name="المنصرف له")
    data=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'المخزن'
        verbose_name_plural = 'المخزن'
    def __str__(self) -> str:
        return self.importer
    def save(self, *args, **kwargs):
        # Decrease the quantity of the book when it is borrowed
        if self.items.quntity> 0:
            self.items.quntity -= self.quntity
            self.items.save()
            super().save(*args, **kwargs)
        
       



