from django.db import models
from  django.contrib.auth.models import User
# Create your models here.

class Categorya(models.Model):
    name=models.CharField(max_length=120)

    class Meta:
        db_table='category'


    def __str__(self):
        return self.name

class News(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Categorya,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    image=models.ImageField(upload_to='news/',default='default/news.jpg',blank=True,null=True)
    desc=models.TextField()
    created_at=models.DateField(auto_now_add=True)


    class Meta:
        ordering=['-created_at']
        db_table='news'

    def __str__(self):
        return self.title



class Coment(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    pos_text=models.TextField(blank=True,null=True)
    neg_text=models.TextField(blank=True,null=True)
    text=models.TextField()
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    rate=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering=['-created_at']
        db_table='coments'

    def __str__(self):
        return self.news.title

class Contact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    email=models.EmailField()
    info=models.CharField(max_length=120,blank=True,null=True)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=['-created_at']
        db_table='contacts'
    def __str__(self):
        return self.name


class Saved(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)



    class Meta:
        db_table='Save'



