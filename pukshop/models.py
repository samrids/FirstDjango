from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=00.00)
    image = models.ImageField(upload_to="gallery", null=True, blank=True)
    for_sale = models.BooleanField(null=False, default=False)
    release_date = models.DateField(null=False, auto_now_add=True)
    sys_created_date = models.DateTimeField(auto_now_add=True, null=False)

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title
