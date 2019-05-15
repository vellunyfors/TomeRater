class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address

    def read_book(self, book, rating=None):
        if type(book) is Book or type(book) is Fiction or type(book) is Non_Fiction:
            self.books.update({book: rating})
        else:
            print("Book not valid")

    def get_average_rating(self):
        if len(self.books) > 0:
            total = 0
            count = 0
            values = self.books.values()
            for value in values:
                if value is not None:
                    total += value
                    count += 1
            if count == 0:
                print("No ratings")
                return 0
            return total/count
        else:
            print("No books")
            return 0

    def __repr__(self):
        return "User {name}, email: {email}, books read: {booksRead}".format(name=self.name, email=self.email, booksRead=str(len(self.books)))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email


class Book(object):
    def validate_price(self, price):
        if (isinstance(price, int) or isinstance(price, float)) and price >= 0:
            return True
        return False

    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        if not self.validate_price(price):
            print("Invalid price '{}', setting price to zero".format(price))
            price = 0
        self.price = price
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("{title} isbn has been updated".format(title=self.title))

    def set_price(self, new_price):
        if not self.validate_price(new_price):
            print("Invalid price '{}', price not updated".format(new_price))
            return
        self.price = new_price

    def add_rating(self, rating):
        if rating is not None and 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid rating")

    def get_average_rating(self):
        if len(self.ratings) > 0:
            total = 0
            for value in self.ratings:
                if value is not None:
                    total += value
            return total/len([rating for rating in self.ratings if rating is not None])
        else:
            print("No books")
            return 0

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def __repr__(self):
        return "Title: {title}, ISBN: {isbn}".format(title=self.title, isbn=self.isbn)

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn, price):
        super().__init__(title, isbn, price)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn, price):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)


class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "TomeRater: {users} users and {books} books".format(users=str(len(self.users)), books=str(len(self.books)))

    def __hash__(self):
        return hash((self.users, self.books))

    def validate_isbn(self, isbn):
        if isbn in [book.isbn for book in self.books.keys()]:
            print("ISBN: {} already in books".format(isbn))
            return False
        return True

    def validate_email(self, email):
        if "@" in email and email[-4:] in [".com", ".edu", ".org"]:
            return True
        else:
            return False

    def create_book(self, title, isbn, price=0):
        return Book(title, isbn, price)

    def create_novel(self, title, author, isbn, price=0):
        return Fiction(title, author, isbn, price)

    def create_non_fiction(self, title, subject, level, isbn, price=0):
        return Non_Fiction(title, subject, level, isbn, price)

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, None)
        if user is not None:
            user.read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                if not self.validate_isbn(book.isbn):
                    return
                self.books.update({book: 1})

    def add_user(self, name, email, user_books=None):
        if email in self.users:
            print("User '{email}' already exists".format(email=email))
            return
        if not self.validate_email(email):
            print("Email '{email}' is not valid".format(email=email))
            return
        self.users.update({email: User(name, email)})
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        if len(self.books) <= 0:
            print("No books")
            return
        return max(self.books, key=self.books.get)

    def highest_rated_book(self):
        highest_book = ""
        highest_rating = float("-inf")
        for book in self.books:
            rating = book.get_average_rating()
            if rating > highest_rating:
                highest_rating = rating
                highest_book = book
        return highest_book

    def most_positive_user(self):
        if len(self.users) <= 0:
            print("No users")
            return
        most_positive_user = ""
        highest_rating = float("-inf")
        for user in self.users.values():
            rating = user.get_average_rating()
            if rating > highest_rating:
                highest_rating = rating
                most_positive_user = user
        return most_positive_user

    def get_n_most_read_books(self, n):
        if not isinstance(n, int) or n <= 0:
            print("Invalid input '{}'".format(n))
            return
        return sorted(self.books, key=self.books.get, reverse=True)[:n]

    def get_n_most_prolific_readers(self, n):
        if not isinstance(n, int) or n <= 0:
            print("Invalid input '{}'".format(n))
            return
        user_books_dict = {user.email: len(user.books) for user in self.users.values()}
        return sorted(user_books_dict, key=user_books_dict.get, reverse=True)[:n]

    def get_n_most_expensive_books(self, n):
        if not isinstance(n, int) or n <= 0:
            print("Invalid input '{}'".format(n))
            return
        book_price_dict = {book: book.price for book in self.books.keys()}
        return sorted(book_price_dict, key=book_price_dict.get, reverse=True)[:n]

    def get_worth_of_user(self,	user_email):
        user = self.users.get(user_email, None)
        if user is None:
            print("User '{email}' not found".format(email=user_email))
            return
        total = 0
        for book in user.books.keys():
            total += book.price
        return total

    def get_book_with_best_rating_for_price(self):
        best_value_book = ""
        best_value = float("-inf")
        for book in self.books.keys():
            if book.price == 0:
                continue
            value = book.get_average_rating() / book.price
            if value > best_value:
                best_value_book = book
                best_value = value
        return best_value_book
