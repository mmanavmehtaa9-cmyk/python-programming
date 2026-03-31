def fun():
    print("This is fun()")

def disp():
    print("This is disp()")

def msg():
    print("This is mdg()")

lst = [fun, disp, msg]

for i in lst:
    i()
