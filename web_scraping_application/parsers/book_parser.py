from bs4 import BeautifulSoup
import re

from locators.book_locators import BookLocators

class BookParser:
    RATINGS = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    def __init__(self,page):
        self.soup = page


    @property
    def name(self):
        locator = BookLocators.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = BookLocators.LINK_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['href']
        return item_name

    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.soup.select_one(locator)
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern,item_price.string)
        return float(matcher.group(1))

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        item_rating = self.soup.select_one(locator)
        classes = item_rating.attrs['class']
        rating_classes = [r for r in classes if r!='star-rating']
        return BookParser.RATINGS.get(rating_classes[0],"No Ratings")

    def __repr__(self):
        return f"<{self.name}, £{self.price}, {self.rating} stars>"





