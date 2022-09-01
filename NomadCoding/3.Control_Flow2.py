from random import randint

print("Welcome to Python casino!")
user_choice = int(input("Choeese number : (1-50"))

pc_choice = randint(1,50) # I imported this

while user_choice != pc_choice:
  if user_choice == pc_choice:
    print("You won.")
  elif user_choice > pc_choice:
    print("Lower!")
  elif user_choice < pc_choice:
    print("Higher!")
  user_choice = int(input("Choeese number :"))
