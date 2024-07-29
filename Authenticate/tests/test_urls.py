from django.test import TestCase, Client
from django.urls import reverse, resolve
from Authenticate.views import logout_user, home


class TestingUrls(TestCase):

    def setUp(self) -> None:

        self.client = Client()
        self.url = reverse("logout")
        self.response_one = reverse("products")
        self.redirect = self.client.get(self.response_one)
        self.response = resolve(self.url)


    def test_url_logout(self):
        self.assertEquals(self.response.func, logout_user, 
                        msg="verify if the url is associated to the 'logout_user' function view.")
        
    
    def test_url_not_associated(self):
        self.assertNotEquals(self.response.func, home, 
                        msg="verify if the url is associated to the 'home' view function.")