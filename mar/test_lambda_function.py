from __future__ import print_function

import unittest
import os
from lambda_function import Context, BaseResponse, download_url, get_model_archive, get_inference_hanlder


class TestLambdaFunction(unittest.TestCase):
    """Test cases for lambda_function"""
    def setUp(self):
        self.test_context = Context(lambda : print, lambda : print, None, None, None)
        self.test_response_1 = BaseResponse("test base response")
        self.test_response_2 = BaseResponse("test base response")
        self.test_response_3 = BaseResponse("test base response")
        self.test_response_4 = BaseResponse("test base response")
        self.test_url = "https://github.com/anchen1011/mxnet-lambda/blob/master/docs/cat.png?raw=true"
        self.test_target = "./cat.png"
        self.test_trigger_dir = os.getcwd()

    def test_get_dict(self):
        self.assertEqual(self.test_response_1.get_dict(), {"headers":{}, "body":"test base response", "statusCode":200})

    def test_add_response_property(self):
        self.test_response_2.add_response_property("content-type", "image/png")
        self.assertEqual(self.test_response_2.get_dict(), {"headers":{"content-type": "image/png"}, "body":"test base response", "statusCode":200})

    def test_set_response_status(self):
        self.test_response_3.set_response_status(404)
        self.assertEqual(self.test_response_3.get_dict(), {"headers":{}, "body":"test base response", "statusCode":404})
       
    def test_set_response_body(self):
        self.test_response_4.set_response_body("")
        self.assertEqual(self.test_response_4.get_dict(), {"headers":{}, "body":"", "statusCode":200})
    
    def test_download_url_no_retry(self):
        download_url(self.test_url, self.test_target, 1)
        os.remove(self.test_target)

    def test_download_url_no_retry(self):
        download_url(self.test_url, self.test_target, 2)
        os.remove(self.test_target)

    def test_get_model_archive(self):
        trigger_dir = get_model_archive()
        self.assertEqual(trigger_dir, self.test_trigger_dir)
        os.chdir(trigger_dir)


if __name__ == "__main__":
    unittest.main()
    