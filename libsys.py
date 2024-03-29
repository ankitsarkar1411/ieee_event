# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 15:25:51 2024

@author: ankit
"""
class LibraryManagementSystem:
    #constructor
    def _init_(self):
        self.books = []
        
    def add_book(self,title,author,copies):
        book = {
            "title":title,
            "author":author,
            "copies":copies,
            "available_copies":copies
        }
        self.books.append(book)
        print(f"{title} book has been added to library!!!")
    
    def display_book(self):
        if self.books:
            for book in self.books:
                print("BOOK Details")
                print(f"Book Title: {book['title']} | Book Author: {book['author']} | Available copies: {book['available_copies']}")
        else:
            print("No books available")
    #helper function to find book(to check title book is present or not)
    def find_book(self, title):
        for book in self.books:
            if book['title'] == title:
                return book
        return None
    def barrow_book(self,title):
        book = self.find_book(title)
        if book is not None:
            if book['available_copies'] < book['copies']:
                book['available_copies'] -= 1
                print(f"{title} book has been barrowed successfully!!")
        else:
            print(f"The {title} book is not present in library!!")    
    def return_book(self,title):
        book = self.find_book(title)
        if book is not None:
            if book['available_copies'] <= book['copies']:
                book['available_copies'] += 1
                print(f"{title} book has been barrowed successfully!!")
        else:
            print(f"The {title} book is not present in library!!")
        
s= LibraryManagementSystem()
s.add_book('Algorithms', 'Alen', 5)   
s.add_book('Python', 'Roy', 10)  
s.display_book()
s.barrow_book('Python')     
s.return_book('Algorithm')   
        
            
            