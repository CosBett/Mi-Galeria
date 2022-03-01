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
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)        

class Test_Image(TestCase):
    def setUp(self):
        self.location = Location(name='Moyale')
        self.location.save_location()
        self.category = Category(name='Nature')
        self.category.save_category()
        self.image_test = Image(id=1, name='image', description='this is a test image', location=self.location,
                                category=self.category)   

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'pictures/test.png')
        changed_img = Image.objects.filter(image='pictures/test.png')
        self.assertTrue(len(changed_img) > 0)

    def test_get_image_by_id(self):
        found_image = self.image_test.get_image_by_id(self.image_test.id)
        image = Image.objects.filter(id=self.image_test.id)
        self.assertTrue(found_image, image) 

    def test_search_image_by_category(self):
        category = 'Nature'
        found_img = self.image_test.search_by_category(category)
        self.assertTrue(len(found_img) > 1)

    def test_filter_image_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_location(location='Moyale')
        self.assertTrue(len(found_images) == 1) 

    def test_filter_image_by_category(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_category(category='Nature')
        self.assertTrue(len(found_images) == 1)        

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()    