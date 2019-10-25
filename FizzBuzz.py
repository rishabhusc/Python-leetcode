n=15

def logic(n):
    ls=[]


    def fizzbuzz(i):
        if i%3==0 and i%5==0:
            return "FizzBuzz"
        elif i%3==0:
            return "Fizz"
        elif i%5==0:
            return "Buzz"
        else:
            return i

    for i in range(1, n + 1):
        ls.append(fizzbuzz(i))
    return ls
print(logic(15))