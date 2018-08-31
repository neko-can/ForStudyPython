import statistics

import week4Base

class SampleClass(week4Base.SampleClass):
    def __init__(self):
        super().__init__()

        self.windowSentences = []

        self.FileEditer = FileEditer(self)
        self.AnalizeTool = AnalizeTool(self)

    def SubstitutionText(self):
        noOfResultLength = self.resultText.count("\n")
        if self.noOfWidth - noOfResultLength > 0:
            self.resultText += "\n" * (self.noOfHeight - noOfResultLength)
        nowWindowText = self.WindowText.format(
            title=self.titleText,
            mode=self.modeText,
            oldCmd=self.oldCmdText,
            result=self.resultText,
            end=self.endText
            )
        self.nowWindowText = nowWindowText
        self.nowWindowText = self.nowWindowText.replace("  ", "")
        self.nowWindowText = self.nowWindowText.strip("\n")
    def SplitText(self):
        #文章のリスト化
        self.windowSentences = self.nowWindowText.split("\n")
    def AdjustSentence(self):
        self.windowSentences[0] = "〇{}〇\n".format(self.windowSentences[0])
        self.windowSentences[-1] = "〇{}〇".format(self.windowSentences[-1])
        self.windowSentences[1:-1] = ["｜"+sentence+" "*Helper.CalcDifferenceLen(" "*self.noOfWidth, sentence)+"||\n" for sentence in self.windowSentences[1:-1]]
    def ConnectText(self):
        result = ""
        for sentence in self.windowSentences:
            result += sentence
        self.nowWindowText = result

class FileEditer(week4Base.FileEditer):
    def __init__(self, MainClass):
        super().__init__(MainClass)

    #load
    def LoadCollection(self):
        self.file = open(self.fileName, "r")
        allCollectionsText = self.file.readlines()
        allCollectionsText = list(map(lambda collection:collection.replace("\n", ""), allCollectionsText))
        allCollectionsText = list(map(lambda collectionText:collectionText.split(","), allCollectionsText))

        allCollections = []
        for collection in allCollectionsText:
            allCollections.append([])
            for data in collection:
                try:
                    allCollections[-1].append(int(data))
                except ValueError:
                    allCollections[-1].append(data)
        self.allCollections = allCollections
        self.file.close()

        self.oldCmdText = "ロードが完了しました。"

    #select menu
    def SelectMenuCommandAction(self):
        commandIndex = int(input("{} : menu >> ".format(self.dataCollection1[0])))
        if commandIndex == 0:
            self.Action = self.Back
        elif commandIndex == 1:
            self.Action = self.ChangeData
        elif commandIndex == 2:
            self.Action = self.Save
        elif commandIndex == 3:
            self.Action = self.Write
        elif commandIndex == 4:
            self.Action = self.Delete
        elif commandIndex == 5:
            self.Action = self.Select
        elif commandIndex == 6:
            self.Action = self.NewCollection
    def SelectMenuSetWindow(self):
        #画面設定
        self.subText = self.dataText.format(
            data1name=self.dataCollection1[0],
            data1=self.dataCollection1[1:],
            data2name=self.dataCollection2[0],
            data2=self.dataCollection2[1:]
            )
        self.resultText = self.fileMenuText.format(subText=self.subText)
        self.resultText = self.resultText.replace("  ", "")
    #save
    def ReflectDataForSave(self):
        collectionNameList = list(map(lambda collection : collection[0], self.allCollections))
        try:
            dataIndex = collectionNameList.index(self.dataCollection1[0])
            self.allCollections[dataIndex] = self.dataCollection1
        except ValueError:
            self.allCollections.append(self.dataCollection1)
    def MakeSentenceForSave(self):
        alldataText = ""
        for collection in self.allCollections:
            collectionText = [str(i) for i in collection]
            alldataText += ",".join(collectionText)+"\n"
        return alldataText
    def WriteInFileForSave(self, alldataText):
        #書き込み
        self.file.write(alldataText)

    #write
    def InputKey(self):
        #入力
        return input("{} : No.{} >> ".format(self.dataCollection1[0], len(self.dataCollection1)))
    def CommandAction(self, command):
        if command == "save":
            self.SaveFunc()
            self.oldCmdText = "保存が完了しました。"
        elif command == "back":
            if len(self.dataCollection1) > 1:
                del self.dataCollection1[-1]
        elif command == "end":
            self.oldCmdText = "書き込み完了"
            self.Action = self.SelectMenu
    def AddData(self, command):
        try:
            self.dataCollection1.append(float(command))
        except ValueError:
            pass
    def ShowEnrouteData(self):
        collectionText = [str(i) for i in self.dataCollection1]
        text = "{} : {}".format(collectionText[0], ", ".join(collectionText[1:]))
        self.resultText = self.writeText.format(data=text)

    #delete
    def DeleteShowData(self):
        collectionText = [str(data) for data in self.dataCollection1]
        text = "{} : {}".format(self.dataCollection1[0], self.dataCollection1[1:])
        self.resultText = text
    def CheckMessage(self):
        answer = input("本当に削除しますか(yes or no) >> ")
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            return False
    def DeleteFromAllCollections(self):
        collectionNameList = list(map(lambda collection : allCollections[0], self.allCollections))
        try:
            dataIndex = collectionNameList.index(self.dataCollection1[0])
            del self.allCollections[dataIndex]
        except ValueError:
            pass

    #select
    def SelectShowAllCollection(self):
        collectionNameList = list(map(lambda collection : collection[0], self.allCollections))
        text = ""
        for i in range(len(collectionNameList)):
            text += "{index} : {data}\n".format(index=i, data=collectionNameList[i])
        self.resultText = text
    def InputCollectionIndex(self):
        index = int(input("Collection Number : "))
        return index
    def SelectToFloatList(self, targetList):
        result = targetList
        result[1:] = [float(i) for i in result[1:]]
        return result

    #new collection
    def InputForNewCollection(self):
        name = input("new name >> ")
        return name
    def ReflectToNewCollection(self, name):

        self.dataCollection1 = [name]

