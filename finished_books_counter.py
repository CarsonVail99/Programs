def book_save(**kwargs):
    with open('books_read.txt', 'a') as f:
        for key, value in kwargs.items():
            f.write(f'{key} : {value}\n')

def ask_book():
    book_collection = {}
    book_finished = 1
    while True:           #               Key                            Value
        book_collection[f'{book_finished}.title'] = input('Enter the book title: ')
        book_collection[f'{book_finished}.author'] = input('Enter the book author: ')
        add_book = input('Do you want to add another book? (y/n)').lower()
        book_finished += 1
        if add_book in ['y','yes']:
            continue
        else:
            break
    return book_collection

def main():
    book_collection = ask_book()#unpacking dictionary
    book_save(**book_collection) #inserting into **kwargs

if __name__ == '__main__':
    main()
