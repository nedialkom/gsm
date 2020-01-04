from django.db import models

# Create your models here.
class Rating(models.Model):
    ratingName = models.CharField(max_length=12)

    def __str__(self):
        return self.ratingName

class Phone (models.Model):
    phoneHash = models.CharField(max_length=13)
    rating = models.ForeignKey(Rating, on_delete=models.PROTECT, default=3)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'Phone No. {} with {} rating'.format(self.phoneHash, self.rating)