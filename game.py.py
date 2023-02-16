# this program demonstrates a guessing game
# get user name
name=input('What is your name?  ')
print('Hello there ' + name +'!')
# generate a random number
from random import randint
random_num=randint(10, 50)
# input random no
counter=0
while counter < 5:
   num=eval(input('Enter number : '))
   counter+=1 # same as counter=counter+1
   if num<random_num:
      print('Number is low')
   elif num>random_num:
      print('Number is high')
   elif num==random_num:
      break #breaks the loop
print('Game over!')
if num==random_num:
   print('You win!')
else:
   print('You lost! The correct number is ')
   print(random_num)

# generate a random no.
# check if the input is equal to generated no
# using a while loop,check if input is equal to generated no.