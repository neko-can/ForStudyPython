
class TestInheritance:
    def __init__(self):
        ""
        print("継承元：init")

    def Main(self):
        ""

    def Main2(self):
        ""
        print("継承元：Main2")

class TestClass(TestInheritance):
    def __init__(self, arg1):
        """
        """
        print("コンストラクタ実行")
        print("コンストラクタ内：" + arg1)
        self.arg1 = arg1

    def Main(self):
        """
        """
        print("Main実行")
        print("Main内：" + self.arg1)


testclass = TestClass("test")
testclass.Main()
testclass.Main2()
