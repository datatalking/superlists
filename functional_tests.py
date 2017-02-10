from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):


	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online app. She goes
		# to edit its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention todo lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# git pull - ... pull the most current version written.
		# git status - ... gives me info with changes i'm committing
		# git commit -m "Comments" ... gives comments to my changes
		# git push ... send changes to repo
		# learn more forking
		# master

		# She is invited to enter a to-do item straight away
		# browser = webdriver.Firefox()

		# Edith has heard about a cool new online to-do app. she goes
		# to checkout its homepage
		# browser.get('http://localhost:8000')

		# She notice the page title and header mention to-do lists.
		# assert 'To-Do' in browser.title

		# She is invited to enter a to-do item right away

		# She types "Buy peacock feathers" into a text box (Edith's hobby
		# is tying fly fishing lures)

		# When she hits enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item on a to-do list

		# There is still a text box inviting her to add anothe item. She
		# enters "Use peacock feathers to make a fly" (Edith is very methodical)

		# The page updates again, and now shows both items on her list

		# Edit wonders wither the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect.

		# She visits that URL - her to-do list is still there

		# Satisfied she goes back to sleep

		if __name__ == '__main__':
			unittest.main(warning='ignore')



		browser.quit()


# http://www.obeythetestinggoat.com/book/chapter_04.html#RefactoringCat


# http://www.diveintopython.net
