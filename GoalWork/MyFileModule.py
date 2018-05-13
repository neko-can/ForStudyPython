import numpy as np
from MyCommonModule import *

class FileModule:
    def __init__(self, fileNameListClass, fileClass):
        self.CM = CommonModule()
        self.fileNameListClass = fileNameListClass
        self.fileClass = fileClass
        self.NGList = [self.fileNameListClass.fileName, " ", "\\", "/", ":", "*", "?", "\"", "<", ">", "|"] #名前を".npy"変換した後にチェック

    def NewName(self, fileName):
        fileName = self.AddNPY(fileName) #.npy拡張子付与
        fileName = self.CheckFileName(fileName) #適切か判定
        return fileName

    def AddNPY(self, fileName):
        if fileName[-4:] != ".npy":
            fileName += ".npy"

        return fileName

    def CheckFileName(self, fileName):
        if self.IsInNGList(fileName):
            print("ファイル名が不適切です。")
            fileName = "Untitled.npy"

        #変数リセット
        newFileName = fileName
        self.fileClass.noSame = 0
        while newFileName in self.fileNameListClass.fileNameArray:
            print("ファイルが既に存在します。")
            self.fileClass.noSame += 1
            newFileName = fileName[:-4] + str(self.fileClass.noSame) + fileName[-4:]

        return newFileName

    def IsInNGList(self, fileName):
        result = False
        for ngstr in self.NGList:
            if ngstr in fileName:
                result = True

        return result

    def AddFileNameList(self, fileName):
        if not(fileName in self.fileNameListClass.fileNameArray):
            self.fileNameListClass.fileNameArray = np.append(self.fileNameListClass.fileNameArray, fileName)

    def AddFinish(self):
        self.IsInAddMode = False
    def AddShowData(self):
        print(self.fileClass.dataDict[self.fileClass.targetListName1])
        if(self.fileClass.targetListName2 != None):
            print(self.fileClass.dataDict[self.fileClass.targetListName2])

    def ShowFileArray(self):
        self.fileNameListClass.Load()
        self.CM.printWithNumber(self.fileNameListClass.fileNameArray)
        self.CM.PrintLog("ファイルリスト表示完了しました。")

class FileClass:
    def __init__(self, fileNameListClass):
        self.FM = FileModule(fileNameListClass, self)
        self.fileNameListClass = fileNameListClass
        self.fileName = self.FM.NewName("Untitled.npy")
        self.dataDict = {"array1" : np.array([])}
        self.targetListName1 = [*self.dataDict][0]
        self.targetListName2 = None
        self.noSame = 0

    def Open(self, fileName):
        try:
            self.dataDict = np.load(fileName)[()]
            self.fileName = fileName
            self.targetListName1 = [*self.dataDict][0]
            self.targetListName2 = None
            self.noSame = 0

        except:
            fileList = self.fileNameListClass.fileNameArray.tolist()
            fileList.remove(fileName)
            self.fileNameListClass.fileNameArray = np.array(fileList)
            print("ファイルが存在しません。\nリストから名前を削除した。")
            self.fileNameListClass.Save()

    def QuestionString(self):
        return self.fileName + " - " + self.targetListName1 + " : "

class FileNameListClass:
    def __init__(self):
        self.fileName = "fileNameList.npy"
        self.fileNameArray = np.array([])
        self.Load()

    def Load(self):
        try:
            self.fileNameArray = np.load(self.fileName)
        except FileNotFoundError:
            print(str(self.fileName) + "が見つかりませんでした。\n新しくファイルを生成します")
            self.Save()

    def Save(self):
        np.save(self.fileName, self.fileNameArray)
        print(str(self.fileName) + "の保存が完了しました。")

