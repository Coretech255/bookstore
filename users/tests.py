from django.contrib.auth import get_user_model
from django.test import TestCase



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

