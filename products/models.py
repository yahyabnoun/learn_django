from django.db import models

class Product(models.Model):

    categoriesChoises = [
        ("phone","phone"),
        ("computer","computer"),
    ]

    name = models.CharField(max_length=150,verbose_name="title")
    content = models.TextField(null=True,blank=True,verbose_name="description")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='photo/%y/m/%d')
    active = models.BooleanField(default=True)
    categories = models.CharField(max_length=150, null=True, blank=True, choices=categoriesChoises)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Product"
        ordering = ["-name"]



class Video(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    


class User(models.Model):
    name = models.CharField(max_length=150)
    # products = models.ForeignKey(Product, on_delete=models.CASCADE) // one to many every user can have multi products
    videos = models.ManyToManyField(Video)
    def __str__(self):
        return self.name
