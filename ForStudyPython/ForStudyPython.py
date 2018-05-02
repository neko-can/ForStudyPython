print("Hello world!")
print(2+3)
print(2.+3)
print(2**3)
print("test\ntest")
print(type("test"))

"""
メモ欄
"""
#コメント

inputResult = input("入力欄：")
print("入力した文字は「"+inputResult+"」です。")

def Test(maxNumber, result=1):
    if(maxNumber > 1):
        result *= maxNumber
        maxNumber -= 1
        result = Test(maxNumber, result)

    return result

print("5! = " + str(Test(5)))

#デリゲート
testDel = Test
print("9! = " + str(testDel(9)))

try:
    num1 = 1
    num2 = "test"
    print(num1/num2)
    print("実行されない")
except ZeroDivisionError:
    print("ZeroDivisonError")
except TypeError:
    print("TypeError")
except:
    print("except only")
finally:
    print("finally")
