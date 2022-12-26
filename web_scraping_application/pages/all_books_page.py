import re

from locators.all_books_page import AllBooksPageLocators
from parsers.book_parser import BookParser
from bs4 import BeautifulSoup

class AllBooksPage:
    def __init__(self,page_content):
        self.soup = BeautifulSoup(page_content,'html.parser')

    @property
    def books(self):
        bset = set(BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS))
        #return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]
        return bset