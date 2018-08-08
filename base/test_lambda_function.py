import unittest
from lambda_function import BaseResponse


class TestLambdaFunction(unittest.TestCase):
	"""Test cases for lambda_function"""
    def setUp(self):
        self.test_response = BaseResponse("test response body")
        self.test_response_dict = {"headers":{"content-type": "application/json", "Access-Control-Allow-Origin": "*"}, "body":"test response body", "statusCode":200}

    def test_get_dict(self):
        self.assertEqual(self.test_response.get_dict(), self.test_response_dict)


if __name__ == "__main__":
    unittest.main()
