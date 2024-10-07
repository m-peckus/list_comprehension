class parent:
    def select(self,*items):
        selected_items = [int for int in items if int < 10]
        print(selected_items)
x = parent()    
#x.select(11,23,4,55)

def square_rt(x):
    answer = 0
    while answer*answer < x:
        answer += 1
    if answer*answer != x:
        print('not a square')
    else:
        print(answer)
#square_rt(16)

def find_factorial(x):
    factorial = 1
    i = 1
    for i in range(i, x+1):
        factorial *= i
    print(factorial)
#find_factorial(5)

def find_dividers(x):
    result = ()
    for i in range(1, x):
        if x % i == 0:
            result += (i,)
    print(result)
#find_dividers(10)