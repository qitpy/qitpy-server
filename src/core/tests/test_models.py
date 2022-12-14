# '''
# Test for models
# '''
# from django.test import TestCase
# from django.contrib.auth import get_user_model

# from core import models
# from unittest.mock import patch


# def create_user(email='user@example.com', name='user name'):
#     '''create and return a new user'''
#     return get_user_model().objects.create_user(token_jwt)


# class ModelTests(TestCase):
#     '''Test models'''

#     def test_create_user_successful(self):
#         '''test creating a user with an email is successful'''
#         email = 'test@example.com'
#         name = 'TestName'
#         password = 'TestPass123'

#         user = get_user_model().objects.create_user(
#             email, name, password,
#         )
#         self.assertEqual(user.email, email)
#         self.assertEqual(user.name, name)
#         self.assertTrue(user.check_password(password))

#     def test_new_user_email_normalized(self):
#         '''Test email is normalized for new users'''
#         sample_emails = [
#             ['Test1@Example.com', 'Test1@example.com'],
#             ['test2@Example.com', 'test2@example.com'],
#             ['TEST3@ExaMple.com', 'TEST3@example.com'],
#             ['TEST4@EXAMPLE.COM', 'TEST4@example.com'],
#         ]

#         for email, expected in sample_emails:
#             user = create_user(email=email)
#             self.assertEqual(user.email, expected)

#     def test_new_user_without_require_field_raises_error(self):
#         '''test that creating a user without an email raises a ValueError'''
#         with self.assertRaises(ValueError):
#             create_user(email='')

#         with self.assertRaises(ValueError):
#             create_user(name='')

#     def test_new_user_with_low_password_security(self):
#         '''tests new user with the security of password is low'''
#         with self.assertRaises(ValueError):
#             create_user(password='12345678')
#         with self.assertRaises(ValueError):
#             create_user(password='1234abcd')
#         with self.assertRaises(ValueError):
#             create_user(password='abc')
#         with self.assertRaises(ValueError):
#             create_user(password='password123')
#         with self.assertRaises(ValueError):
#             create_user(password='abcdefGGGG')
#         with self.assertRaises(ValueError):
#             create_user(password='1234567GG')

#         good_password = 'normalPW123'
#         user = create_user(password=good_password)
#         self.assertTrue(user.check_password(good_password))

#     def test_create_superuser(self):
#         """Test creating a superuser"""
#         user = get_user_model().objects.create_superuser(
#             email='super@example.com',
#             name='super',
#             password='PassWord123'
#         )

#         self.assertTrue(user.is_superuser)

#     def test_new_user_must_be_activate(self):
#         '''test create new user must be enable by email'''
#         user = create_user(email='active@example.com')

#         self.assertTrue(user.is_active, False)
#         self.assertIsNotNone(user.verify_email_code)
