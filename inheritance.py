class A:
    def funA(self):
        print("class A")
class B(A):#extending
    def funB(self):
        print("class B")
        
objA = A()
objB = B()
objB.funA()