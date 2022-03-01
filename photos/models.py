
from django.db import models
from django.forms import ImageField

class Location(models.Model):
  name = models.CharField(max_length=60)
  def __str__(self):
        return self.name

  def save_location(self):
    self.save()

  def update_location(self, name):
    self.name = name
    self.save()

  def delete_location(self):
    self.delete()  

class Category(models.Model):
  name = models.CharField(max_length=60)
  
  def __str__(self):
        return self.name

  def save_category(self):
    self.save()

  def delete_category(self):
    self.delete()  
    
class Image(models.Model):
  image = models.ImageField(upload_to='pictures',blank=True)
  name = models.CharField(max_length=80)
  description = models.TextField(max_length=1500)
  location = models.ForeignKey(Location,on_delete=models.CASCADE)
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  
 
  @classmethod
  def get_image_by_id(cls,id):
    images_results = cls.objects.filter(id = id).all()
    return images_results

  @classmethod
  def search_image(cls,search_term):
    categoryImg_results = cls.objects.filter(category__name= search_term)
    return categoryImg_results
  
  @classmethod
  def filter_by_location(cls, location):
    locationImg_results = cls.objects.filter(location__name= location).all()
    return locationImg_results

  @classmethod
  def filter_by_category(cls, category):
    categoryImg_results = cls.objects.filter(category__name= category).all()
    return categoryImg_results

  @classmethod
  def search_by_category(cls, category):
    images = cls.objects.filter(category__name__icontains=category)
    return images
  
  def __str__(self):
      return self.name

  def save_image(self):
    self.save()


  def delete_image(self):
    self.delete() 
  
  def update_image(self, name,image, description,location,category):
    self.name = name
    self.image = image
    self.description = description
    self.location = location
    self.category = category

    self.save()

 
  
