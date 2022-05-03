import utils
import sorts

# start testing by loading the small list of books
bookshelf = utils.load_books('books_small.csv')

# Add a for loop to print the titles within the bookshelf.
for book in bookshelf:
    print(book["title"])

# Python’s built-in comparison operators compare letters lexicographically based on their Unicode code point.
# You can determine the code point of characters using Python’s built-in ord function.
print(f"Code point of \"a\" is {ord('a')}")
print(f"Code point of \" \" is {ord(' ')}")
print(f"Code point of \"A\" is {ord('A')}")


# by_title_ascending - take book_a and book_b as arguments.
# Return True if the title_lower of book_a is “greater than” the title_lower of book_b and False otherwise.
def by_title_ascending(book_a, book_b):
    return book_a["title_lower"] > book_b["title_lower"]


print("\nBubble_sort by title asc:")
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort_1:
    print(book['title'])


# by_author_ascending - take book_a and book_b as arguments.
# Return True if the author_lower of book_a is “greater than” the author_lower of book_b and False otherwise.
def by_author_ascending(book_a, book_b):
    return  book_a["author_lower"] > book_b["author_lower"]


print("\nBubble_sort by author asc:")
# The sorting algorithms will alter the original bookshelf, so create a new copy of this data.
bookshelf_v1 = bookshelf.copy()
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)

for book in sort_2:
    print(book['author'])


print("\nQuicksort by author asc:")
bookshelf_v2 = bookshelf.copy()
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2)-1, by_author_ascending)
for book in bookshelf_v2:
    print(book['author'])


# by_total_length - take book_a and book_b as arguments.
# Return True if the sum of characters in book_a's title + author is “greater than” the sum of characters
# in book_b's title + author, False otherwise.
def by_total_length(book_a, book_b):
    return (len(book_a['title'])+len(book_a['title'])) > (len(book_b['title'])+len(book_b['title']))


# now lets test on the large list of books
long_bookshelf = utils.load_books('books_large.csv')
# print("\Bubble_sort by total length:")
# sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)

print("\nQuicksort by total length:")
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf)-1, by_total_length)
for book in long_bookshelf:
    print(f"Author: {book['author']}, Title:{book['title']}\n")
