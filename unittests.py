from unittest import TestCase


class TestHttpRequests_Get(TestCase):
    def setUp(self):
            from HTTPRequests import HttpGet
            self.inst = HttpGet()
    def test_get_request(self):
            object = self.inst.get_request().status_code
            self.assertEqual(object,200)
    def test_get_with_querystring(self):
            status_code = self.inst.get_request_querystring().status_code
            self.assertEqual(status_code,200)
    def test_get_with_custom_headers(self):
            status_code = self.inst.get_request_headers().status_code
            self.assertEqual(status_code, 200)


