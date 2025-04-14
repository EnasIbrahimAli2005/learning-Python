
# My project graduation from unit 1

# print ("Welcome to the YouTube channel name generator:\n")
# nickname=input("What is your nickname?\n")
# channel_about=input("What is your channel about?\n")
# print("You could name your channel"+ "(" + channel_about + " with " +  nickname + ")" )

# # # My project graduation from unit 2

# str_seconds=input("Enter the duration in seconds:\n")
# miuntes=int(str_seconds)//3600
# hours=miuntes//60
# second=hours%60
# print(f"the duration is : {hours}hours,{miuntes}minutes,and{second}seconds")



# unit 3
# project 1

# print("Welcome to my application\n ")
# age=int(input("How old are you ?\n"))
# if(age<12):
#     print("sorry,you can not use the app.")
# else:
#     print("Good, you can use the app.")
    
# # project 2

# score = float(input("Enter your score\n"))
# if(score>=90):
#     print("A")
# elif(score>=75):
#     print("B")
# elif(score >=50):
#     print("c")
# else:
#     print("D")
    
# project 3
# password=input("Enter your password \n")
# correct_password="abc"
# if(password==correct_password):
#     print("Welcome")
# else:
#     print("sorry")
    
# project 4

# user_input=input("Enter yes ,no,maybe\n")
# if(user_input=="yes"):
#     print("you write yes")
# elif(user_input=="no"):
#     print("you write no")
# elif(user_input=="maybe"):
#     print("you write maybe")
# else:
#     print(f"you writed {user_input}")
    
    
# # project 5

# guess=int(input("gusse namber\n"))
# correct_gusses=7
# if(guess==correct_gusses):
#     print("correct")
# else:
#     print("incorrect")



# My project graduation from unit 3

# print(""" 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$__$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$_______________$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$___________________$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$____$$$_________$$$____$$$$$$$$$$$$$
# $$$$$$$$$$$$$_____$$$_________$$$_____$$$$$$$$$$$$
# $$$$$$$$$$$$___________________________$$$$$$$$$$$
# $$$$$$$$$$$$___________________________$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$_____$$$____________________________$$$____$$$
# $$$$_____$$$____________________________$$______$$
# $$$$_____$$$____________________________$$______$$
# $$$$_____$$$____________________________$$______$$
# $$$$_____$$$____________________________$$______$$
# $$$$_____$$$____________________________$$______$$
# $$$$_____$$$____________________________$$______$$
# $$$$______$$____________________________$$______$$
# $$$$_____$$$____________________________$$______$$
# $$$$$___$$$$____________________________$$$___$$$$
# $$$$$$$$$$$$____________________________$$$$$$$$$$
# $$$$$$$$$$$$____________________________$$$$$$$$$$
# $$$$$$$$$$$$___________________________$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                         """)
# print("Welcome to my island!\n")
# print("there are two doors in front of you. A red door and A blue door .")
# coloar=input ("which door do you want open?\n").lower()
# if(coloar=="blue"):
#     print("Oops! You chose the crocodile door. ")
#     print("Game over!")
# elif(coloar=="red"):
#     print("Great! now you enterd a room.")
#     print("you found three boxes: white ,black,green\n")
#     coloar_boxes=input("Which box do you open?\n")
#     if(coloar_boxes=="white"):
#         print("Oops!You opened a box filled with snakes.")
#     elif(coloar_boxes=="black"):
#         print("Oops! You opened a box filled with spiders.")
#     elif(coloar_boxes=="green"):
#         print("Congratulation! You found the treasure!")
#     else:
#         print("Invalid choice! ")
# else: 
#     print("Invalid choice!")
    

# unit 4

#project 1

# import random   
# my_random_number=random.randint(-5,5)
# print(my_random_number)

# # How to create moduales

# import Mymodual
# print(Mymodual.course)
# print(Mymodual.level)
# print(Mymodual.teasher)

# #project 2

