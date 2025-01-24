class Book:
    def __init__(self, number_of_pages, author):
        self.number_of_pages = number_of_pages
        self.author = author
        self.is_open = False
        self.current_page = 1
    
    def open_book(self):
        self.is_open = True

    def close_book(self):
        self.is_open = False

    def go_to_page_p(self, p):
        self.current_page = p
        