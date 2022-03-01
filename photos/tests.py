from unicodedata import category
from django.test import TestCase
from .models import Location, Category, Image

class Test_Location(TestCase):
    def setUp(self):
        self.location = Location(name='Kericho')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))      
    
    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_update_location(self):
        new_location = 'Kabianga'
        self.location.update_location(self.location.id, new_location)
        changed_location = Location.objects.filter(name='Kabianga')
        self.assertTrue(len(changed_location) > 0)      

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)
class Test_Category(TestCase):
    def setUp(self):
        self.category = Category(name='Fashion')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))      
    
    def test_save_category(self):
        self.category.save_category()
        category = Category.get_category()
        self.assertTrue(len(category) > 0)

    def test_update_category(self):
        new_category = 'textile'
        self.category.update_category(self.category.id, new_category)
        changed_category = Category.objects.filter(name='textile')
        self.assertTrue(len(changed_category) > 0)      

    def test_delete_category(self):
        self.location.delete_category()
        location = Category.objects.all()
        self.assertTrue(len(category) == 0)        
