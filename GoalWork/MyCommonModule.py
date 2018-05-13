"""
機能
・分析補助モジュール記述
・プロパティを持つinput
"""

import numpy as np
import sys

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

    def IsFloat(self, str):
        result = None

        try:
            resultVariable = float(str)
            result = True
        except ValueError:
            result = False

        return result

    def inputInOption(self, str, option):
        result = input(str)
        if result not in option:
            print("入力ミスです。")
            result = self.inputInOption(str, option)

        return result

    def printList(self, targetlist):
        print(targetlist) #後で実装

    def printWithNumber(self, ndarray):
        noline = ndarray.shape[0]
        for i in range(noline):
            print(str(i) + ". " + str(ndarray[i]))

    #ver3
    def UpdateWithoutOverride(originaldic, adddic):
        CommonModule.CheckKeyDuplication(originaldic, adddic, qstr="存在しているキーが含まれています。")
        originaldic.update(adddic) #dicは参照型

    def CheckKeyDuplication(dic1, dic2, qstr="キーが重複しています。"):
        for key in [*dic1]:
            if key in [*dic2]:
                raise KeyError(qstr)


class CommandModule:
    def __init__(self, **kwargs):
        
        self.option = {"commandquestion" : "command : ",
                       "cancelstr" : "キャンセルされました。",
                       "cancelcommand" : "cancel",
                       "cancelfunc" : self.Cancel,
                       "subcommand" : {},
                       "transcommand" : {}}
        self.option.update(kwargs)
        
        self.CM = CommonModule()
        
        self.__isPlay = True
        self.__subcommand = {"showcommand" : self.ShowCommand}
        self.__transcommand = {self.option["cancelcommand"] : self.option["cancelcommand"]}
        self.commandquestion = self.option["commandquestion"]
        self.cancelstr = self.option["cancelstr"]
        self.subcommand = self.option["subcommand"]
        self.transcommand = self.option["transcommand"]

        self.UpdateWithoutOverride(self.__subcommand, self.subcommand) 
        self.UpdateWithoutOverride(self.__transcommand, self.transcommand)
        self.CheckKeyDuplication(self.__subcommand, self.__transcommand)

    def UpdateWithoutOverride(self, originaldic, adddic):
        self.CheckKeyDuplication(originaldic, adddic, qstr="存在しているキーが含まれています。")
        originaldic.update(adddic) #dicは参照型

    def CheckKeyDuplication(self, dic1, dic2, qstr="キーが重複しています。"):
        for key in [*dic1]:
            if key in [*dic2]:
                raise KeyError(qstr)

    def Cancel(self):
        print(self.cancelstr)
        
    def ShowCommand(self):
        self.CM.printList([*self.__subcommand])
        self.CM.printList([*self.__transcommand])

    def Main(self):
        self.__isPlay = True
        self.command = None

        while self.__isPlay:
            self.command = input(self.commandquestion)

            if self.command in [*self.__transcommand]:
                self.__transcommand[self.command]()
                self.__isPlay = False
            elif self.command in [*self.__subcommand]:
                self.__subcommand[self.command]()

#ver3
class OriginalClass:
    def __init__(self, MyAnalysis, **kwargs):
        self.CM = CommonModule()
        self.MyAnalysis = MyAnalysis
        self.option = {"question" : "command : ",
                       "funclist" : {},
                       "phaselist" : []}
        self.option.update(kwargs)

        self.funclist = {"showcommand" : self.ShowCommand,
                         "end" : self.EndProgram}
        self.phaselist = self.option["phaselist"]

        CommonModule.UpdateWithoutOverride(self.funclist, self.option["funclist"])
        self.question = self.option["question"]

    def Main(self):
        command = input(self.question)
        if command in [*self.funclist]:
            self.funclist[command]()
        elif command in self.phaselist:
            self.ChangePhase(command)

    def ShowCommand(self):
        print(self.phaselist)
        print([*self.funclist])

    def EndProgram(self):
        self.MyAnalysis.isPlay = False
        print("プログラムを終了します。。。")
    
    def ChangePhase(self, nextphase):
        self.MyAnalysis.MainClass = self.MyAnalysis.AllMode[nextphase]
        self.MyAnalysis.MainClass.ShowCommand()