# import random
# PIN_Code=random.randint(1000,9999)
# user_input=int(input("Enter a 4 PIN code :\n"))
# if(user_input < 4 or user_input>4):            #if(user_input!=4)
#     print("Please Enter 4 digits")
# elif(PIN_Code==user_input):
#     print("Congratualation!")
# else:
#     print("Failure! PIN code did not match.")
#     print(f"The compuater generated this PIN :{ PIN_Code}")
    
# project 3

# random() => [0,1)float 

# import random
# random_number=random.random()
# print(random_number)
# # number betwen 0,number
# # random()*number
# random_number=random.random()*5
# print(random_number)



# # project 4

# import random 
# print("Welcome to the coin Guessing Game!")
# print("choose a method to toss the coin:")
# print("1. using random.random()")
# print("2. using random.randint()")
# choice=input("Enter your choice (1 or 2)\n")



# if(choice=="1"):
#      method1=random.random()
#      if(method1>=0.5):
#          computer_result="Heads"
#      else:
#          computer_result="Tails"
# elif(choice=="2"):
#      method2=random.randint(0,1)
#      if(method2==0):
#          computer_result="Heads"
#      else:
#          computer_result="Tails"
# else:
#     print("Invalid choice. Please select either 1 or 2.")
    




# user_choice=input("Enter your guess (Heads or Tails)\n").lower()

# if(user_choice==computer_result.lower()):
#     print("Congratulations! You Won!")
# else:
#     print("Sorry, you lost!")
          
    

# print(f"The computer coin toss result was:{computer_result}")

   
# project 5

# my_best_friend=[ "Esraa","Engy","Arwa","Hassna","Alaa"]
# print(f"The first name in our list is:{my_best_friend[0]} and the last name in our list is:{my_best_friend[-1]}")

# my_best_friend[-1]="kholod"
# print(f"The first name in our list is:{my_best_friend[0]} and the last name in our list is:{my_best_friend[-1]}")
# print(my_best_friend)

# # append("....")
# color=[]
# color.append("red")
# print(color)


# # project 6

# color1=input("Add the first color you like :\n")
# color=[]
# color.append(color1)
# more_color=input("Do you want to add more color ?Yes or No?\n").lower()
# if(more_color=="yes"):
#     color2=input("Add anther color to the list :")
#     color.append(color2)
#     print(f"The colors you like are :{color}")
    
# # extend(......)

# class_a=["tom","Enas","osama"]
# class_b=["hoda","ebrahim","Ali"]
# class_a.extend(class_b)
# print(class_a)
#  # anther solution
# class_a=["tom","Enas","osama"]
# class_b=["hoda","ebrahim","Ali"]
# all_student=[]
# all_student.extend(class_a)
# all_student.extend(class_b)
# print(all_student)

# # anther solution

# class_a=["tom","Enas","osama"]
# class_b=["hoda","ebrahim","Ali"]
# student=class_a+class_b
# print(student)

# remove(....)

# numbers=[3,5,7,9]
# numbers.remove(3)
# print(numbers)
# guess=int(input("Guess the name of the fruits in the basket\n"))
# # لتحقق من وجود قيمة في اليست
# if guess in numbers:
#     print("Good guess")
# else:
#     print("Sorry, better luck next time")
# # لتحقق من ان اليوزر دخل حاجة

# name=input("What is your name?")
# if name:
#     print(f"Hello,{name}")
# else:
#     print("You forgot to enter your name")
    

# My project graduation from unit 4

# books=[]
# book1=input("Enter the name of a book you own:\n")
# books.append(book1)
# book2=input("Enter the name of anther book you own(or press 'Enter' to skip):\n")
# if(book1):
#     books.append(book2)
# print(f"Your Library:\n{books}")   # print("your library :\n" ,books)


# future_books=[]
# books_wish1=input("Enter the name of a book you wish to have in the future:\n")
# future_books.append(books_wish1)
# books_wish2=input(f"Enter the name of antherbook you wish to have (or press'Enter' to skip):\n")
# if(books_wish2):
#     future_books.append(books_wish2)
# print(f"Your wishlist:\n{future_books}")

