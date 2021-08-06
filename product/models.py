from django.db import models

# Create your models here.
STATUS = (
    (0,"Not Redeemed"),
    (1,"Redeemed")
)

class Location(models.Model):
    
    name = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=220, null=True)
    rating = models.IntegerField(blank=True, null=True)
    reviews = models.IntegerField(blank=True, null=True) 
    icon = models.FileField(upload_to='icons/%Y/%m/%d/', blank=True, null=True)


    def __str__(self):
        return str(self.location) if self.location else ''


class Offer(models.Model):


    title = models.CharField(max_length=120)
    sponsor_name = models.CharField(max_length=120)
    sponsor_logo = models.FileField(upload_to='logos/sponsor_logo/%Y/%m/%d/', null=True)
    description = models.TextField()
    location = models.ManyToManyField(Location, blank=True)
    image = models.ImageField(upload_to='images/{self.title}/', null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    redeem_status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['title','sponsor_name']

    def __str__(self):
        return str(self.title)


class Redemption(models.Model):

    offer_title = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='offer_redemption')
    barcode_number = models.IntegerField()
    coupon_image = models.ImageField(upload_to='coupons/%Y/%m/%d/', null=True)
    qrcode_string = models.CharField(max_length=250, null=True)
    sms_number = models.IntegerField(blank=True, null=True)
    keyword = models.CharField(max_length=12, null=True)
    terms_n_conditions = models.CharField(max_length=560, null=True)

    class Meta:
        ordering = ['offer_title']

    def __str__(self):
        return self.offer_title
