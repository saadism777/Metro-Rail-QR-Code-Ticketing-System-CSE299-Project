from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from accounts.utils import unique_order_id_generator
from django.db.models.signals import pre_save
# Create your models here.
class User(AbstractUser):
    is_guser = models.BooleanField(default=False)
    is_trainmaster = models.BooleanField(default=False)

class GeneralUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=300)
    location = models.CharField(max_length=500)
    email = models.EmailField(max_length=200)

    def __str__(self):
           return self.user.username


class TrainMaster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    location = models.CharField(max_length=500)
    licenseNumber = models.CharField(max_length=200)
    def __str__(self):
           return self.user.username


class Route(models.Model):
    routeId= models.AutoField(primary_key=True)
    source = models.CharField(max_length=200)
    dest = models.CharField(max_length=200)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return self.dest
class Book(models.Model):
    BOOKED = 'Booked'
    CANCELLED = 'Cancelled'
    CONFIRMED = 'Confirmed'
    PAID = 'Paid'
    NOT_PAID = 'Not_Paid'
    REFUNDED = 'Refunded'


    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),
                       (CONFIRMED,'Confirmed'))
    PAYMENT_STATUSES =((PAID, 'Paid'),
                       (NOT_PAID ,'Not_Paid'),
                       (REFUNDED , 'Refunded'))
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    routeid = models.IntegerField()
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=15)
    payment_status = models.CharField(choices= PAYMENT_STATUSES, default=NOT_PAID, max_length=30)
    date = models.DateField()
    time = models.TimeField()
    order_id = models.CharField(max_length=120, blank=True)
    code = models.ImageField(blank=True, upload_to='code')
    is_paid = models.BooleanField(default=False, blank=True)
    is_refunded = models.BooleanField(default=False, blank=True)
    @property
    def imageURL(self):
        """
        This Function is to fetch the respective product image without gettting an error
        :param: self
        :return: url 
        """
        try:
            url = self.code.url
        except:
            url = ''
        return url

    

    def save(self, *args, **kwargs):
        self.order_id = unique_order_id_generator(self)
        qr_image = qrcode.make(self.order_id)
        qr_offset = Image.new('RGB', (310,310), 'white')
        qr_offset.paste(qr_image)
        files_name = f'{self.username}-{self.order_id}qr.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.code.save(files_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)

pre_save.connect(pre_save_create_order_id, sender = Book)

# class Ticket(models.Model):
#     name = models.CharField(max_length=100)
#     code = models.ImageField(blank=True, upload_to='code')




#     @property
#     def imageURL(self):
#         """
#         This Function is to fetch the respective product image without gettting an error
#         :param: self
#         :return: url 
#         """
#         try:
#             url = self.code.url
#         except:
#             url = ''
#         return url

#     def __str__(self) -> str:
#         return self.name

#     def save(self, *args, **kwargs):
#         qr_image = qrcode.make(self.name)
#         qr_offset = Image.new('RGB', (310,310), 'white')
#         qr_offset.paste(qr_image)
#         files_name = f'{self.name}-{self.id}qr.png'
#         stream = BytesIO()
#         qr_offset.save(stream, 'PNG')
#         self.code.save(files_name, File(stream), save=False)
#         qr_offset.close()
#         super().save(*args, **kwargs)