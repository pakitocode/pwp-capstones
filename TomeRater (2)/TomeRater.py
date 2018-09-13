
                                # TOME RATER PROJECT
            # NAME: LY SON THACH
            # EMAIL: lysonthach@gmail.com
            # USER NAME: pakitocode

# This TomeRater class has methods below:

# Tome_Rater.print_catalog() # print the list of books that class hold.
# print(Tome_Rater.most_positive_user()) # print the most positive user, this user has highest book rating.
# print(Tome_Rater.highest_rated_book()) # print the highest rated book.
# print(Tome_Rater.most_read_book()) # print the book that has highest readers
# Tome_Rater.print_users() # print the list of users
# Tome_Rater.get_n_most_prolific_readers(3) # return 3 users that have read the most books
# Tome_Rater.get_n_most_expensive_books(3) # return 3 highest price books.

# Uncomment these sentences below and paste them blow the code to test the Tome Rater project:

#Tome_Rater = TomeRater()

# #Create some books:
# book1 = Tome_Rater.create_book("Society of Mind", 12345678, 20)
# novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345, 19)
# novel1.set_isbn(9781536831139)
# nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452, 23)
# nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938, 11)
# novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010, 21)
# novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000, 34)

# #Create users:
# Tome_Rater.add_user("Alan Turing", "alan@turing.com")
# Tome_Rater.add_user("David Marr", "david@computation.org")
# Tome_Rater.add_user("Pakito", "pakito@python.org")

# #Add a user with three books already read:
# Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

# #Add books to a user one by one, with ratings:
# Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
# Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
# Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
# Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
# Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

# Tome_Rater.add_book_to_user(novel3, 'nobook@python.org', 1)
# Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
# Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
# Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)
# Tome_Rater.add_book_to_user(novel3, "pakito@python.org", 5)
# Tome_Rater.add_user("Pakito2", "pakito@python.org")
# Tome_Rater.add_user("Pakito3", "pakito@python")
# Tome_Rater.add_user('Noname', 'nobook@python.org')


# Tome_Rater.print_catalog()
# print("Most positive user:")
# print(Tome_Rater.most_positive_user())
# print("Highest rated book:")
# print(Tome_Rater.highest_rated_book())
# print("Most read book:")
# print(Tome_Rater.most_read_book())
# Tome_Rater.print_users()
# Tome_Rater.get_n_most_prolific_readers(3) # return 3 users that have read the most books
# Tome_Rater.get_n_most_expensive_books(3) # return 3 highest price books.





class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {} #will map a Book object to this user’s rating of the book 
        self.user_book = {} # email of user and list of book they have read, email is key and book is value, value is a list of book
        # name will be a string
        # email will be a string

    def get_email(self):#that returns the email associated with this user 
        return self.email

    def change_email(self, new_email):# that takes in a new email and changes the email associated with this user.It should also print a message saying that this user’s email has been updated. 
        self.email = new_email
        print("user {name}'email has been updated successful".format(name=self.name))
    
    def read_book(self, book, rating = None):
        #should add a key:value pair to self.books where the key is book and the value is rating
        a = hash(book)
        if a not in self.books.keys():
            self.books[a] = [rating]
        else:
            self.books[a] += [rating]
        return self.books
    def number_books_read(self, book, email):
        if email not in self.user_book:
            self.user_book[email] = [book]
        else:
            if self.user_book[email] != None:
                self.user_book[email] += [book]
            else:
                self.user_book[email] = [book]
        #print(self.user_book)
        return self.user_book
        

    def __repr__(self):#returns a string to print out this user object like this: User Stephen Hawking, email: hawking@universe.edu, books read : 7
        a = 0
        number_books_read = [len(x) for x in self.user_book.values() if x != None] 
        return 'User {name}, email: {email}, books read : {number_books_read}'.format(name=self.name, email=self.email, number_books_read=number_books_read)

    def __eq__(self, other_user): #to deﬁne comparison between users
        return self.name == other_user.name and self.email == other_user.name
    

    
    def get_average_rating(self):
        #iterates through all of the values in self.books ,which are the ratings, and calculates the average rating. It should return this average
        average = 0
        list_average = {}
        b = self.books
        for key, value in b.items():
            for x in value:
                if x == None:
                    pass
                else:
                    average = sum(b[key]) / len(b[key])
                    list_average[key] = average
        return list_average
        #return average # this is average rating of book object


