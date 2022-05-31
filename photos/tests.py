from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Image, Location, Category

class ImageTestClass(TestCase):

  def setUp(self):
    self.category = Category(cat_name='food')
    self.category.save()

    self.location = Location(city='nairobi', country='kenya', locale='westlands')
    self.location.save()

    self.image1 = Image(photo='test.jpg', img_name='test trip', description='short trip to jamaica', location=self.location, category=self.category)
    self.image1.save()
  
  def test_instance(self):
    self.assertTrue(isinstance(self.image1, Image))

  def test_save(self):
    self.image1.save_image()
  
  def test_get_img_by_id(self):
    img = Image.get_image_by_id(self.image1.pk)
    self.assertEqual(img, self.image1)
  
  def test_search(self):
    img_cat = Image.search_cat('food')
    self.assertIn(self.image1, img_cat)
    
  def test_delete_image(self):
    image2 = Image(photo='test_2.jpg', img_name='test 2 trip', description='short trip to hawaii', location=self.location, category=self.category)
    image2.save_image()
    image2.delete_image()
    result=Image.get_image_by_id(pk=image2.id)
    self.assertEqual(result,"Image does not exist")
  
  def test_update_image(self):
    new_img = 'photo2.jpg'
    Image.update_image(self.image1.id,new_img)
    updated_img = Image.get_image_by_id(self.image1.id)
    self.assertEqual(updated_img.photo,"photo2.jpg")
  
  class CategoryTestClass(TestCase):

    def setUp(self):
      self.category2 = Category(cat_name='Travel')




      

   
  

    