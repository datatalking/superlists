from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title


# http://www.obeythetestinggoat.com/book/chapter_04.html#RefactoringCat


# http://www.diveintopython.net