class Book(object):
    def __init__(self, title, isbn):
        self.title = title # will be a string 
        self.isbn = isbn # will be a number
        self.ratings = {} # pair email and rating as key:value
    def get_title(self):
        return self.title
        #returns the title of the books
    def __hash__(self):
        return hash((self.title, self.isbn))
    def __repr__(self):
        return '{title} with isbn {isbn}'.format(title=self.title, isbn=self.isbn)
        
    def get_isbn(self):
        #returns the isbn of the books
        return self.isbn
        
        
    def set_isbn(self, new_isbn):
        #takes in a new ISBN and sets the book’s isbn to be this new number.It should also print a message saying that this book’s ISBN has been updated. 
        self.isbn = new_isbn
        print("The book's isbn '{isbn}' has been updated".format(isbn=self.isbn))
        return self.isbn
        
        
    def add_ratings(self, email, rating): 
        #takes in a rating and adds it to the list self.ratings .It should only do this if rating is a valid rating(at least 0 and at most 4 ).Otherwise, it should print "Invalid Rating"
        self.email= email
        if rating in range(5):
            if email not in self.ratings:
                self.ratings[email] = [rating]
            else:
                self.ratings[email] += [rating]
        else:
            print("Invalid rating from user email: {user_invalid_rating}".format(user_invalid_rating=self.email))
        return self.ratings
            

    def __eq__(self, other):
        #to deﬁne comparison between books. A Book object should be equal to another Book object if they both have the same title and isbn.
        other = Book(self.title, self.isbn)
        return self.title == other.title and self.isbn == other.isbn
    
    def get_average_rating(self):
        #iterates through all of the values in self.ratings and calculates the average rating. It should return this average.
        average = 0
        list_average = {}
        b = self.ratings
        for key, value in b.items():
            average = sum(b[key]) / len(b[key])
            list_average[key] = average
        return list_average

    


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        if author:
            self.author = author
        
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return '{title} by {author}'.format(title=self.title, author=self.author)
    
class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        if subject:
            self.subject = subject # will be a string like "Geology"
        if level:
            self.level = level #will be a string like "advanced"
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return '{title}, a {level} manual on {subject}'.format(title=self.title, level=self.level, subject=self.subject)
    
