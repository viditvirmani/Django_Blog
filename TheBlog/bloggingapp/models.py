''' My MODELS WILL BE
    1) User  ( Name ,  )
    2) Post (Fields Required = Name,DateCreated,Having text field for blogpost content)
        Fields :- author, Text,Title,created_date,published date
        Methods :- publish the post,
    3) Comments ( having text field for commenting on a blog )
    4)
    models.Model
'''
from django.db import models
from django.utils import timezone
'''TIMEZONE UTILITY FOR POSTS '''

class Post(models.Model):
      author = models.ForeignKey('auth.user',on_delete = models.CASCADE)
      text = models.TextField()
      title = models.CharField(max_length=70)
      created_date = models.DateTimeField(default=timezone.now())
      published_date = models.DateTimeField()
      '''Methods '''
      '''when post is published it should save the updates done (used save() method)'''
      def publish(self):
          self.published_date = timezone.now()
          self.save()
      def __str__(self):
          '''Just to represent the POST class string representation i.e the TITLE OF THE POST'''
          return self.title
