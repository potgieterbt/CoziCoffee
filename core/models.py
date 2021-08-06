from django.db import models


MYUSER = get_user_model()
# Create your models here.

# class Item(models.Model):
#     title = models.CharField(max_length=35)
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     code = models.IntegerField(max_length=15, unique=True, primary_key=True)
#     milk = models.BooleanField()
#     discounted_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

class Cart(models.Model):
    cart_id = models.CharField(max_length=80)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Discount, on_delete=models.SET_NULL, blank=True, null=True)
    price_ht = models.DecimalField(max_digits=5, decimal_places=2)
    price_ttc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(default=1, validators=[validators.quantity_validator])
    anonymous = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)
    objects = models.Manager()
    cart_manager = managers.CartManager.as_manager()
    statistics = managers.CartsStatisticsManager.as_manager()

    class Meta:
        ordering = ['-created_on', '-pk']
        indexes = [
            models.Index(fields=['price_ht', 'quantity']),
        ]

    def __str__(self):
        return self.cart_id

    def clean(self):
        if self.price_ht > 0:
            self.price_ttc = utilities\
                    .calculate_tva(self.price_ht, tva=20)

class Review(models.Model):
    user = models.ForeignKey(MYUSER, blank=True, null=True, on_delete=models.SET_NULL)
    customer_order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE ,blank=True, null=True)
    rating = models.IntegerField(default=1)
    text = models.TextField(max_length=300)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_order

class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=280, blank=True, null=True)
    price_ht = models.DecimalField(max_digits=5, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_valid_until = models.DateField(default=utilities.add_to_current_date(d=30))
    slug = models.SlugField()
    objects = models.Manager()
    product_manager = managers.ProductManager.as_manager()

    class Meta:
        ordering = ['-created_on', '-pk']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name
        
        if self.name:
            new_slug = utilities.create_product_slug(self.name)
            self.slug = new_slug

    def get_absolute_url(self):
        collection_name = self.collection.name.lower()
        return reverse('product', args=[self.pk, self.slug])