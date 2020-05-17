print("Hello! My name is Aid.")
print("I was created in 2020.")
print('Please, remind me your name.')
your_name = str(input())
print('What a great name you have,'+ your_name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')
remainder_of_3 = int(input())
remainder_of_5 = int(input())
remainder_of_7 = int(input())
age = (remainder_of_3 * 70 + remainder_of_5 * 21 + remainder_of_7 * 15) % 105
print("Your age is"+ str(age) + "; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')
number = int(input())
counter = 0
while(counter <= number):
    print(str(counter) + "!")
    counter = counter + 1

print('Completed, have a nice day!')