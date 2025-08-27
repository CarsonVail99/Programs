class Books:
    def __init__(self, title, author, pages,category):
        self._title = title
        self._author = author
        self._pages = pages
        self._category = category

    @property #property is a getter method so it doesnt return a memory address
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def pages(self):
        return self._pages

    @property
    def category(self):
        return self._category

    @title.setter
    def title(self, new_title): #helps change the value of the attribute with simple input = new_value
        self._title = new_title

    @author.setter
    def author(self, new_author):
        self._author = new_author

    @pages.setter
    def pages(self, new_pages):
        self._pages = new_pages

    @category.setter
    def category(self, new_category):
        self._category = new_category


    def __contains__(self, keyword):#__contains__ to check if keyword is in title
        return keyword.lower() in self._title.lower()#returns true or false

    #called via slicing
    def __getitem__(self, item):#__getitem__ returns item
        if isinstance (item, int):
            if item == 0:
                return self._title
            elif item == 1:
                return self._author
            elif item == 2:#How to slice a list via __getitem__
                return self._pages
            elif item == 3:
                return self._category
            else:
                print('Invalid index')
        return None

    #called upon print(book)
    def __str__(self):
        return f'{self._title} by {self._author}'


books = [

Books('The Unknown Universe', 'Someone', 341, 'Non-Fiction'),
Books('The Hunger Games', 'Suzanne Collins',486,'Fiction'),
Books('Pride and Prejudice', 'Jane Austen', 284, 'Historic Fiction'),
Books('How to kill a Mockingbird', 'Harper Lee', 679, 'Fiction'),
Books('Harry Potter', 'JRR Rowlings', 245, 'Fantasy'),
Books('The Book Thief', 'Markus Zusak', 444, 'Fiction'),
Books('The Hobbit', 'JRR Tolkien', 873, 'Fiction')
]


def save_data():
    with open('test.txt', 'w') as f:
        for book in books:
            f.write(f'Books({book.title}, {book.author}, {book.pages}, {book.category})\n')

def import_data():#Basically stripping the quotes, commas, Book Class, and slicing to make sure it's a valid book'
    with open('test.txt', 'r') as r:
        for line in r:
            line = line.strip()
            if line.startswith('Books(') and line.endswith(')'):#making sure it fits the format of a Book Class
                data = line[6:-1].split(', ')
                if len(data) == 4:
                    title = data[0].strip("'")
                    author = data[1].strip("'") #importing with txt is not fun, alot of parsing needed
                    pages = int(data[2].strip("'"))
                    category = data[3].strip("'")
                    if not any(book.title == title for book in books): #any yields true or false if condition is true
                        new_book = Books(title, author, pages, category)
                        books.append(new_book)



def menu():
    while True:
        print('----Welcome to the Book Manager----')
        print('1. Show all Books')
        print('2. Change title, author, pages and category of book')
        print('3. Check to see if a book is available')
        print('4. Search for a book by category')
        print('5. Search for a book by author')
        print('6. Search for a book by title')
        print('7. Add a new book')
        print('8. Save data to file')
        print('9. Import data from file')
        print('10. Exit')


        choice = input('Enter your choice: ')
        if choice == '1':
            for book in books:
                print(book)

        elif choice == '2': #setter method
            book_to_change = input('Enter title of book to change: ').capitalize()
            for book in books:
                if book.title.lower() == book_to_change.lower():
                    what_to_change = input('What do you want to change? (title, author, pages, category): ').lower()
                    if what_to_change.lower() == 'title':
                        new_title = input('Enter new title: ').capitalize()
                        book.title = new_title
                    elif what_to_change.lower() == 'author':
                        new_author = input('Enter new author: ').capitalize()
                        book.author = new_author
                    elif what_to_change.lower() == 'pages':
                        new_pages = input('Enter new pages: ')
                        book.pages = new_pages
                    elif what_to_change.lower() == 'category':
                        new_category = input('Enter new category: ').capitalize()
                        book.category = new_category
                    else:
                        print('Invalid choice')

        elif choice == '3':#__contains__method
            keyword = input('Search the title:')
            for book in books:
                if keyword in book:#use __contains__ with in
                    print(book)


        elif choice == '4':#__getitem__ method
            category = input('Enter a category:')
            for book in books:
                if book[3].lower() == category.lower(): #use __getitem__ with []
                    print(book)

        elif choice == '5':
            author = input('Enter an Author to search for:')
            for book in books:
                if book[1].lower() == author.lower():
                    print(book)

        elif choice == '6':
            title = input('Enter a title to search for:')
            for book in books:
                if book[0].lower() == title.lower():
                    print(book)

        elif choice == '7':
            while True:
                title = input('Enter title: ').capitalize()
                author = input('Enter author: ').capitalize()
                pages = int(input('Enter pages: '))
                category = input('Enter category: ').capitalize()
                book_counter = len(books)
                book_counter += 1
                book_counter = str(book_counter)
                book_counter = 'book' + book_counter
                book_counter = Books(title, author, pages, category)
                books.append(book_counter)
                print(f'Book {book_counter} added successfully')
                prompt = input('Do you want to add another book? (y/n) ')
                if prompt in ['y', 'yes']:
                    continue
                else:
                    break
        elif choice == '8':
            save_data()
            print('Data saved successfully')

        elif choice == '9':
            import_data()
            print('Data imported successfully')

        elif choice == '10':
            print('Exiting...')
            return False
        else:
            print('Invalid choice')


def main():
    menu()


if __name__ == '__main__':
    menu()


