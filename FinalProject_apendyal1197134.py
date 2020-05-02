#Book Class- It creates book objects to be used in the program. 
class Book():
    def __init__(self, title, author, genre, price):
        
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.book = [self.title, self.author, self.genre, self.price]
    def book(self):
        return(self.book)
    def __str__(self):
        return ("\n Title: " + str(self.book[0]) + "\n Author(s): " + str(self.book[1]) + "\n Genre: " + str(self.book[2]) + "\n Price: " + str(self.book[3])+"\n"+"="*32 + "\n")

#Inventory class- A list of book objects, contains all of created book objects. It  gets info that you need to create objects from the file.      
class Inventory():
    def __init__(self):
        pass
#add_book method finds info needed and collects it, while appropriately spliting the lines. 
    def add_book(self):
        book_list = open('booklist.txt', 'r+')
        read_list = book_list.readlines()
        book_info_seperate = []
        length = len(read_list)
        i = 0
        while (i < length):
            tempstring = read_list[i]
            tempstring = tempstring.rstrip('\n')
            read_list[i] = tempstring
            i = i + 1

        for count in range (0, length):
            data = read_list[count].split(',')
            book_info_seperate.append(data)

        temp_list_items = []
        temp_list_books = []
        for count in range(0, length):
            temp_list_items.append(book_info_seperate[count][0])
            new_book = Book(book_info_seperate[count][1],book_info_seperate[count][2],book_info_seperate[count][3],book_info_seperate[count][4])
            temp_list_books.append(new_book)

#map called "books." Instead of manually creating a map, I just used the dict() function which turns things into maps. 
        self.books = dict(zip(temp_list_items, temp_list_books))
        return(self.books)
#display method just displays the book objects    
    def display(self):
        for key in self.books:
            print(" Item number: " + key)
            print(self.books[key])
#Cart class, a subclass of Inventory. They are the same, except that cart uses the user's input.
class Cart(Inventory):
    def __init__ (self):
        self.inventory = Inventory()
        self.inventory = self.inventory.add_book()
        self.temp_key = []
        self.temp_value = []
    #add_book method, It is overwriting the add_book method in the inventory class.
    #It is using the user's input to make a list of the books they want, unlike the Inventory class which pulls info from files.
    def add_book(self, item_num):
        self.item_num = item_num
        length_before = len(self.temp_key)
        for key in self.inventory:
            if key == self.item_num:
                self.temp_key.append(key)
                myBook = self.inventory[key]
                self.temp_value.append(myBook)
        if length_before == len(self.temp_key):
            print('That item does not exist in the inventory!')

   #view_cart method, It displays what is inside of the cart.         
    def view_cart(self):
        for value in self.temp_key:
            print()
            print(' Item number: ' + value)
            print(self.inventory[value])
        if len(self.temp_key) == 0:
            print('Your cart is empty!')
##checkout method, It adds the prices of the books that the user added to their cart and displays the total price.
    def checkout(self):
        self.empty_int = 0
        for value in self.temp_key:
            if value == '1000':
                cost = 23.99
                self.empty_int = self.empty_int + cost
            if value == '1001':
                cost = 3.99
                self.empty_int = self.empty_int + cost
            if value == '1002':
                cost = 3.99
                self.empty_int = self.empty_int + cost
            if value == '1003':
                cost = 9.99
                self.empty_int = self.empty_int + cost
            if value == '1004':
                cost = 61.99
                self.empty_int = self.empty_int + cost
            
        if self.empty_int == 0:
            return("Your cart is empty!")
        else:
            print("Thanks for shopping with us!")
            return("Your total is: $"+ str(self.empty_int))
            
#delete_book method, It deletes books from the cart if the user wants to get rid of a book.
    def remove_book(self, item_num):
        if item_num in self.temp_key: 
            self.temp_key.remove(item_num)
            print("Item " + item_num + " was removed.")
        else:
            print('Item ' + item_num + ' is not in your cart. ')


list_of_books_bought = []   
cart = Cart()   
run = True
while run == True:
    #options menu
    print('\n\n\n\nWelcome to ABC Book Store!')
    print('-' * 47)
    print('Here\'s what you can do:')
    print('1. Display a list a books available for sale. ')
    print('2. Buy a book from the list of available books and add it into your cart. ')
    print('3. Show items in your cart. ')
    print('4. Checkout.')
    print('5. Delete a book in your cart. ')
    print('6. Exit the program. ')

    choice = input('What would you like to do? ')
    inventory = Inventory()
    inventory_run = inventory.add_book()

    
#if/elif Statements that run based on the user's choice

#Display all of the books
    if choice == '1':
      inventory.display()
#Adding a book to your cart
    elif choice == '2':
        item_num = input("What book do you want to buy? Enter in the item number. ")
        list_of_books_bought.append(item_num)
        cart.add_book(item_num)
#Checking your cart
    elif choice == '3':
        cart.view_cart()
#Displays the total price of the books you have checked out
    elif choice == '4':
        print(cart.checkout())

#Delete a book from your cart
    elif choice == '5':
        item_num = input('Enter the item number of the book you would like to delete from your cart: ')
        cart.remove_book(item_num)
#If the user wants to exit the program, the run loop will end and the program will stop 
    elif choice == '6':
        print("Thanks for shopping with us!")
        run = False
#If the user does not enter a number from the options listed above. 
    else:
        print()
        print('Please select a number from the options listed above.')
        print()



