from django.test import TestCase, Client
from django.urls import reverse


class TestViewHome(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("home")
        self.url_register = reverse("register")
        self.url_login = reverse("login")
        self.response = self.client.get(self.url)
        self.response_login = self.client.get(self.url_login)
        self.response_register = self.client.get(self.url_register)


    def test_home_view_returns_200_ok(self):
        self.assertEquals(self.response.status_code, 200, msg="the view 'home' have to returns a 200 status code.")
    

    def test_view_home_fail(self):
        self.assertNotEquals(self.response.status_code, 404, msg="the view 'home' do not returns a 404 status code.")


    def test_template_associated_to_url_pass(self):
        #testing the template associated to the url
        self.assertTemplateUsed(self.response, "home.html")

    
    def test_template_not_associated_to_url_fail(self):
        self.assertTemplateNotUsed(self.response, "products.html")


    def test_context_template_register(self):
        #testing the context inside the template register.
        self.assertIn("form", self.response_register.context)