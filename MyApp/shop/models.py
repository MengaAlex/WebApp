from django.db.models import Model, TextField, DateField, ImageField

class Product(Model):
    name = TextField()
    image = ImageField(upload_to='images')
    price = TextField()
    description = TextField()
    type = TextField()
    date = DateField()
    
    def __str__(self):
        return self.name