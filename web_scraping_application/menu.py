from app import books


USER_CHOICES = """Select any one of the following:
- 'b' to look at 5-star books
- 'c' to look at cheapest books
- 'n' to just get the next available book on the page
- 'q' to exit the application
Your Choice: """

def menu():
    USER_INPUT = input(USER_CHOICES)
    while USER_INPUT.title() != 'Q':
        if USER_INPUT.title() == 'B':
            best_books()
        elif USER_INPUT.title() == 'C':
            cheapest_books()
        elif USER_INPUT.title() == 'N':
            next_book()
        else:
            print("Kindly enter a valid input.")
        USER_INPUT = input(USER_CHOICES)


def best_books():
    bbooks = sorted(books,key=lambda x : x.rating * -1)[:10]
    for boosk in bbooks:
        print(boosk)

def cheapest_books():
    cbooks = sorted(books,key=lambda x:x.price)[:10]
    for cbook in cbooks:
        print(cbook)

book_generator = (x for x in books)
def next_book():
    print(next(book_generator))

menu()