class NewClass:
    def __init__(self):
        self.x = 10

    def printnew(self):
        return "newClass"


class ChildClass(NewClass):
    pass


newObj = NewClass()
print(newObj.printnew())
print(newObj.x)

newChild = ChildClass()
print(newChild.x)


