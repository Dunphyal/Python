a = 100
b = [1,2,3]

def f1():
    global a #global
    a=10
    b[0] = 6 #this will effect the global variable without the use of global
    print(a)
    print(b)

def f2():
    a = 50 # local
    print(a)

f1()
f2()
print(a)
print(b)

#1) Two types of scope - Global & local
#2) python function create local scopes
