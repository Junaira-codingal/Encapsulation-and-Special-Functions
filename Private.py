class myClass:
    
    __privateVar = 27;
    
    def __privateMeth(self):
        print("I'm inside class myClass")
        
    def hello(self):
        print(f"Private Variable value: {myClass.__privateVar} ")
        
foo = myClass()

foo.hello()
print(foo.__privateVar)
foo.__privateMeth()