# all_books=[]
# acquired_books=[]
# acquired_books1=input("Enter the name of a book from your wishlist that you have acquired (or press 'Enter' to skip):\n")
# acquired_books.append(acquired_books1)
# if acquired_books:
#     if acquired_books1 in future_books:
#       all_books=acquired_books+books
#       future_books.remove(acquired_books1)
   
# print(f"Updated Library: {all_books}")
# print(f"Updated wishlist:{future_books}")

# donate=[]
# donate1=input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip):\n")
# donate.append(donate1)
# if donate:
#     if(donate1 in donate):
#        all_books.remove(donate1)
#        print(f"Final library after Donations :{all_books}")

    

# unit 5

# split("   ")

# names_string=input("Enter names sparated dy a comma.....\n")
# names=names_string.split(", ")
# print(type(names)) 
# print(names)

# print(len(names))

# project 1

# import random 
# names_string=input("""Welcome to 'Whose Wallet?'\nYou will give me a list of names, and I will picka person to pay\nIf you are ready, enter the names sparatered by a comma\n""")
# names=names_string.split(", ")
# size_names=len(names)
# random_names=random.randint(0,size_names-1)
# print(f"Please ask '{names[random_names]}' to take his wallet out .Dinner is on him") 

#or

#names_string=input("""Welcome to 'Whose Wallet?'\nYou will give me a list of names, and I will picka person to pay\nIf you are ready, enter the names sparatered by a comma\n""").split(", ")
#print(f"Please ask '{random.choice(names_string)}' to take his wallet out .Dinner is on him.") 

# nested list 
# basket=[]
# basket=[["apple","bannana"],["milk","water"]]
# print(basket[0][0],basket[1][0])
# desert=["cake","candy"]
# basket.append(desert)
# print(basket)
# basket.insert(1,"enas")
# print(basket)

# ############################################
# books=["book2","book3","book5"]
# books.insert(0,"book1")
# books.insert(3,"book4")
# books.insert(5,"book6")
# print(books)
# #or
# books.append("book6")
# print(books)

# project 2
# fruits=["Apple","Bananas"]
# fruits.insert(0,"Orange")
# fruits.insert(3,"Kiwis")

# luikuid=["Milk","Water"]
# luikuid.insert(0,"Coffee")
# luikuid.remove(luikuid[1])
# luikuid.append("Tea")

# numbers=[1, 2, 3]

# basket=[["Apple","Bananas"],["Milk","Water"]]
# print(basket)
# input("Press enter to change the content........")
# basket.remove(basket[0])
# basket.remove(basket[0])
# basket.insert(0,fruits)
# basket.insert(1,luikuid)
# basket.insert(2,numbers)


# print(f"Here is the updated basket\n{basket}")

####################################################or
# basket=[]
# basket=[["Apple","Bananas"],["Milk","Water"]]
# print(basket)
# input("Press enter to change the content........")
# basket[0].insert(0,"Orange")
# basket[0].append("Kiwis")
# basket[1].insert(0,"Coffee")
# basket[1].append("Tea")
# basket[1].remove("Water")
# basket.append([1,2,3])
# print(f"Here is the updated basket\n{basket}")


# project 3





#############################################################





# unit 5 loop

# name="Enas"
# for x in name:
#     print(x.upper())



# color=["Red","Blue","Green","Yellow"]
# for y in color:
#     if y=="Blue":
#         print(f"the blue is my favorate color")
#     else:
#      print(y)
     
# project 1
# numbers=[1,2,3,4,5,6,7,8,9,10]
# for x in numbers:
#    if x%2==0:
#       print(x)
#       print("\n")
      
# print("Finished the loop successfully")


# project 2

# attendence=["Alice","Bob","Charlie"]
# for x in attendence:
#    print(x)
#    confirmed_attendance=input("Is this person attending?(yes/no):").lower()
#    if confirmed_attendance=="yes":
#       print("Attendance confirmed.")
#    else:
#       print("Attendance not confirmed.")
#    print("-----------------")   
   

#project 3

# task_list=input("Enter your tasks for today sparated by a comma :\n").split(", ")
# done=[]
# ongoing=[]

