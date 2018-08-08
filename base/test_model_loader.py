import unittest
import os
import model_loader


class TestModelLoader(unittest.TestCase):
    """Test cases for model loader"""
    def setUp(self):
        self.url = "https://github.com/anchen1011/mxnet-lambda/blob/master/docs/cat.png?raw=true"
        self.target = "./cat.png"

    def test_download_url_no_retry(self):
        model_loader.download_url(self.url, self.target, 1)
        os.remove(self.target)

    def test_download_url_no_retry(self):
        model_loader.download_url(self.url, self.target, 2)
        os.remove(self.target)


if __name__ == "__main__":
    unittest.main()
    