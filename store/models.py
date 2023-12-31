from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        get_user_model(), null=True, blank=True, on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    profile_image = models.ImageField(null=True, blank=True, default="default.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.email


class Categorie(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    colors = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.colors


class Size(models.Model):
    sizes = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.sizes


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Categorie, on_delete=models.PROTECT, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    colors = models.ManyToManyField(Color, blank=True)
    sizes = models.ManyToManyField(Size, blank=True)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.name

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True
    )
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=False, null=True)
    transaction_id = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    state = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        ordering = ("-date_ordered",)

    def __str__(self):
        return str(self.customer)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    size = models.CharField(max_length=20, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_ordered",)

    def __str__(self):
        return str(self.product)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddres(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True
    )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=50, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
