from distutils.command.upload import upload
from multiprocessing import set_forkserver_preload
from unicodedata import category
from django.db import models
from django.forms import ImageField

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
  image = ImageField(upload_to = 'pictures/')
  name = models.CharField(max_lenght= 50)
  description = models.CharField(max_length=500)
  location = models.ForeignKey(Location,on_delete=models.CASCADE)
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  
