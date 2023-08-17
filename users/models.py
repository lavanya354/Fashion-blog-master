from django.db import models

# Create your models here.

from django.db import models

class Image(models.Model):
    IMAGE_TYPES = (
        ('kids', 'Kids'),
        ('men', 'Men'),
        ('women', 'Women'),
    )
    
    image_type = models.CharField(max_length=10, choices=IMAGE_TYPES)
    image_file = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255, blank=True)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='uploaded_images')
    def __str__(self):
        return self.description or str(self.image_file)
