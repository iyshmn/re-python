class A:
    __a = None
    __b = None
    def __init__(self,a,b):
        self.__a=a
        self.__b=b
    def sum(self):
         sum=self.__a+self.__b
         return sum
obj = A(12,13)
print(obj.sum())