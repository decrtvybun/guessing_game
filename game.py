# this program demonstrates a guessing game
# get user name
name=input('What is your name?  ')
print('Hello there ' + name +'!')
# generate a random number
from random import randint
num=randint(10, 50)
# input random no
counter=0
while counter < 5:
   num=eval(input('Enter number : '))
# generate a random no.
# check if the input is equal to generated no
# using a while loop,check if input is equal to generated no.