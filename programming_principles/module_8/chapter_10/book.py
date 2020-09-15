class Book:
    
    def __init__(self, init_title, init_author, init_pages):
        self.__title = init_title
        self.__author_name = init_author
        self.__number_of_pages = init_pages

    # Show the current state of the object
    # Author, title and pages
    def __str__(self):
        return f'Author: {self.__author_name}\nTitle: {self.__title}\nPages: {self.__number_of_pages}'

    # Returns the number of pages in the book
    def __len__(self):
        return self.__number_of_pages
        
