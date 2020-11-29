from app import create_app
import unittest

app = create_app()

class FlaskTeste(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_status_code_get_feira(self):
        tester = app.test_client(self)
        response = tester.get('/feira/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_content_type_Buscar_feira(self):
        tester = app.test_client(self)
        response = tester.get('/feira/')
        self.assertEqual(response.content_type, "application/json")

    def test_products(self):
        # get list of products
        rv, json = self.client.get('/api/v1/products/')
        self.assertTrue(rv.status_code == 200)
        self.assertTrue(json['products'] == [])

        # add a customer
        rv, json = self.client.post('/api/v1/products/',
                                    data={'name': 'prod1'})
        self.assertTrue(rv.status_code == 201)
        location = rv.headers['Location']
        rv, json = self.client.get(location)
        self.assertTrue(rv.status_code == 200)
        self.assertTrue(json['name'] == 'prod1')
        rv, json = self.client.get('/api/v1/products/')
        self.assertTrue(rv.status_code == 200)
        self.assertTrue(json['products'] == [location])

        # edit the customer
        rv, json = self.client.put(location, data={'name': 'product1'})
        self.assertTrue(rv.status_code == 200)
        rv, json = self.client.get(location)
        self.assertTrue(rv.status_code == 200)
        self.assertTrue(json['name'] == 'product1')





if __name__ == "__main__":
    unittest.main()