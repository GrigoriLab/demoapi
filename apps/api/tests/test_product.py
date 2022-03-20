from apps.api.tests.base import BaseTestCase


class ProductTestCase(BaseTestCase):
    fixtures = [
        "store/initial_data.json",
    ]

    def test_products(self):
        self.api_client.login("grigori", "grigori")
        resp = self.api_client.get("products/")
        expected_product = {
            "id": 1,
            "name": "Test product",
            "price": 99.0,
            "description": "test product description",
            "created_at": "2022-03-20T10:58:46.806000Z"
        }
        self.assertDictEqual(expected_product, resp.json[0])

    def test_products_unauthorized(self):
        resp = self.api_client.get("products/")
        self.assertEqual(resp.status_code, 401)
        resp = self.api_client.post("products/", data={})
        self.assertEqual(resp.status_code, 401)
