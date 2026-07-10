# FizzBuzz: Print numbers from 1 to 50. For multiples of 3 print "Fizz", for multiples of 5 print "Buzz", and for multiples of both print "FizzBuzz".

for i in range(1,50):
    if i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    elif i%3==0 or i%5==0:
        print('FizzBuzz')