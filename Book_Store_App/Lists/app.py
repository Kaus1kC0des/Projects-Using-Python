MENU_INPUT = "\n Enter 'a' to add a book, 's' to search, 'l' to list, 'd' to delete, 'e' to exit: "

books = []

def add_book():
  name = input("Enter the name of the book: ")
  author = input("Enter the name of the author: ")
  read_input = input("Have you read the book? (Y/N): ")
  read = None
  if read_input.title() == "Y":
    read = True
  else:
    read = Fals
  book_dict = {
        'name': name,
        'author': author,
        'read' : read
    }
  books.append(book_dict)
  
def search_book():
  sbook = input("Enter the name of the book you want to search for: ")
  for book in books:
    if book["name"].title() == sbook.title():
      print(book)
      
    
  
  
