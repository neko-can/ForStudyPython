class TestClass:
    main = None
    main = "test"
    
    def __init__(self):
        print("test constracter")

    def Main(self):
        print(self.main)
        self.main = "main"

    def ChangeMain():
        TestClass.main = "ChangeMain"


print(TestClass.main)
TestClass.ChangeMain()
print(TestClass.main)