
from django.db.models import Model, ImageField
from django.db.models.fields import CharField, TimeField, DecimalField



class Tct(Model):
    name = CharField(max_length=255)
    mentor = CharField(max_length=255)
    room = CharField(max_length=255)
    time = TimeField()
    price = DecimalField(max_digits=10, decimal_places=2)
    image = ImageField(upload_to='products/')

    def __str__(self):
        return self.name


