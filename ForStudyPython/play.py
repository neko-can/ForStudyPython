a = 1

def ChangeNumber(a):
    b = a
    a = 99

    print("{before}から{after}に変更しました。".format(before=b, after=a))

ChangeNumber(a)

print(a) #ここで何が表示されるでしょーか？

print("-------------------クラス参照型--------------------")

class MyClass:
    def Main(self):
        self.a = 1

myClass = MyClass()
myClass.Main()

otherClass = myClass
otherClass.a = 99

print("myClass.a = {a}".format(a = myClass.a)) #ここで何が表示されるでしょうか
print("myClass's id = {myClassID}\notherClass's id = {otherClassID}".format(myClassID = id(myClass), otherClassID=id(otherClass)))

del a
del MyClass, myClass, otherClass
print("-----------------平文におけるメモリ確保状況--------------")


class MyClass:
    def Main(self):
        self.a = a

    def Print(self):
        print(self.a)
myClass = MyClass()
a = 1
myClass.Main()
myClass.Print()

print("---------------pythonの内部実行順序-------------")
del a, MyClass, myClass

b = 1
class MyClass:
    a = b
    def Main():
        print(MyClass.a)
print(MyClass.a)
MyClass.Main()

print("------------delegate入門--------------")

def Function():
    print("休みだ！"*3)

a = Function
a()