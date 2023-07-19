def outer(x):
    def inner(y):
        def sup(z):
            return x+y+z
        return sup
    return inner
ins = outer(5)
sec = ins(6)
third = sec(7)
print(third)

def make_pretty(func):
    def inner():
        print("i got decorated")
        func()
    return inner
@make_pretty
def ordinary():
    print("i am ordinary")
# call = make_pretty(ordinary)
# call()
ordinary()