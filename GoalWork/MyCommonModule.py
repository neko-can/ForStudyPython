"""
機能
・分析補助モジュール記述
・プロパティを持つinput
"""

import numpy as np

class CommonMainModule:
    def __init__(self, MyAnalysisID):
        self.MyAnalysis = MyAnalysisID
        self.exceptRoopList = ["end"]

    def ChangeMenu(self, keyString):
        "mainとmenuの変更"
        self.MyAnalysis.main = self.MyAnalysis.mainMenu[keyString]
        if(keyString != "end"):
            self.MyAnalysis.mainMenu = self.MyAnalysis.menuList[keyString]
            self.ShowMenu()

    def InputChangeMenu(self, questionString = "メニュー選択 : "):
        
        option = input(questionString + self.MyAnalysis.fileClass.QuestionString())

        if option in self.MyAnalysis.mainMenu["main"].keys():
           self.MyAnalysis.main = self.MyAnalysis.mainMenu["main"][option]
           self.MyAnalysis.mainMenu = self.MyAnalysis.menuList[option]
           self.ShowMenu()

        elif option in self.MyAnalysis.mainMenu["sub"].keys():
             self.MyAnalysis.mainMenu["sub"][option]()
             if option != "end":
                 self.InputChangeMenu(questionString)
        else:
             self.InputChangeMenu(questionString)

    def ShowMenu(self):
        print(self.MyAnalysis.mainMenu["main"].keys())
        print(self.MyAnalysis.mainMenu["sub"].keys())

class CommonModule:
    def __init__(self):
        self.NGList = np.array([]) #fileNameListを追加する

    def PrintLog(self, log):
        print(" - " + str(log))

    def InputFloat(str):
        inputValue = input(str)
        try:
            inputValue = float(inputValue)
        except ValueError:
            InputFloat(str)

        return inputValue

    def IsFloat(self, str):
        result = None

        try:
            resultVariable = float(str)
            result = True
        except ValueError:
            result = False

        return result