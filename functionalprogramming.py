from functools import reduce

books = [
 {"title": "to kill a Mockingbird", "author": "Harper Lee", "pages": 281, "year": 1960},
 {"title": "1984", "author": "George Orwell", "pages": 328, "year": 1949},
 {"title": "pride and Prejudice", "author": "Jane Austen", "pages": 432, "year": 1813},
 {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "pages": 180, "year": 1925},
 {"title": "Moby-Dick", "author": "Herman Melville", "pages": 635, "year": 1851}]

#convert all book titles ot uppercase
def upper(s):
    return s["title"].upper()
uppercase = list(map(upper, books))
print(uppercase)

#filter books published after 1900
def year_above_1900(s):
    return s["year"] > 1900
above_1900 = list(filter(year_above_1900, books))
print(above_1900)

#total number of pages
def total_pages(a, b):
    return a + b
def book_pages(s):
    return s["pages"]
book_pgs = list(map(book_pages, books))
total_p = reduce(total_pages, book_pgs)
print(total_p)

#average pages for books published before 1950
def before_1950(s):
    return s["year"] < 1950
def average_pgs(a, b):
    return a + b

books_before_1950 = list(filter(before_1950, books))
average_pgs_before_1950 = reduce(average_pgs, map(book_pages, books_before_1950))
print(average_pgs_before_1950/len(books_before_1950))

#rewriting task 2 with list comprehension
filtered_books_after_1900 = [book for book in books
                 if book["year"] > 1900]
print(filtered_books_after_1900)

#sorting and combining using lambda function to grab first 3 elements
top_3_total_pages = sum(map(book_pages, sorted(books, key=lambda x: x['pages'], reverse=True)[:3]))
print(top_3_total_pages)

#generator expression
sorted_by_title = sorted(books, key=lambda x: x['title'])
print(sorted_by_title)