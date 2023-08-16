from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .views import SignupPageView





class CustomUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username ='admin',
            email='ikehezechi@gmail.com',
            password='!Oneluv@123'
        )

        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.email, 'ikehezechi@gmail.com')
        self.assertEqual(user.is_active,True)
        self.assertEqual(user.is_staff,False)
        self.assertEqual(user.is_superuser,False)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@gmail.com',
            password='testpass123'
        )

        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@gmail.com')
        self.assertEqual(admin_user.is_active,True)
        self.assertEqual(admin_user.is_staff,True)
        self.assertEqual(admin_user.is_superuser,True)


class SignupTest(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    # Test for status code, template used, included and excluded test
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there!, I should not be on the page')


    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username,self.username)
        self.assertEqual(get_user_model().objects.all()[0].email,self.email)
        
        
        
        #Test when Django basic auth is used
        # Test to assert that CustomerUserCreationForm is used
        #form = self.response.context.get('form')
        #self.assertIsInstance(form, CustomUserCreationForm)
        #self.assertContains(self.response, 'csrfmiddlewaretoken')

    # Test to assert that page resolves to SignupPageView
    #def test_signup_view(self):
    #    view = resolve('/account/signup/')
    #    self.assertEqual(
    #        view.func.__name__,
    #        SignupPageView.as_view().__name__
    #    )
