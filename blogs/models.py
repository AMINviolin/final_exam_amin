from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser




class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    

class Tags(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length= 255)
    content1 = models.TextField()
    content2 = models.TextField(null=True,blank=True)
    content3 = models.TextField(null=True,blank=True)
    content4 = models.TextField(null=True,blank=True)
    content5 = models.TextField(null=True,blank=True)
    endcontent = models.TextField()
    banner = models.TextField(max_length= 255)
    topic1 = models.TextField(max_length= 255)
    topic2 = models.TextField(null=True,blank=True)
    counted_views = models.IntegerField(default=0)
    counted_comment = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to= 'blog', default= 'default.jpg')
    second_image = models.ImageField(upload_to = 'blog', default= 'blog-2.jpg')
    author = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    auther_img = models.ImageField(upload_to= 'blog', default="bauth.jpg")
    auther_bio = models.TextField(null=True,blank=True)
    twitter = models.CharField(max_length=255,default='twitter.com')
    facebook = models.CharField(max_length=255,default='facebook.com')
    instagram = models.CharField(max_length=255,default='instagram.com')
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tags)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title



    class Meta:
        ordering = ('-created_date',)



class Comments(models.Model):
    which_post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='post')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self):
        return self.name
    


class Replay(models.Model):
    which_comment = models.ForeignKey(Comments, on_delete=models.CASCADE,related_name='comments')
    message = models.TextField()
    status= models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self):
        return str(self.which_comment)
