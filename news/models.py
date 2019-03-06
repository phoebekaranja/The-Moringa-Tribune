from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
#......
import datetime as dt



# class Editor(models.Model):
#     first_name=models.CharField(max_length =30)
#     last_name=models.CharField(max_length =30)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length = 10,blank =True)
#
#     def save_editor(self):
#         self.save()
#
#     def __str__(self):
#         return self.first_name
class Meta:
        ordering = ['first_name']

# try:
#     editor = Editor.objects.get(email = 'example@gmail.com')
#     print('Editor found')
# except DoesNotExist:
#     print('Editor was not found')
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
class Article(models.Model):
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
    title = models.CharField(max_length =60)
    post = HTMLField()
    editor = models.ForeignKey(User,on_delete = models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/',blank=True)
    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
