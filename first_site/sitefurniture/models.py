from time import time

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return str(new_slug) + '-' + str(int(time()))


class ProductPhoto(models.Model):
    url = models.CharField(max_length=150)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return '{}'.format(self.url)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.url)
        super().save(*args, **kwargs)

#https://images.ua.prom.st/1043446275_w640_h640_stul-s14-ekokozha.jpg
#https://images.ua.prom.st/1043445148_w640_h640_stul-s14-ekokozha.jpg
#https://images.ua.prom.st/1043445094_w640_h640_stul-s14-ekokozha.jpg
#https://images.ua.prom.st/1043445144_w640_h640_stul-s14-ekokozha.jpg


#https://images.ua.prom.st/2160393609_w640_h640_kreslo-myagkoe-dlya.jpg
#https://images.ua.prom.st/2160394530_w640_h640_kreslo-myagkoe-dlya.jpg
#https://images.ua.prom.st/2160393403_w640_h640_kreslo-myagkoe-dlya.jpg
#https://images.ua.prom.st/2160393208_w640_h640_kreslo-myagkoe-dlya.jpg

#https://images.ua.prom.st/2072959352_w640_h640_stul-nik-eames.jpg
#https://images.ua.prom.st/2072959353_w640_h640_stul-nik-eames.jpg

#https://images.ua.prom.st/2023973796_w640_h640_stol-knizhka-matroluxe.jpg
#https://images.ua.prom.st/1589304368_w640_h640_stol-knizhka-matroluxe.jpg
#https://images.ua.prom.st/2023973797_w640_h640_stol-knizhka-matroluxe.jpg
#https://images.ua.prom.st/2023973798_w640_h640_stol-knizhka-matroluxe.jpg

#https://images.ua.prom.st/1645822119_w640_h640_stil-transformer-alfa.jpg
#https://images.ua.prom.st/1645822120_w640_h640_stil-transformer-alfa.jpg
#https://images.ua.prom.st/782153706_w640_h640_stil-transformer-alfa.jpg
#https://images.ua.prom.st/413118025_w640_h640_stil-transformer-alfa.jpg

#https://images.ua.prom.st/1312043396_w640_h640_stol-raskladnoj-seattle.jpg
#https://images.ua.prom.st/1259441745_w640_h640_stol-raskladnoj-seattle.jpg
#https://images.ua.prom.st/1259441748_w640_h640_stol-raskladnoj-seattle.jpg
#

class Product(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)
    description = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    types = models.ManyToManyField('TypeFurniture', blank=True, related_name='products')
    photos = models.ManyToManyField('ProductPhoto', blank=True, related_name='products')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        print(reverse('product_detail_url', kwargs={'slug': self.slug}))
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']


class TypeFurniture(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        print("---***---", reverse('type_detail_url', kwargs={'slug': self.slug}))
        return reverse('type_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['title']

# class Cart(models.Model):
#    pass


# class Client(models.Model):
#    pass


# class CartProduct():
#    pass


########## **** shell
# >>> pp=ProductPhoto(url="url5")
# >>> pp.save()
# >>> pps=ProductPhoto.objects.all()
# >>> pps
# <QuerySet [<ProductPhoto: url1>, <ProductPhoto: url2>, <ProductPhoto: url3>, <ProductPhoto: url4>, <ProductPhoto: url5>]>
# >>> pr = Product(title = "Chair", description = "Perfect chair")
# >>> pr.save
# <bound method Product.save of <Product: Chair>>
# >>> pr.save()
# >>> pr.types.add(tf)
# >>> pr.save()
# >>> pr.types
# <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x10c184828>
# >>> pr.types.all()
# <QuerySet [<TypeFurniture: Bedroom>]>
# pp1 = ProductPhoto.objects.get(url="url2")
# >>> pp1
