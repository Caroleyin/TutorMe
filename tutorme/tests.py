# Resources: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

from django.test import TestCase
from django.test.utils import setup_test_environment

from .models import AppUser
from .models import Course

# Create your tests here.

# Test 1: App User model
class AppUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        AppUser.objects.create(first_name = "fname", last_name = "lname")

    # label tests
    def test_first_name_label(self):
        user = AppUser.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        user = AppUser.objects.get(id=1)
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_is_student_label(self):
        user = AppUser.objects.get(id=1)
        field_label = user._meta.get_field('is_student').verbose_name
        self.assertEqual(field_label, 'is student')
    
    def test_is_tutor_label(self):
        user = AppUser.objects.get(id=1)
        field_label = user._meta.get_field('is_tutor').verbose_name
        self.assertEqual(field_label, 'is tutor')

    # max length tests
    def test_first_name_max_length(self):
        user = AppUser.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_last_name_max_length(self):
        user = AppUser.objects.get(id=1)
        max_length = user._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

# Test 2: Course Model
class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Course.objects.create(title = "something", subject = "CS")

    # label tests
    def test_title_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_subject_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('subject').verbose_name
        self.assertEqual(field_label, 'subject')

    def test_catalog_number_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('catalog_number').verbose_name
        self.assertEqual(field_label, 'catalog number')
    
    def test_course_id_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('course_id').verbose_name
        self.assertEqual(field_label, 'course id')

    def test_is_enrolled_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('is_enrolled').verbose_name
        self.assertEqual(field_label, 'is enrolled')

    def test_meeting_days_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('meeting_days').verbose_name
        self.assertEqual(field_label, 'meeting days')

    def test_start_time_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('start_time').verbose_name
        self.assertEqual(field_label, 'start time')

    def test_end_time_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('end_time').verbose_name
        self.assertEqual(field_label, 'end time')

    # max length tests
    def test_title_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_subject_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('subject').max_length
        self.assertEqual(max_length, 10)

    def test_catalog_number_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('catalog_number').max_length
        self.assertEqual(max_length, 10)

    def test_course_id_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('course_id').max_length
        self.assertEqual(max_length, 10)

    def test_meeting_days_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('meeting_days').max_length
        self.assertEqual(max_length, 10)

    def test_start_time_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('start_time').max_length
        self.assertEqual(max_length, 200)

    def test_end_time_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('end_time').max_length
        self.assertEqual(max_length, 200)



# Test 3: Selecting a CS 3240 adds it to the user's profile page

# Test 4: Forms, selecting student/tutor sets the boolean correctly

# Test 5: Test whether the entered time is correct or not

# 