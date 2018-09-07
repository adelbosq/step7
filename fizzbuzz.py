def fizzBuzz1(n_max):
    "Simple and direct"
    for n in range(1,n_max+1):
        if (n % 15) == 0:
            print "FizzBuzz",
        elif (n % 3) == 0:
                print "Fizz",
        elif (n % 5) == 0:
            print "Buzz",
        else:
            print n,

def fizzBuzz2(n_max):
    "Some fancy language features"
    for n in range(1, n_max+1):
        print "Fizz" * (n % 3 == 0) + "Buzz" * (n % 5 == 0) or n,

def fizzBuzz3(n_max):
    assert isinstance(n_max, (int, long))
    for n in range(1, n_max + 1):
        divisible_by_5 = (n % 5) == 0
        if (n % 3) == 0:
            if divisible_by_5:
                print "FizzBuzz",
            else:
                print "Fizz",
        elif divisible_by_5:
            print "Buzz",
        else:
            print n,