# for task in task_list:
#    print(f"\n{task}\n")
#    done_task=input(f"Did you finish {task} already?\n").lower()
#    if done_task=="yes":
#       done.append(task)
#       print("Nice job \n--------------------")
#    else:
#       ongoing.append(task)
#       print("Try not to put it off\n-------------------")
      

# see_progress=input("Do you want to see your today s progress?(yes, no)\n").lower()
# if(see_progress=="yes"):
#     print("\n*************** Done Tasks ***************\n")
#     print(done)
#     print("**************** Ongoning Tasks ************\n")
#     print(ongoing)
    

# range(stop)=> start 0
#range(start, stop)
# range(start,stop, step)

# for i in range(10):
#    print(i)
   

# for i in range(1,11):
#    print(i)
   

#range( start, stop, step)

# for i in range(0,20,2):
#    print(i)


# project 3

# print("\n**** Welcome to the multiplication table ***")
# number=int(input("Enter a number:"))
# print(f"Multiplication table for {number}:")
# for i in range(1,11):
#     mul=number*i
#     print(f"{number} * {i} = {mul}")
    
    # project 4


# basket=[]
# price=[]
# print("*** Welcome to ishop calculater ***")
# number_items=int(input("How many items are there in your basket today ? "))
# print("Let is get to counting them...... ")
# for i in range(1,number_items+1):
#     name_item=input(f"Please tell me the name of the item number {i} ")
#     price_item=float(input(f"What is the price of {name_item}?\n$ "))
#     basket.append(name_item)
#     price.append(price_item)
    
# basket_items=input("Would you like to see your entire basket iteams? ")
# if basket_items=="yes":
#     print(basket)
    

# total_price=input("Would you like to see how much total cost ?")
# if total_price=="yes":
#     for x in range(1,number_items+1):
#         #price=price+x
#          price_items_total=sum(price)
#     print(f"Buying these items will cost :\n{price_items_total}")
    
### .join(v)-> هتلحق كل عنصر بحاجة
# slice
### print(names[0:4])
### print(names[0:4:2])
    
# My project graduation from unit 3
# import random
# import string
# password=[]
# print("Welcome to the password Generator!")
# total_number=int(input("Enter the total number of characters in the password: "))
# number_letter=int(input("Enter the number of letters in the password: "))
# number_number=int(input("Enter the number of numbers in the password: "))
# number_symbol=int(input("Enter the number of symbols in the password: "))
# total_input=number_letter+number_symbol+number_number
# if total_input==total_number:
#     letter=(random.choices(string.ascii_letters,k=number_letter))
#     number=(random.choices(string.digits,k=number_number))
#     symbol=(random.choices(string.punctuation, k=number_symbol))
#     password.append(letter)
#     password.append(number)
#     password.append(symbol)
#     random.shuffle(password)

#     for x in password:
#         password=password+x
#     print (  f"Generated Password : {password}")

# else:
#     print("Invalid input . The sum of letters, numbers,and symbols does not match the password")



# def welcome():
#     print("Welcome to the program")
    
# def thanks():
#     print("Thanks for using the program. See you soon!")
    


# welcome()
# input("Press Enter to exit ")
# thanks()

# for loop vs wihle loop

# import random
# number_random=random.randint(1,10)
# number=int(input("Guess a number between 1 and 10: "))
# while number_random!=number:
   
#    if number<number_random:
#       number=int(input("Too low! Guess again: "))
#    else:
#       number=int(input("Too high!Guess  again"))
      
# print("Congratulation ! you guess the number!")
      
      

# unit 4
#Hangman

# import random 
# # stages hangman.....
# HANGMANPICS = ['''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''']

# words=["office","panda","cadin","ginger"]
# random_word=random.choice(words)
# display=["_"]*len(random_word)
# print(" ".join(display))
# tries=6

# #قائمة لتخزين الحروف التي تم تخمينها
# guess_letter=[]
# print(HANGMANPICS[0])
# while "_" in display and tries>0:
#     guessed=input("Please guess a letter: ").lower()
#     #هل الحرف تم تخمينه قبل ذلك 
#     if guessed in guess_letter:
#         print("You already guessed that. Try again.")
#         print(f"You have {tries} more tries")
#         continue
#     #في حالة لم يسبق تخمينه0 ضيفة للقايمة
#     guess_letter.append(guessed)
    
