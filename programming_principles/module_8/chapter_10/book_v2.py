class Book:

    def __init__(self, init_title, init_author, init_publisher):
        self.set_book_title(init_title)
        self.set_author_name(init_author)
        self.set_publisher_name(init_publisher)

    def __str__(self):
        return f'Title: {self.__title}\nAuthor: {self.__author}\nPublisher: {self.__publisher}'
    
    def set_book_title(self, new_title):
        self.__title = new_title

    def set_author_name(self, new_author):
        self.__author = new_author

    def set_publisher_name(self, new_publisher):
        self.__publisher = new_publisher

    def get_book_title(self):
        return self.__title

    def get_author_name(self):
        return self.__author

    def get_publisher_name(self):
        return self.__publisher
