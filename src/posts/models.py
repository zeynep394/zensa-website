from django.db import models
from django.urls import reverse
from tinymce import HTMLField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    content = HTMLField()
    f_price = models.FloatField(default=0)
    l_price = models.FloatField(default=0)
    thumbnail = models.ImageField()
    deneme_resim= models.ImageField(blank=True)
    deneme_resim2= models.ImageField(blank=True)
    deneme_resim3= models.ImageField(blank=True)

#Bunları anasayfadaki çok satan vs kısmındaki ürünleri ayırmak için kullanıyoruz
#admin kısmında ürün eklerken hangi kutucuğu işaretlersek orada görünür
#yani anasayfada çok satanlar kısmında gözükmesini ve akıl oyunları içinde yer almasını istiyorsan 
# akıl oyunları kutucuğunu ve çok satanlar kutucuğunu işaretler
    enyeniler = models.BooleanField()
    coksatanlar= models.BooleanField()
    ahsap = models.BooleanField()
    boyalar = models.BooleanField()

    ahsap_obje=models.BooleanField()
    boya=models.BooleanField()
    akıl_oyunları=models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
    })
