for i in range(1, 101):
    variablePara3 = i/3
    variablePara5 = i/5
    
    if (i % 3 == 0 and i % 5 == 0):
        print('FizzBuzz');
    elif(i % 3 == 0):
        print('Fizz');
    elif(i % 5 == 0):
        print('Buzz');
    else:
        print(i)
