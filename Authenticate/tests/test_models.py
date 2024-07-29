from django.test import TestCase
from Authenticate.products import Products


class TestingModels(TestCase):
    
    def setUp(self) -> None:
        self.product_one = Products.objects.create(
            name="Iphone 14",
            brand="Apple",
            description="The iPhone 14 and iPhone 14 Plus feature a 6.1-inch (15 cm) and 6.7-inch (17 cm) display",
            price=2000000,
            quantity=1
        )

        #count all the values in the column name
        self.all_products = Products.objects.values_list("name").count()


    def test_is_intance(self):
        self.assertIsInstance(self.product_one, Products)


    def test_count_all_values_name(self):
        self.assertEquals(self.all_products, 1)


    def test_product_name(self):
        self.assertEquals(self.product_one.name, "Iphone 14")

    
    def test_product_price(self):
        self.assertLess(self.product_one.price, 5000000)

    
    def test_updaed_product_name(self):
        
        self.product_one.name = "redmi 12 pro"
        self.product_one.save()
        self.assertEquals(self.product_one.name, "redmi 12 pro")