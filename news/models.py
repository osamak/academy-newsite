from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    body = models.TextField()
    image = models.FileField(upload_to="post_images")
    pub_date = models.DateTimeField(auto_now_add=True)

    def has_image(self):
        if self.image == "":
            return False
        else:
            return True

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=128)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Comment by %s on post %s" % (self.author,
                                             self.post.title)
