import sqlite3 as sql
def create_table():
    connection = sql.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read text)')
    connection.commit()
    connection.close()

def add_book(name,author):
    read = 'No'
    connection = sql.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books VALUES(?,?,?)', (name,author,read))
    connection.commit()
    connection.close()

def list_books():
    connection = sql.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    books = [{"name":row[0], "author":row[1], "read":row[2]} for row in cursor.fetchall()]
    connection.close()
    print(books)

def delete_book(name):
    connection = sql.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE name=?',(name,))
    connection.commit()
    connection.close()

def mark_as_read(name):
    connection = sql.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read="Yes" WHERE name=?',(name,))
    connection.commit()
    connection.close()


