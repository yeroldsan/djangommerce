from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from .models import Category, Item

class CategoryModelTest(TestCase):
  def setUp(self):
    '''
    Test the creation of a new category
    '''
    Category.objects.create(name="Test Category")

  def test_category_str(self):
    category = Category.objects.get(name="Test Category")
    self.assertEqual(str(category), "Test Category")

class ItemModelTest(TestCase):
  def setUp(self):
    user = User.objects.create_user(username="testuser", password="testpass")
    category = Category.objects.create(name="Test Category")
    Item.objects.create(
      category=category,
      name="Test Item",
      description="Test description",
      price=50.00,
      status=Item.AVAILABLE,
      created_by=user,
  )

  def test_item_str(self):
    item = Item.objects.get(name="Test Item")
    self.assertEqual(str(item), "Test Item")

  def test_item_status_choices(self):
    item = Item.objects.get(name="Test Item")
    self.assertEqual(item.status, Item.AVAILABLE)