class AnalizeTool(week4Base.AnalizeTool):
    def __init__(self, MainClass):
        super().__init__(MainClass)

    #平均
    def CalcAverage(self):
        meanX = statistics.mean(self.dataCollectionX[1:])
        meanY = statistics.mean(self.dataCollectionY[1:])
        return [meanX, meanY]

    def CalcDispersion(self):
        dispersionX = statistics.variance(self.dataCollectionX[1:])
        dispersionY = statistics.variance(self.dataCollectionY[1:])
        return [dispersionX, dispersionY]

    def CalcStandardDeviation(self):
        stdevX = statistics.stdev(self.dataCollectionX[1:])
        stdevY = statistics.stdev(self.dataCollectionY[1:])
        return [stdevX, stdevY]

    def CalcLeastSquaresMethod(self):
        a, b, sigmaA, sigmaB = 0, 0, 0, 0

        X = self.dataCollectionX[1:]
        Y = self.dataCollectionY[1:]
        squareX = [i**2 for i in X]
        squareY = [i**2 for i in Y]
        multi = sum(list(map(lambda x, y:x*y, X, Y)))
        n = len(X)

        sumX = sum(X)
        sumY = sum(Y)
        sumSquareX = sum(squareX)
        sumSquareY = sum(squareY)

        a = (sumY*sumSquareX - sumX*multi) / (n*sumSquareX - sumX**2)
        b = (n*multi - sumY * sumX) / (n*sumSquareX - sumX**2)

        deviation = list(map(lambda x, y:(y - (a + b*x))**2, X, Y))
        sigmaY = (sum(deviation) / (n-2))**(1/2)

        sigmaA = sigmaY * (sumSquareX/(n*sumSquareX - sumX**2))**(1/2)
        sigmaB = sigmaY*(n/(n*sumSquareX - sumX**2))**(1/2)

        a = round(a, 4)
        b = round(b, 4)
        sigmaA = round(sigmaA, 4)
        sigmaB = round(sigmaB, 4)

        return [a, b, sigmaA, sigmaB]

class Helper(week4Base.Helper):
    def __init__(self, MainClass):
        super().__init__(MainClass)

SampleClass().Main()