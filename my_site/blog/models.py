from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_address=models.EmailField(max_length=100)

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullname()



class Tag(models.Model):
    caption=models.CharField(max_length=50)


    def __str__(self):
        return f"{self.caption}"



class Post(models.Model):
    title=models.CharField(max_length=100)
    excerpt=models.CharField(max_length=200)
    image_name=models.CharField(max_length=80)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True,db_index=True)
    content=models.TextField(validators=[MaxLengthValidator(1500)])
    author=models.ForeignKey(Author, null=True,on_delete=models.CASCADE,related_name="post")
    tags=models.ManyToManyField(Tag)


    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        return super().save(*args,**kwargs)


    def __str__(self):
        return f"{self.title}"
    