class MenuModule:
    def __init__(self, MyAnalysis):
        self.fileClass = MyAnalysis.fileClass
        self.fileNameListClass = MyAnalysis.fileNameListClass
        self.CM = CommonModule()
        self.FM = FileModule(self.fileNameListClass, self.fileClass)
        
        #ver3
        self.OpenMode = OpenMode(MyAnalysis, question="ファイルを開く : ")

    def Save(self):
        self.FM.AddFileNameList(self.fileClass.fileName)
        np.save(self.fileNameListClass.fileName, self.fileNameListClass
                .fileNameArray)
        np.save(self.fileClass.fileName, self.fileClass.dataDict)
        print("上書き保存しました。")

    def SaveAsNew(self):
        print("新規保存しました。")

    def OpenFile(self):
        self.fileNameListClass.Load()
        self.Opencmd.ShowCommand()
        self.Opencmd.Main()

    def NewFile(self):
        print("新しいファイルを作成しました。")

    def AddData(self):
        #変数リセット
        self.FM.IsInAddMode = True

        while self.FM.IsInAddMode:
            addData = input("データ入力 : ")
            if self.CM.IsFloat(addData):
                addData = float(addData)
                self.fileClass.dataDict[self.fileClass.targetListName1] = np.append(self.fileClass.dataDict[self.fileClass.targetListName1], addData)
                self.CM.PrintLog("データを追加しました。")
            if addData in self.FM.addCommand.keys():
                self.FM.addCommand[addData]()

    def ShowData(self):
        print(self.fileClass.dataDict[self.fileClass.targetListName1])
        self.CM.PrintLog("データ表示完了しました。")

    def ShowFileList(self):
        print(self.fileNameListClass.fileNameArray)

    def ShowArrayList(self):
        print([*self.fileClass.dataDict])

    def RenameFile(self):
        self.fileClass.fileName = self.FM.NewName(input("ファイル名変更 : "))
        self.CM.PrintLog("ファイルの名前を変更しました。")


    def RenameArray(self):
        ""

#ver3
class FileMode(OriginalClass):
    def __init__(self, MyAnalysis, **kwargs):
        self.CM = CommonModule()
        self.MyAnalysis = MyAnalysis
        self.option = {"funclist" : {},
                       "phaselist" : []}
        self.option.update(kwargs)

        self.funclist = {"showcommand" : self.ShowCommand}
        self.phaselist = self.option["phaselist"]
        self.fileclass = self.MyAnalysis.fileClass

        CommonModule.UpdateWithoutOverride(self.funclist, self.option["funclist"])

        #追加コマンド → filename, arrayname

    def Main(self):
        command = input(self.fileclass.QuestionString())
        if command in [*self.funclist]:
            self.funclist[command]()
        elif command in self.phaselist:
            self.ChangePhase(command)

class OpenMode(OriginalClass):
    def __init__(self, MyAnalysis, **kwargs):
        self.CM = CommonModule()
        self.MyAnalysis = MyAnalysis
        self.fileclass = self.MyAnalysis.fileClass
        self.filenamelistclass = self.MyAnalysis.fileNameListClass
        self.option = {"question" : "command : ",
                       "funclist" : {},
                       "phaselist" : []}
        self.option.update(kwargs)

        self.funclist = {"showcommand" : self.ShowCommand,
                         "cancel" : self.Cancel}
        self.phaselist = self.option["phaselist"]

        CommonModule.UpdateWithoutOverride(self.funclist, self.option["funclist"])
        self.question = self.option["question"]

    def Main(self):
        self.isPlay = True
        self.ShowCommand()
        while self.isPlay:
            command = input(self.question)
            if command in [*self.funclist]:
                self.funclist[command]()

            if command in self.filenamelistclass.fileNameArray:
                self.fileclass.Open(command)
                self.Cancel()

    def Cancel(self):
        self.isPlay = False

    def ShowCommand(self):
        print(self.phaselist)
        print([*self.funclist])
        print(self.filenamelistclass.fileNameArray)

class AddDataMode(OriginalClass):
    def Main(self):
        ""