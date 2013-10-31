from django.db import models
from urlparse import urlparse

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % self.name 

class Host(models.Model):
    url = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def get_host(self):
        url = urlparse(self.url)
        return '%s' % url.hostname

    def __unicode__(self):
        return self.get_host()

class Service(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    group = models.ForeignKey(Group)
    host = models.ForeignKey(Host)

    def __unicode__(self):
        return '%s' % self.name 

