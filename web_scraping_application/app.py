import requests
from pages.all_books_page import *

page_content = requests.get('http://books.toscrape.com').content

page = AllBooksPage(page_content)

books = page.books
#for book in books:
    #print(book)