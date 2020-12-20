# functional_tests.py -

import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.b = webdriver.Firefox()

    def tearDown(self):
        self.b.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User checks out the new to-do app's homepage
        self.b.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.b.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box

        # When she hits enter, the page updates, and now the page lists "1: Buy peacock
        # feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. She enters "Use
        # peacock feathers to make a fly"

        # The page updates again, and now shows both items in her list

        # The user sees that the site has generated a unique URL for her, there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there

if __name__ == '__main__':
    unittest.main()
