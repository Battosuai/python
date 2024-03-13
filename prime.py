def isPrime(number):
    prime = True
    if number == 1:
        return prime
    
    for i in range(2,number):
        print(i)
        if number%i==0:
            prime = False
            return prime

    return prime
    
try:
    value = int(input("Type a number?\n"))
    
    print(isPrime(value))

except ValueError:
    print("You have to give a number")    
