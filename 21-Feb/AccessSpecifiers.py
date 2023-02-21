class Test:
    var1 = None
    _var2 = None
    __var3 = "20"

    def __init__(self):
        pass


t = Test()
print(t.__var3)
