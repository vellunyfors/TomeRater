from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678, 10)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345, 20)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938, 30)
print("Create novel with invalid price:")
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010, -13)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000, 50)

#Set price to some books afterwards
novel2.set_price(60)
novel1.set_price(99.90)

print("Set invalid prices:")
nonfiction1.set_price("asdf")
nonfiction1.set_price(-4000)


#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

print("Add existing email")
Tome_Rater.add_user("David2 Marr", "david@computation.org")
print("Add invalid emails")
Tome_Rater.add_user("Vellu", "test@email.xxx")
Tome_Rater.add_user("Vellu", "email.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
hr_book = Tome_Rater.highest_rated_book()
print("{book}, rating: {rating}".format(book=hr_book, rating=hr_book.get_average_rating()))
print("Most read book:")
print(Tome_Rater.most_read_book())

print("print Tome_Rater")
print(Tome_Rater)

print("Test comparison")
Tome_Rater2 = Tome_Rater
print("Should equal:")
if Tome_Rater == Tome_Rater2:
    print("TomeRaters are equals")
else:
    print("TomeRaters are not equal")

Tome_Rater3 = TomeRater()
Tome_Rater3.add_user("another user", "another@user.org")

print("Should not equal:")
if Tome_Rater == Tome_Rater3:
    print("TomeRaters are equal")
else:
    print("TomeRaters are not equal")

print("Test n most read books:")
print(Tome_Rater.get_n_most_read_books(3))
print(Tome_Rater.get_n_most_read_books(1000))
print(Tome_Rater.get_n_most_read_books(1.4))
print(Tome_Rater.get_n_most_read_books(-2))


print("Test n most prolific readers:")
print(Tome_Rater.get_n_most_prolific_readers(3))
print(Tome_Rater.get_n_most_prolific_readers(1000))
print(Tome_Rater.get_n_most_prolific_readers(1.4))
print(Tome_Rater.get_n_most_prolific_readers(-2))

print("Test n most expensive books:")
print(Tome_Rater.get_n_most_expensive_books(3))
print(Tome_Rater.get_n_most_expensive_books(1000))
print(Tome_Rater.get_n_most_expensive_books(1.4))
print(Tome_Rater.get_n_most_expensive_books(-2))


print("Test worth of a user:")
print(Tome_Rater.get_worth_of_user("marvin@mit.edu"))
print(Tome_Rater.get_worth_of_user("not@existing.user"))

print("Test best value book:")
print(Tome_Rater.get_book_with_best_rating_for_price())

