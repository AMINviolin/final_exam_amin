from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Services(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']

class PortFolio(models.Model):
    image = models.ImageField(upload_to='port',default='default.jpg')
    title = models.CharField(max_length=40)
    ouner_name = models.CharField(max_length = 60,default = 'ouner')
    content = models.TextField(max_length=100)
    ouner_image = models.ImageField(upload_to='port',default='default.jpg')
    ouner_category = models.ManyToManyField(Category, related_name='portfolio_owner_category')
    description = models.TextField()
    category = models.ManyToManyField(Category, related_name='portfolio_category')
    client = models.TextField()
    project_date = models.DateTimeField(auto_now_add=True)
    project_url = models.URLField()
    subject = models.CharField(max_length=250,default='bigan')
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    
    def snip(self):
        return self.content[:15] + '...'
    
    def capt(self):
        return self.title.capitalize()