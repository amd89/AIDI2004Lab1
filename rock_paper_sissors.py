import random

print('Lets play rock, paper, sissors')
choice = int(input('please make you choice 1 for rock, 2 for paper, 3 for sissors:'))
comp_choice = random.randint(1, 3)
print(comp_choice)
if(choice == comp_choice):
    print('DRAW')
elif(choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
    print('YOU LOSE')
else:
    print('YOU WIN')

