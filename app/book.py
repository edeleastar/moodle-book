#!/usr/bin/env python
if __name__ == "__main__":
  from os              import path
  from controllers.App import App
  from models.Book     import Book  

  app = App(path.dirname(path.realpath(__file__)))
  book = Book()
  app.publishBook(book) 
  