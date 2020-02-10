""" Floating Prime """

def main():
    """ main function """
    while True:
        num = float(input())
        if(num == 0.0):
            break
        else:
            if(10 >= num >= 1):
                if((function(num) == True) or (function(num*10) == True) or (function(num*100) == True) or (function(num*1000) == True)):
                    print("TRUE")
                else:
                    print("FALSE")
            else:
                print("FALSE")


def function(n):
    if (int(n) > 1):
        for i in range(2, int(n)):
            if (int(n) % i == 0):
                return False
        return True
    else:
        return False
main()