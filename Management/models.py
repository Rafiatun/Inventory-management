from django.db import models

# Create your models here.

class Vendor(models.Model):
    full_name=models.CharField(max_length=100 ,null=True , blank=True)
    photo=models.ImageField(upload_to="vendor/")
    address=models.TextField()
    phone_number=models.CharField(max_length=12)
    status=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='1. Vendor'

    def __str__(self):
        return self.full_name

class Unit(models.Model):
    title=models.CharField(max_length=100 ,null=True , blank=True)
    short_name=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='2. Unit '
   

    def __str__(self):
        return self.title


class Product(models.Model):
    title=models.CharField(max_length=100 ,null=True , blank=True)
    details=models.TextField()
    unit=models.ForeignKey(Unit, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="product/")

    class Meta:
        verbose_name_plural='3. Product'

    def __str__(self):
        return self.title


class Purchase(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    quantity=models.FloatField()
    price=models.FloatField()
    total_amount=models.FloatField(editable=False,default=0)
    purchase_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='4. Purchase'

    def save(self,*args,**kwargs):
        self.total_amount =self.quantity * self.price
        super(Purchase,self).save(*args,**kwargs)
        #inventory

        inventory=Inventory.objects.filter(product=self.product).order_by('-id').first()
        if inventory:
            totalBalance= inventory.total_balanced_quantity + self.quantity
        else:
            totalBalance=self.quantity

        Inventory.objects.create(
            product=self.product,
            purchase=self,
            sale=None,
            purchase_quantity=self.quantity,
            sale_quantity=None,
            total_balanced_quantity=totalBalance

        )


 

class Sale(models.Model):
    product=models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity=models.FloatField()
    price=models.FloatField()
    total_amount=models.FloatField(editable=False,)
    sale_date=models.DateTimeField(auto_now_add=True)
    customer_name=models.CharField(max_length=100,null=True)
    customer_phn=models.CharField(max_length=12,null=True)


    class Meta:
        verbose_name_plural='5. Sale'


    def save(self,*args,**kwargs):
        self.total_amount =self.quantity * self.price
        super(Sale,self).save(*args,**kwargs)
        #inventory

        inventory=Inventory.objects.filter(product=self.product).order_by('-id').first()
        if inventory:
            totalBalance= inventory.total_balanced_quantity - self.quantity
  

        Inventory.objects.create(
            product=self.product,
            purchase=None,
            sale=self,
            purchase_quantity=None,
            sale_quantity=self.quantity,
            total_balanced_quantity=totalBalance

        )


class Inventory(models.Model):
    product=models.ForeignKey(Product , on_delete=models.CASCADE)
    purchase=models.ForeignKey(Purchase,on_delete=models.CASCADE , default=0,null=True)
    sale=models.ForeignKey(Sale,on_delete=models.CASCADE,default=0,null=True)
    purchase_quantity=models.FloatField(default=0,null=True)
    sale_quantity=models.FloatField(default=0,null=True)
    total_balanced_quantity=models.FloatField()

    

    class Meta:
        verbose_name_plural='6. Inventory'

    def purchase_product_unit(self):
        return self.product.unit.title



    def purchase_date(self):
        if self.purchase:
            return self.purchase.purchase_date

    def sale_date(self):
        if self.sale:
            return self.sale.sale_date



