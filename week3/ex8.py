x = 1
y = 2

def name_x():
    global x  
    x = 2
    y = 3  
    print(x)  # x  = 2
    print(y)  # y  = 3


name_x()
print(x)   # x=1 when x is not a global variable；x=2 when x is a global variable


def name_y():
    y = 4  
    print(y)  # y = 4

name_y()
print(y)  # y