#     if guessed not in random_word:
#         tries-=1
#         print(HANGMANPICS[6-tries])
#     else:
#       for position in range(len(random_word)): 
#          if random_word[position]==guessed:
#              display[position]=guessed
             
#     print(" ".join(display))
#     print(f"You have {tries} more tries")
    

# if tries==0:
#     print("           You lose!            \n")
#     print(HANGMANPICS[-1])
        
    
# else:      
#    print("""
#        *************
#           YOU WIN
#        *************""")    
    



# def multiplication(number):
#     for i in range(1,11):
#        mul=number*i
#        print(f"{number} * {i} = {mul}")
    
# multiplication(7)

# الشفرة

# import string
# alphabet=string.ascii_lowercase
# word=input("Please type a word: ").lower()
# encrypted_word=""
# for letter in word:
#     if letter not in alphabet:
#         encrypted_word+=letter
#     else:
#         original_position=alphabet.index(letter)
#         new_possition=(original_position+2)%26
#         encrypted_word+=alphabet[new_possition]
    
    # if letter != "z":
       # original_position=alphabet.index(letter)
       # new_possition=original_position+2
       # encrypted_word+=alphabet[new_possition]
# print(f"Here is the encrypted word : {encrypted_word}")
    

# import string
# def crypt(massage,number):
    
#     encrypted_massage=""
#     alphabet=string.ascii_letters
#     for letter in massage:
#         if letter.lower() in alphabet:
#             original_position=alphabet.index(letter.lower())
#             new_possition=(original_position-number)%26
#             encrypted_letter=alphabet[new_possition]
#             if letter.isupper():
#                 encrypted_letter=encrypted_letter.upper()
#             encrypted_massage+=encrypted_letter  
#         else:
#            encrypted_massage+=letter
#     print(f"Here is the encrypted word : {encrypted_massage}")
    
# massage=input("Enter a massage:  ")
# number=int(input("Enter a shift number:"))
# crypt(massage,number)

# Dictionary

# book={
#     'title':'red queen',
#     'outhor':'victoria aveyarad',
#     }
# print(book[1])

#project 1

# student={
#     1:"Jack sparrow",
#     2:"Vito Corleone",
#     3:"Gandalf",
#     4:"Darth Vader",
#     5:"Jack Sparrow"}
# for number in student:
#     print("Student ID:")
#     print(number)
#     print("Student name :")
#     print(student[number])
#     print("====================================")
    
# info={}
# user_name=input("What is your name? ")
# user_place=input("Where are you from ?")
# user_age=int(input("How old are you? "))  
# info["name"]=user_name
# info["contry"]=user_place
# info["age"]=user_age
# print(info)



## project 2


# contact={}
# while True:
#       print("Contact Mangement ")
#       print("""
# 1- Add a contact            
# 2- View contact 
# 3-Edit a contact 
# 4- Exit \n""" )  
#       choose_number=int(input("Please choose number from 1-4 : "))
#       if choose_number==1:
#           Id_contact=input("Enter the contact ID: ") 
#           name=input("Please type a name : ")
#           phone_number=int(input("Please type a phone number : "))
#           contact["ID"]=Id_contact
#           contact["name"]=name
#           contact["phone"]=phone_number
#           print(f" \n\n  {name} was added successfully......")    
#       elif choose_number==2:
#            print(contact)
#       elif choose_number==3:
#           Id_to_edit=input(" Please enter an ID edit : ")
#           if Id_to_edit in contact["ID"]:
#              new_name=input("Enter a new name : ")
#              new_phone=int(input("Enter a new number : "))
#              contact["name"]=new_name
#              contact["phone"]=new_phone
#              print("     Success......  ")
#           else:
#               print(f"Sorry, {Id_to_edit} was not found.......") 
#       else:
#            print("Exiting the program........")
#            break
          
