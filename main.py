from core.search_helper import SearchHelper
from core.baseapp import BaseApp
from view.view_book import ViewBook
from view.input_book import InputBook


class MainApp(BaseApp):
    def _init_(self):
        self.books = []


if name == "_main_":
    app = MainApp()
    app.run()


def list_book(self):
    view = ViewBook(self.books)
    view.list()


def add_book(self):
    add = InputBook()
    add.input()


def search_book():
    cari = InputBook()
    cari.search()
    help = SearchHelper()
    help.search_title()
    liat = ViewBook(books=self)
    liat.list(
