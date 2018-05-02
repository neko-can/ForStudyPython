import numpy as np
import MyCommonModule as CM

class FileModule:
    def __init__(self, fileNameListClass, fileClass):
        self.CM = CM.CommonModule()
        self.fileNameListClass = fileNameListClass
        self.fileClass = fileClass
        self.NGList = [self.fileNameListClass.fileName, " ", "\\", "/", ":", "*", "?", "\"", "<", ">", "|"] #名前を".npy"変換した後にチェック
        self.openCommand = {"cancel" : self.OpenCancel,
                            "showFileList" : self.ShowFileArray,
                            "showCommand" : self.OpenShowCommand}
        self.IsInOpenMode = True

        self.addCommand = {"finish" : self.AddFinish,
                           "showData" : self.AddShowData}
        self.IsInAddMode = True

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

    def OpenCancel(self):
        self.IsInOpenMode = False
    def OpenShowCommand(self):
        print(self.openCommand.keys())

    def AddFinish(self):
        self.IsInAddMode = False
    def AddShowData(self):
        print(self.fileClass.dataDict[self.fileClass.targetListName1])
        if(self.fileClass.targetListName2 != None):
            print(self.fileClass.dataDict[self.fileClass.targetListName2])

    def ShowFileArray(self):
        self.fileNameListClass.Load()
        print(self.fileNameListClass.fileNameArray)
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

            print("ファイルを開きました。")
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
    def __init__(self, fileClass, fileNameListClass):
        self.fileClass = fileClass
        self.fileNameListClass = fileNameListClass
        self.CM = CM.CommonModule()
        self.FM = FileModule(fileNameListClass, fileClass)
        
    def Save(self):
        self.FM.AddFileNameList(self.fileClass.fileName)
        np.save(self.fileNameListClass.fileName, self.fileNameListClass
                .fileNameArray)
        np.save(self.fileClass.fileName, self.fileClass.dataDict)
        self.CM.PrintLog("上書保存しました。")

    def SaveAsNew(self):
        self.CM.PrintLog("新規保存しました。")

    def OpenFile(self):
        #変数リセット
        self.fileNameListClass.Load()
        self.FM.OpenShowCommand()
        self.FM.IsInOpenMode = True

        while self.FM.IsInOpenMode:
            command = input("ファイルを開く : ")

            if command in self.FM.openCommand.keys():
                self.FM.openCommand[command]()

            if command in self.fileNameListClass.fileNameArray:
                self.fileClass.Open(command)
                self.FM.IsInOpenMode = False

    def NewFile(self):
        self.CM.PrintLog("新しいファイルを作成しました。")

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

    def DeleteData(self):
        self.CM.PrintLog("データを削除しました。")

    def DeleteArray(self):
        self.CM.PrintLog("配列を削除しました。")

    def ReplaceData(self):
        self.CM.PrintLog("データを並べ替えました。")

    def ShowData(self):
        print(self.fileClass.dataDict[self.fileClass.targetListName1])
        self.CM.PrintLog("データ表示完了しました。")

    def ShowArrayList(self):
        ""

    def ShowFileArray(self):
        self.fileNameListClass.Load()
        print(self.fileNameListClass.fileNameArray)
        self.CM.PrintLog("ファイルリスト表示完了しました。")

    def RenameFile(self):
        self.fileClass.fileName = self.FM.NewName(input("ファイル名変更 : "))
        self.CM.PrintLog("ファイルの名前を変更しました。")

    def RenameArray(self):
        ""

    def SelectArray(self):
        ""
