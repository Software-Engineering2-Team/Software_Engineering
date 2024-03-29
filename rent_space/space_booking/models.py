from django.db import models
from rent_space.user_management.models import User


class AdSpace(models.Model):
    location = models.CharField(max_length=100)
    size = models.FloatField()
    price = models.FloatField()
    availability = models.BooleanField()
    photos = models.ImageField(upload_to='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='spaces_owned')

    def checkAvailability(self):
        pass

    def updateAvailability(self):
        pass


class Booking(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    adSpace = models.ForeignKey(AdSpace, on_delete=models.CASCADE)
    bookingDate = models.DateTimeField()
    status = models.BooleanField()

    def makePayment(self):
        pass

    def issueRefund(self):
        pass

    def updateStatus(self):
        pass


class Rating(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    adSpace = models.ForeignKey(AdSpace, on_delete=models.CASCADE)
    score = models.FloatField()
    comment = models.TextField()

    def updateScore(self):
        pass

    def updateComment(self):
        pass


class Payment(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField
    paymentStatus = models.BooleanField()
    spaceOwnerId = models.ForeignKey(User, on_delete=models.CASCADE)

    def processPayment(self):
        pass

    def validatePayment(self):
        pass
