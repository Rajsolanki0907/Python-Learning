
#Integer datatype
a = 10
b = 20
c = a + b 
print(c)
print(type(a))

#float datatype
a = 10.20
print(a)
print(type(a))


# String datatype
name  = "raj solanki"
name1  = 'raj solanki'
print(name)
print(name1)
print(type(name))

#boolean datatype
a = True
b = False
print(a)
print(b)
print(type(a))

#None datatype
d = None
print(d)
print(type(d))

#Python bool
print(bool("Hello")) #True
print(bool(15)) # True
x = "Hello"
y = 15
print(bool(x)) #True
print(bool(y)) #True
print(bool(" ")) #True
print(bool("")) #False
print(bool(0)) # False
print(bool(None)) # False
print(bool(())) # empty tuple,list , dict all returns false 


class myclass():
    def __len__(self):
        return 0

myObj = myclass()
print("class obj using _len_ function")
print(bool(myObj))    
