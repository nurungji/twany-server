from selenium import webdriver
import unittest

class FunctionalTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_before_starting_project(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('test', self.browser.title)
        self.fail('Finish the test!')
if __name__ == '__main__':
    unittest.main(warnings='ignore')
