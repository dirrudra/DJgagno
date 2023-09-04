from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=200,default='Default Caption')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Images(models.Model):
    img_photo = models.ImageField(upload_to='images/',null=True, blank=True)

    def get_image(self):
        if self.img_photo and hasattr(self.img_photo, 'url'):
            return self.img_photo.url
        else:
            return '/path/to/default/image'

    def __str__(self):
        return self.img_photo