import unittest
import model_service
import mxnet as mx
from PIL import Image


class TestModelService(unittest.TestCase):
    """Test cases for model_service"""
    def setUp(self):
        self.test_event = {"url": "https://github.com/anchen1011/mxnet-lambda/blob/master/docs/cat.png?raw=true"}
        img = Image.open('../docs/cat.png')
        img = img.resize((224, 224))
        img = mx.nd.array(img)
        img = img.transpose((2, 0, 1))
        img = img.expand_dims(axis=0)
        self.test_model_input = img
        self.test_model_output = 280
        self.test_response_body = '{"category": "n02123045 tabby, tabby cat"}'

    def test_preprocess(self):
        self.assertEqual(model_service.preprocess(self.test_event).shape, (1,3,224,224))

    def test_inference(self):
        self.assertEqual(model_service.inference(self.test_model_input), self.test_model_output)

    def test_postprocess(self):
        self.assertEqual(model_service.postprocess(self.test_model_output), self.test_response_body)


if __name__ == "__main__":
    unittest.main()
    