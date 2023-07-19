class Human:
    x = None
    def hello(self):
        print("i am human")
class Boy(Human):
    y=None
    def hello(self):
        print("i am a boy")
class Girl(Human):
    def hello(self):
        print("i am girl ")
objH = Human()
objH.hello() 
objH= Boy()
objH.hello()
objH.x=12