# import os          
# print(os.name)
# print("Hallo")
# print("Hallo")
# print("Hallo")
# input("\nPress any key to clear the screen.......")
# if os.name=="nt":
#     os.system("cls")
# else:
#     os.system("clear")
    
# ### project
# import os
# def system():
#     if os.name=="nt":
#       os.system("cls")
#     else:
#        os.system("clear")

# def price_all_item(number_items,price):
#    return number_items*price
   
# while(True):
#     system()   
#     budget=int(input("Enter your spending budget"))
#     item_buy=input("Enter the item you want to buy:")  
#     number_items=int(input(f"How many {item_buy}s do you to buy?"))
#     price=int(input(f"Enter the price per {item_buy} :"))
#     all_price=price_all_item(number_items,price)
#     if all_price>budget:
#         print("Warning: Your purchase exceeds your daily budget!")
#     else:
#             print("Purchase successful! Enjoy your new item.")   
#     if input("Do you want to continue?y/n")!='y':
#         break


# function calling

# def tax_calculate(salary):
#     return salary*0.15

# def salary_calculate(result):
#     return result-(tax_calculate(salary))

# salary=float(input("Enter your base salary: "))
# bouns=float(input("How much bouns did you get? "))
# result=salary+bouns
# salary_after_tax=salary_calculate(result)
# print(f"Your salary after tax :{salary_after_tax}")



###################################################################################################################
# My project graduation from level 1

# import os
# import time
# import random
# import string

# def system():
#      if os.name=="nt":
#        os.system("cls")
#      else:
#         os.system("clear")

# def distribuation_cards():
#     cards=[11,2,3,4,5,6,7,8,9,10,10,10]
#     card=random.choice(cards)
#     return card

# def counting_cards(user_card,computer_card):
   
#    total_user=0
#    total_computer=0
#    for i in range(2):
#       total_user+=user_card[i]
#       total_computer+=computer_card[i]
#    if total_user==21:
#       print(f"Computer went over 21, you win✨")
#    elif total_computer==21:
#       print(f"Computer went 21, you loose😥")
#    else:
#       if(total_user>21):
#          if(11 in user_card):
            


        

   
# print("Choose a game to start............")
# print("""
# 1- Froggy
# 2- Twanty one
# 3- Snake
# --------- """ )
# game=input()
# print("Starting game............")
# time.sleep(3)
# system()
# user_card=[]
# computer_card=[]
# for _ in range(2):
#    user_card.append(distribuation_cards())
#    computer_card.append(distribuation_cards())

# print(counting_cards(user_card,computer_card))


# Function to calculate the area of a triangle
# def calculate_triangle_area(base, height):
#     area = 0.5 * base * height
#     return area

# # Input base and height from the user
# base = float(input("Enter the base value: "))
# height = float(input("Enter the height value: "))

# # Calculate the area
# area = calculate_triangle_area(base, height)

# # Display the result
# print(f"The area of the triangle is: {area}")
# w=int(input("Enter your Weight"))
# h=float(input("Enter your Height"))
# BMI=w/h**2
# if BMI<=18.4:
#   print("Unerweight")
# elif 18.4 > BMI < 24.9:
#     print("Normal")
# elif 25.0>BMI<39.9:
#       print("Overweight")
# elif BMI>=40.0:
#         print("Obese")

# n=input("Enter your number")
# count_even=0
# count_odd=0
# while n!=0:
#   if n%2==0:
#     count_even+=1
#   else:
#     count_odd+=1
#   n=input("Enter your number")

# print(f"count_even:",count_even)
# print(f"count_odd:",count_odd)
# names=["en","eb","al"]
# names.replace("_")
# print(names)


# nums=[1 ,2,3,4,5]
# for i in nums:
#     if i>nums[i]:
#         print ("the largest number is:",i



# list=input("Enter list")
# list.split()

# print(list)
# for i in range(len(list)):
#   if i==int(list[i]):
#    del list[i]

# p
#rint(list)


# list1=[1,2,3,4,5]
# list2=[6,7,5,3,4]
# for i in range(len(list1)):
#     if list1[i]==list2[i]:
#         print("true")

