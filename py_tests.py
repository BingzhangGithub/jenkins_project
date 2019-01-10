import unittest, time
from selenium import webdriver


class TestClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
        self.base_url = "http://www.testclass.net"

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_case(self):
        self.driver.get(self.base_url)
        print(self.driver.title)

    def test_case2(self):
        self.driver.get(self.base_url)
        print(self.driver.get_cookies())


if __name__ == '__main__':
    unittest.main()