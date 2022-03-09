from django.db import models

# Create your models here.
GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
)
class BMI_model(models.Model):
    name = models.CharField(max_length=50, null=True, blank= True)
    phone_number = models.IntegerField(default=0)
    email = models.EmailField(null=True, max_length=255)
    age = models.IntegerField()
    gender = models.IntegerField(choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='images/')
    bmi = models.TextField()
    fat = models.TextField()

    def delete(self,*args,**kwargs):
       self.image.delete()
       super().delete(*args,**kwargs)
