from multiprocessing import set_forkserver_preload
from django.db import models

class Location(models.Model):
  name = models.CharField(max_lenght= 50)

  def save_location(self):
    self.save()

  def update_location(self, name):
    self.name = name
    self.save()

  def delete_location(self):
    self.delete()  

class Category(models.Model):
  name = models.CharField(max_lenght= 50)
  
  def save_category(self):
    self.save()

  def update_category(self, name):
    self.name = name
    self.save()

  def delete_category(self):
    self.delete()  
class Image(models.Model):
  name = models.CharField(max_lenght= 50)
