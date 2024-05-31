from django.test import TestCase
from .models import Category, Recipe
from django.utils import timezone

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Test Category')

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Test Category')
        Recipe.objects.create(
            title='Test Recipe',
            description='Test description',
            instructions='Test instructions',
            ingredients='Test ingredients',
            created_at=timezone.now(),
            updated_at=timezone.now(),
            category=category
        )

    def test_title_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_instructions_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('instructions').verbose_name
        self.assertEqual(field_label, 'instructions')

    def test_ingredients_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('ingredients').verbose_name
        self.assertEqual(field_label, 'ingredients')

    def test_category_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_created_at_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label, 'created at')

    def test_updated_at_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('updated_at').verbose_name
        self.assertEqual(field_label, 'updated at')

    def test_title_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    # Додайте інші тести для перевірки максимальної довжини, наявності категорії і т. д.


