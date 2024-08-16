"""
sometimes you may want to raise an exception yourself
why? new devs spend enough time fixing the ones they already get!
becuase sometimes, stopping script execution is preferebale
to introducing invalid or malformed data into your system
"""
import BookError
books = [] #mutable list, intended for storing book dictionaries
num_books = 0
# new books may ONLY be created through the procedural add_new_book function
# each new book MUST HAVE an author first and last name > 2 characters
def add_new_book(title, author_fname, author_lname):
    if len(author_fname.strip()) <2 or len(author_lname.strip()) < 2:
        # print("names must be more than 2 characters long")
        raise BookError("names must be more than 2 characters long")
    else:
        book = {"title":title,
                "author_fname":author_fname,
                "author_lname":author_lname}
        books.append(book)
        global num_books
        num_books += 1
try:
    add_new_book("Scary Smart", "Mo", "Gawdat")
    add_new_book("Why We Drive", "Matthew", "Crawford")
    # add_new_book("Born To Run", "B", "S")
except:
    print("at least one book not created")

# add_new_book("Born To Run", "B", "S")#will generate BookError (custom name) in stack trace

print(books)#when instantiations wrapped in exception handling code no invalid Book object is added