class TomeRater:
    def __init__(self):
        self.users = {}
        #will map a user’s email to the corresponding User object, create a method to add data to this one
        self.books = {} #will map a Book object to the number of Users that have read it
        self.mail_books_read = {} # map email(key) and number of books(value) that users have read.
        self.user_books = {} #map email and book object
        self.hash_books = {} # map hashbook and book object as key:value
        self.book_price = {} # map price of book to object book
        
    def create_book(self, title, isbn, price):
        #creates a new book with that title and ISBN. Returns this Book object
        new_book = Book(title, isbn)
        a = hash(new_book)
        if a not in self.books.keys():
            self.books[a] = 0
        if a not in self.hash_books.keys():
            self.hash_books[a] = new_book
        if a not in self.book_price.keys():
            self.book_price[a] = price
        return new_book
        
    
    def create_novel(self, title, author, isbn, price):
        #creates a new Fiction with that title, author and ISBN.Returns this Fiction object
        fiction_book = Fiction(title, author, isbn)
        a = hash(fiction_book)
        if a not in self.books.keys():
            self.books[a] = 0
        if a not in self.hash_books.keys():
            self.hash_books[a] = fiction_book
        if a not in self.book_price.keys():
            self.book_price[a] = price
        return fiction_book
    
    def create_non_fiction(self, title, subject, level, isbn, price):
        #creates a new Non_Fiction with that title, author and ISBN.Returns this Non_Fiction object
        non_fiction_book = NonFiction(title, subject, level, isbn)
        a = hash(non_fiction_book)
        if a not in self.books.keys():
            self.books[a] = 0
        if a not in self.hash_books.keys():
            self.hash_books[a] = non_fiction_book
        if a not in self.book_price.keys():
            self.book_price[a] = price
        return non_fiction_book
    
    def add_book_to_user(self, book, email, rating=None):
        
        #print(self.user_books)
        #should get the user in self.users with the key email .If this user doesn’t exist,it should print out`“No user with email {email}!”.
        #If the user exists, it should:
        #Call read_book on this user,with book and rating
        #Call add_rating on book , with rating 
        #Check if the book is in TomeRater’s self.books already. If it is not, add the key book to self.books with a value of 1 (because one user has read it)
        #If book was already in the catalog, increase the value of it in self.books by 1,because one more user has read it.
        if email in self.users:
            if email not in self.user_books:
                self.user_books[email] = [book]
            else:
                self.user_books[email] += [book]
            self.users[email].read_book(book, rating)
            book.add_ratings(email, rating)
            self.users[email].number_books_read(book, email)
            #print(self.users[email].books)
            if hash(book) not in self.books:
                self.books[hash(book)] = 1
            else:
                self.books[hash(book)] += 1
        else:
            print("No user with email {email}!".format(email=email))
        #print(self.user_books)
        
        
    def add_user(self, name, email, user_books = None):
        #create a new User object from name and email. Then, if books is provided, it should loop through the list, and add each Book to the user(using the TomeRater method add_book_to_user) 
        self.email = email
        new_user = User(name, email)
        a = '@'
        b = ['.com', '.net', '.edu', '.org']
        last_letter = email[-4:]
        if email not in self.users.keys():
            if a in email and last_letter in b:
                self.users[email] = new_user
                if user_books != None:
                    for i in user_books:
                        self.add_book_to_user(i, email)
                else:
                    new_user.user_book[email] = None
            else:
                print('Invalid email {email}, please input your email again'.format(email=self.email))
                pass
        else:
            print("The email {email} has already exists, please input again".format(email=self.email))
            pass
        return self.users

    def print_catalog(self):
        #iterates through all of the keys in self.books (which are Book objects), and prints them 
        print('The list of books:')
        for a in self.hash_books.values():           
            #print(self.books)
            print(a)
    
    def print_users(self):
        #iterates through all of the values of self.users (which are the User objects),and prints them 
        a = self.users.values()
        print('The list of users:')
        for i in a:
            print(i)
    
    def most_read_book(self):
        #iterate through all of the books in self.books and return the book that has been read the most
        #Remember that the keys of self.books are Books,and the values are how many times they’ve been read. 
        most_read = ''
        max_viewer = 0
        for key, value in self.books.items():
            if value > max_viewer:
                max_viewer = value
                most_read = key
        print('The most read book:')
        return (self.hash_books[most_read])
            
        
    def highest_rated_book(self):
        #iterate through all of the books in self.books and return the book that has the highest average rating
        # Remember that the keys of self.books are Books, and you can call book.get_average_rating() on a Book object book
        
        highest_rated = 0
        book = ''
        for i in self.users.values():
            a = i.get_average_rating()
            for key, value in a.items():
                if value > highest_rated:
                    highest_rated = value
                    book = key
        print('The highest rated book:')
        return self.hash_books[book]
        
        
        
    def most_positive_user(self):
        #iterate through all of the users in self.users and return the user that has the highest average rating
        #Remember that the values of self.users are Users,and you can call user.get_average_rating() on a User object user
        highest_rating = 0
        largest_key = ''
        for books in self.user_books.values():
            if len(books) == 1:
                for book in books:
                    a = book.get_average_rating()
                    for key, value in a.items():
                        if value > highest_rating:
                            highest_rating = value
                            largest_key = key
            else:
                for x in books:
                    a = x.get_average_rating()
                    for key, value in a.items():
                        if value > highest_rating:
                            highest_rating = value
                            largest_key = key
        print('The most positive user:')
        return self.users[largest_key]
        #return user
        
    def get_n_most_prolific_readers(self, n):# return the users that has read the most books
        list_user_read = {}
        list_rank = {}
        list_user = []
        self.n = n
        x = 0
        for users in self.users.values():
            for key, value in users.user_book.items():
                if value != None:
                    list_user_read[key] = len(value)
                else:
                    pass
        a = list_user_read
        b = a.values()
        b = list(b)
        b.sort(reverse=True)
        for i in b:
            for key, value in a.items():
                if value == i:
                    list_rank[key] = value
                    list_user = list(list_rank)
        if n <= len(list_user):
            list_request = list_user[:n]
            print('The {n} users that have read the most book in descending order: '.format(n=self.n) )
            for i in list_request:
                x += 1
                print('Number {x}'.format(x=x))
                print(self.users[i])
        else:
            print('You have requested too many and the number you requested exceeding the number of users we have')
            
    
    def get_n_most_expensive_books(self, n):
        list_rank = {}
        list_books = []
        self.n = n
        x = 0
        a = self.book_price
        b = a.values()
        b = list(b)
        b.sort(reverse=True)
        for i in b:
            for key, value in a.items():
                if value == i:
                    list_rank[key] = value
                    list_books = list(list_rank)
        if n <= len(list_books):
            list_request = list_books[:n]
            print('The {n} highest price books in descending order: '.format(n=self.n))
            for i in list_request:
                x += 1
                print('Number {x}'.format(x=x))
                print(self.hash_books[i])
        else:
            print('You have requested too many and the number you requested exceeding the number of books we have')




