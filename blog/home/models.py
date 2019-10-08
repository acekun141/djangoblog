from django.db import models
import uuid
# Create your models here.
class Post(models.Model):
    uuid = str(uuid.uuid4())
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title