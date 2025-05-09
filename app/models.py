from itertools import product
from multiprocessing.spawn import old_main_modules
from statistics import quantiles
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.validators import MaxLengthValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.validators import MaxLengthValidator, MinValueValidator

STATE_CHOICE = (
    ('London', 'London'),
    ('Paris', 'Paris'),
    ('Rome', 'Rome'),
    ('Berlin', 'Berlin'),
    ('Madrid', 'Madrid'),
    ('Amsterdam', 'Amsterdam'),
    ('Vienna', 'Vienna'),
    ('Prague', 'Prague'),
    ('Budapest', 'Budapest'),
    ('Barcelona', 'Barcelona'),
    ('Lisbon', 'Lisbon'),
    ('Dublin', 'Dublin'),
    ('Athens', 'Athens'),
    ('Copenhagen', 'Copenhagen'),
    ('Stockholm', 'Stockholm'),
    ('Oslo', 'Oslo'),
    ('Brussels', 'Brussels'),
    ('Helsinki', 'Helsinki'),
    ('Warsaw', 'Warsaw'),
    ('Zurich', 'Zurich'),
    ('Munich', 'Munich'),
    ('Milan', 'Milan'),
    ('Frankfurt', 'Frankfurt'),
    ('Edinburgh', 'Edinburgh'),
    ('Nice', 'Nice'),
    ('Florence', 'Florence'),
    ('Krakow', 'Krakow'),
    ('Porto', 'Porto'),
    ('Geneva', 'Geneva'),
    ('Naples', 'Naples'),
    ('Seville', 'Seville'),
    ('Lyon', 'Lyon'),
    ('Cologne', 'Cologne'),
    ('Valencia', 'Valencia'),
    ('Bratislava', 'Bratislava'),
    ('Riga', 'Riga'),
    ('Tallinn', 'Tallinn'),
    ('Vilnius', 'Vilnius'),
    ('Luxembourg', 'Luxembourg'),
    ('Ljubljana', 'Ljubljana'),
    ('Reykjavik', 'Reykjavik'),
    ('Bucharest', 'Bucharest'),
    ('Sofia', 'Sofia'),
    ('Belgrade', 'Belgrade'),
    ('Zagreb', 'Zagreb'),
    ('Sarajevo', 'Sarajevo'),
    ('Skopje', 'Skopje'),
    ('Tirana', 'Tirana'),
    ('Podgorica', 'Podgorica'),
    ('Chisinau', 'Chisinau'),
    ('San Marino', 'San Marino'),
    ('Monaco', 'Monaco'),
    ('Andorra la Vella', 'Andorra la Vella'),
    ('Valletta', 'Valletta'),
    ('Nicosia', 'Nicosia'),
    ('The Hague', 'The Hague'),
    ('Rotterdam', 'Rotterdam'),
    ('Antwerp', 'Antwerp'),
    ('Ghent', 'Ghent'),
    ('Hamburg', 'Hamburg'),
    ('Düsseldorf', 'Düsseldorf'),
    ('Bordeaux', 'Bordeaux'),
    ('Turin', 'Turin'),
    ('Bologna', 'Bologna'),
    ('Palermo', 'Palermo'),
    ('Verona', 'Verona'),
    ('Leeds', 'Leeds'),
    ('Manchester', 'Manchester'),
    ('Birmingham', 'Birmingham'),
    ('Liverpool', 'Liverpool'),
    ('Sheffield', 'Sheffield'),
    ('Newcastle', 'Newcastle'),
    ('Glasgow', 'Glasgow'),
    ('Stuttgart', 'Stuttgart'),
    ('Dresden', 'Dresden'),
    ('Nuremberg', 'Nuremberg'),
    ('Innsbruck', 'Innsbruck'),
    ('Salzburg', 'Salzburg'),
    ('Graz', 'Graz'),
    ('Basel', 'Basel'),
    ('Lucerne', 'Lucerne'),
    ('Lausanne', 'Lausanne'),
    ('Bern', 'Bern'),
    ('Cannes', 'Cannes'),
    ('Toulouse', 'Toulouse'),
    ('Marseille', 'Marseille'),
    ('Malaga', 'Malaga'),
    ('Alicante', 'Alicante'),
    ('Granada', 'Granada'),
    ('Cordoba', 'Cordoba'),
    ('Bilbao', 'Bilbao'),
    ('San Sebastian', 'San Sebastian'),
    ('Lille', 'Lille'),
    ('Strasbourg', 'Strasbourg'),
    ('Utrecht', 'Utrecht'),
    ('Eindhoven', 'Eindhoven'),
    ('Brno', 'Brno'),
    ('Wroclaw', 'Wroclaw'),
    ('Gdansk', 'Gdansk'),
)


class Customer(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=90)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=80)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ('Mobile', 'MEN WEAR'),
    ('Laptop', 'WOMAN WEAR'),
    ('ElectronicAccessories', 'Accessories'),
    # ('BW', 'Bottom Wear'),
)

class Brand(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    def __str__(self):
        return (self.name)
    
# class Category(models.Model):
#     category = models.CharField(choices=CATEGORY_CHOICES, max_length=30)
    
#     def __str__(self):
#         return (self.category)

class Product(models.Model):
    title = models.CharField(max_length=50)
    selling_price = models.FloatField()
    discounted_prie = models.FloatField()
    short_description = HTMLField(max_length=110)
    description = HTMLField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30)
    product_image = models.ImageField(upload_to='productimg', null=False , blank=False)

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def totalCost(self):
        return self.quantity * self.product.discounted_prie


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=60, choices=STATUS_CHOICES, default='Pending')

    @property
    def totalCost(self):
        return self.quantity * self.product.discounted_prie


# Create your models here.
class Verification(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	token = models.CharField(max_length=150)
	verify = models.BooleanField(default=False)
    