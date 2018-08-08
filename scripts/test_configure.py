import unittest
import os
import shutil
from configure import do_install, download_url, check_existence


class TestLambdaFunction(unittest.TestCase):
    """Test cases for configure"""
    def setUp(self):
        self.test_url = "https://github.com/anchen1011/mxnet-lambda/blob/master/docs/cat.png?raw=true"
        self.test_target = "./cat.png"

    def test_download_url_no_retry(self):
        download_url(self.test_url, self.test_target, 1)
        os.remove(self.test_target)

    def test_download_url_no_retry(self):
        download_url(self.test_url, self.test_target, 2)
        os.remove(self.test_target)

    def test_do_install_package(self):
        os.mkdir("tmp1")
        do_install("tqdm", False, "tmp1/")
        shutil.rmtree("tmp1")

    def test_do_install_requirements(self):
        os.mkdir("tmp2")
        do_install("../base/requirements.txt", True, "tmp2")
        shutil.rmtree("tmp2")

    def test_check_existence_file(self):
        self.assertEqual(check_existence('configure.py', './'), True)

    def test_check_existence_dir(self):
        self.assertEqual(check_existence('scripts', '../'), True)

    def test_check_existence_none(self):
        self.assertEqual(check_existence('aAjsdJAN', './'), False)


if __name__ == "__main__":
    unittest.main()
    