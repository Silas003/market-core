from django.db import models
from django.contrib.auth.models import User
import uuid

class Category(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        ordering=('name',)
        verbose_name_plural='Categories'
    def __str__(self):
        return self.name
    

class Item(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    category=models.ForeignKey(Category,related_name='items',on_delete=models.PROTECT)
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='items/',null=True,blank=True)
    is_sold=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name='items',on_delete=models.PROTECT)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    