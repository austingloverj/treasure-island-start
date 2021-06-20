print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

choice1 = input("You come upon a fork in the road, do you go left or right? Type L for left and R for right\n")

if choice1 == "R":
  print("You have fallen into a pit of highly venomus snakes. Game over.")
else:
  choice2 = input("You come upon a lake, do you wait for a boat or go for a swim? Type 1 for wait and 2 for swim\n")
  if choice2 == "2":
    print("You are quickly snatched by a family of aligators")
  else: 
    choice3 = input("You are picked up on a boat by a local who took you to the island that supposedly holds the treasure. You land on the beach and start digging until you come across 3 boxes. One red, one yellow and one blue. The local yells at you from the boat to only open one because opening more would cause you to be cursed. Which would you choose? Type B for blue, Y for yellow and r for red.\n")
    if choice3 == "B":
      print("The box is empy. You have to re-bury the treasure and walk away")
    elif choice3 == "Y":
      print("The box contains a curse. You will be haunted by demons for the rest of your life.")
    else:
      print("You found the treasure! You're set for life.")





  