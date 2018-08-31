import os
import unicodedata
import copy

class SampleClass:
    def __init__(self):
        #ウィンドウ設定
        self.noOfHeight = 20
        self.noOfWidth = 80

        self.enable = True
        self.WindowText = """
        {title:-^80}
        {mode}
        old cmd : {oldCmd}
        {result}
        {end:=>80}
        """

        self.titleText = "Sample Class"
        self.modeText = "モード未選択"
        self.oldCmdText = "なし"
        self.resultText = ""
        self.endText = "End"

        self.previousWindowText = None
        self.nowWindowText = None
        self.updateWindowSwitch = False
        self.Action = self.Start

        #データ
        self.defaultCollection = ["default collection"]
        self.dataCollection1 = []
        self.dataCollection2 = []

        #モード選択
        self.selectModeText = """
        モード選択
        0 : ファイルモード
        1 : データ分析モード
        """

        #外部実装
        self.Helper = None
        self.FileEditer = None
        self.AnalizeTool = None

    def Start(self):
        self.AutoDataSelect()
        self.Action = self.SelectMode

    def Main(self):
        while self.enable:

            if self.Action != None:
                self.Action()

            self.SetWindow()
            if self.nowWindowText != self.previousWindowText or self.updateWindowSwitch:
                os.system("cls")
                print(self.nowWindowText)
            self.previousWindowText = self.nowWindowText

    def SetWindow(self):
        self.SubstitutionText()
        self.SplitText()
        self.AdjustSentence()
        self.ConnectText()
    def SubstitutionText(self):
        pass
    def SplitText(self):
        pass
    def AdjustSentence(self):
        pass
    def ConnectText(self):
        pass

    def SelectMode(self):
        self.resultText = self.selectModeText
        self.Action = self.SelectModeUpdate
    def SelectModeUpdate(self):
        modeIndex = int(input("{} : mode >> ".format(self.dataCollection1[0])))

        if modeIndex == 0:
            self.Action = self.FileEditer.Main
        elif modeIndex == 1:
            self.Action = self.AnalizeTool.Main
    def AutoDataSelect(self):
        if self.dataCollection1 != None:
            self.dataCollection1 = copy.deepcopy(self.defaultCollection)
        if self.dataCollection2 != None:
            self.dataCollection2 = copy.deepcopy(self.defaultCollection)

class FileEditer:
    def __init__(self, MainClass):
        self.MainClass = MainClass
        self.Helper = MainClass.Helper
        self.Action = self.Start

        self.modeText = "ファイル"
        self.oldCmdText = "ファイルモードが選択されました。"
        self.resultText = ""

        self.fileMenuText = """
        ファイルメニュー
        0 : 戻る
        1 : データ入れ替え
        2 : 保存
        3 : 書き込み
        4 : 削除
        5 : 選択
        6 : 新規データ作成

        {subText}
        """
        self.subText = ""
        self.dataText = """
        {data1name} : {data1}
        {data2name} : {data2}
        """

        self.fileName = "documents/data.txt"
        self.file = None

        self.allCollections = []
        self.dataCollection1 = []
        self.dataCollection2 = []

        #write
        self.writeText = """
        コマンドメニュー
        save : 保存
        back : 戻る
         end : 終了

        {data}
        """

    def Start(self):
        self.LoadCollection()
        self.SetWindow()
        self.GetData()
        self.Action = self.SelectMenu

    def Main(self):
        if self.Action != None:
            self.Action()
        self.ReflectData()
        self.SetWindow()

    def SetWindow(self):
        self.MainClass.oldCmdText = self.oldCmdText
        self.MainClass.modeText = self.modeText
        self.MainClass.resultText = self.resultText
    def GetData(self):
        self.dataCollection1 = self.MainClass.dataCollection1
        self.dataCollection2 = self.MainClass.dataCollection2
    def ReflectData(self):
        self.MainClass.dataCollection1 = self.dataCollection1
        self.MainClass.dataCollection2 = self.dataCollection2

    #load
    def LoadCollection(self):
        pass

    #select menu
    def SelectMenu(self):
        self.SelectMenuSetWindow()
        self.Action = self.SelectMenuUpdate
    def SelectMenuUpdate(self):
        self.SelectMenuCommandAction()
    def SelectMenuCommandAction(self):
        pass
    def SelectMenuSetWindow(self):
        pass

    #back
    def Back(self):
        self.oldCmdText = "モード選択に戻ります。"
        self.MainClass.Action = self.MainClass.SelectMode
        self.Action = self.Start
        
    #change
    def ChangeData(self):
        dataCollection1 = copy.deepcopy(self.dataCollection1)
        self.dataCollection1 = copy.deepcopy(self.dataCollection2)
        self.dataCollection2 = dataCollection1
        self.Action = self.SelectMenu

    #save
    def Save(self):
        self.SaveFunc()
        self.oldCmdText = "保存が完了しました。"
        self.Action = self.SelectMenu
    def SaveFunc(self):
        self.file = open(self.fileName, mode="w")
        self.ReflectDataForSave()
        alldataText = self.MakeSentenceForSave()
        self.WriteInFileForSave(alldataText)
        self.file.close()
    def ReflectDataForSave(self):
        pass
    def MakeSentenceForSave(self):
        pass
    def WriteInFileForSave(self, alldataText):
        pass

    #write
    def Write(self):
        self.ShowEnrouteData()
        self.Action = self.WriteUpdate
    def WriteUpdate(self):
        self.oldCmdText = "データ書き込み中"
        self.MainClass.updateWindowSwitch = True
        command = self.InputKey()
        self.CommandAction(command)
        self.AddData(command)
        self.ShowEnrouteData()
    def InputKey(self):
        pass
    def CommandAction(self):
        pass
    def AddData(self, command):
        pass
    def ShowEnrouteData(self):
        pass

    #delete
    def Delete(self):
        self.DeleteShowData()
        self.Action = self.DeleteUpdate
    def DeleteUpdate(self):
        if self.CheckMessage():
            self.DeleteFromAllCollections()
            self.oldCmdText = "データを削除しました。"
        self.Action = self.SelectMenu
    def CheckMessage(self):
        pass
    def DeleteShowData(self):
        pass
    def DeleteFromAllCollections(self):
        pass

    #select
    def Select(self):
        self.SelectShowAllCollection()
        self.Action = self.SelectUpdate
    def SelectUpdate(self):
        index = self.InputCollectionIndex()
        self.dataCollection1 = copy.deepcopy(self.allCollections[index])
        self.dataCollection1 = self.SelectToFloatList(copy.deepcopy(self.dataCollection1))
        self.oldCmdText = "データを選択しました。"
        self.Action = self.SelectMenu
    def SelectShowAllCollection(self):
        pass
    def InputCollectionIndex(self):
        return 0
    def SelectToFloatList(self, targetList):
        return []

    #new collection
    def NewCollection(self):
        self.resultText = "previous name : {}".format(self.dataCollection1[0])
        self.Action = self.NewCollectionUpdate
    def NewCollectionUpdate(self):
        name = self.InputForNewCollection()
        self.ReflectToNewCollection(name)
        self.oldCmdText = "新規データを作成しました。"
        self.Action = self.SelectMenu
    def InputForNewCollection(self):
        return self.MainClass.defaultCollection[0]
    def ReflectToNewCollection(self, name):
        pass

class AnalizeTool:
    def __init__(self, MainClass):
        self.MainClass = MainClass
        self.Action = self.Start

        self.modeText = "データ分析"
        self.oldCmdText = "データ分析モードが選択されました。"
        self.resultText = ""

        self.menuText = """
        0 : 戻る
        1 : データ入れ替え
        2 : 平均
        3 : 分散
        4 : 標準偏差
        5 : 最小二乗法

        {data}

        {subText}
        """
        self.subText = ""
        self.dataText = """
        X => {data1name:.>30} : {data1}
        Y => {data2name:.>30} : {data2}
        """

        self.singleText = """
        {menu}
        X => {collectionX:.>15} : {resultX}
        Y => {collectionY:.>15} : {resultY}
        """

        self.dataCollectionX = []
        self.dataCollectionY = []

    def Start(self):
        self.GetData()

        self.SetWindow()
        self.Action = self.SelectMenu

    def Main(self):
        if self.Action != None:
            self.Action()
        self.SetWindow()

    def SetWindow(self):
        self.resultText = self.resultText.replace("  ", "")

        self.MainClass.modeText = self.modeText
        self.MainClass.oldCmdText = self.oldCmdText
        self.MainClass.resultText = self.resultText
    def GetData(self):
        self.dataCollectionX = self.MainClass.dataCollection1
        self.dataCollectionY = self.MainClass.dataCollection2

    #メニュー選択
    def SelectMenu(self):
        dataText = self.dataText.format(
            data1name=self.dataCollectionX[0],
            data1=self.dataCollectionX[1:],
            data2name=self.dataCollectionY[0],
            data2=self.dataCollectionY[1:]
            )

        self.resultText = self.menuText.format(
            data=dataText,
            subText=self.subText)
        self.Action = self.SelectMenuCommandAction
    def SelectMenuCommandAction(self):
        command = int(input("{} : menu >> ".format(self.dataCollectionX[0])))

        if command == 0:
            self.Action = self.Back
        if command == 1:
            self.Action = self.ChangeData
        if command == 2:
            self.Action = self.Average
        if command == 3:
            self.Action = self.Dispersion
        if command == 4:
            self.Action = self.StandardDeviation
        if command == 5:
            self.Action = self.LeastSquaresMethod

    #データ入れ替え
    def ChangeData(self):
        dataCollectionX = copy.deepcopy(self.dataCollectionX)
        self.dataCollectionX = copy.deepcopy(self.dataCollectionY)
        self.dataCollectionY = dataCollectionX
        self.Action = self.SelectMenu

    #戻る
    def Back(self):
        self.oldCmdText = "モード選択に戻ります。"
        self.MainClass.Action = self.MainClass.SelectMode
        self.Action = self.Start

    #平均
    def Average(self):
        [meanX, meanY] = self.CalcAverage()
        self.oldCmdText = "平均値を計算しました。"
        self.MainClass.updateWindowSwitch = True
        self.Action = self.SelectMenu

        self.subText = self.singleText.format(
            menu="平均値",
            collectionX=self.dataCollectionX[0],
            collectionY=self.dataCollectionY[0],
            resultX=meanX,
            resultY=meanY)
    def CalcAverage(self):
        return 0

    #分散
    def Dispersion(self):
        [dispersionX, dispersionY] = self.CalcDispersion()
        self.oldCmdText = "分散を計算しました。"
        self.MainClass.updateWindowSwitch = True
        self.Action = self.SelectMenu

        self.subText = self.singleText.format(
            menu="分散",
            collectionX=self.dataCollectionX[0],
            collectionY=self.dataCollectionY[0],
            resultX=dispersionX,
            resultY=dispersionY)
    def CalcDispersion(self):
        return 0

    #標準偏差
    def StandardDeviation(self):
        [stdevX, stdevY] = self.CalcStandardDeviation()
        self.oldCmdText = "標準偏差を計算しました。"
        self.MainClass.updateWindowSwitch = True
        self.Action = self.SelectMenu
        self.subText = self.singleText.format(
            menu="標準偏差",
            collectionX=self.dataCollectionX[0],
            collectionY=self.dataCollectionY[0],
            resultX=stdevX,
            resultY=stdevY)
    def CalcStandardDeviation(self):
        return 0

    #最小二乗法
    def LeastSquaresMethod(self):
        [a, b, sigmaA, sigmaB] = self.CalcLeastSquaresMethod()
        self.oldCmdText = "最小二乗法を計算しました。"
        self.MainClass.updateWindowSwitch = True
        self.Action = self.SelectMenu
        self.subText = """
        最小二乗法
        y = ({a} ± {sigmaA}) + ({b} ± {sigmaB})x
        """.format(
            a=a,
            b=b,
            sigmaA=sigmaA,
            sigmaB=sigmaB)
    def CalcLeastSquaresMethod(self):
        pass

class Helper:
    def __init__(self, MainClass):
        self.MainClass = MainClass

    def CommandAnnounce(self, text):
        self.MainClass.oldCmdText = text

    def GetEastAsianWidthCount(text):
        count = 0
        for c in text:
            if unicodedata.east_asian_width(c) in "FWA":
                count += 2
            else:
                count += 1
        return count

    def CalcDifferenceLen(fromText, toText):
        result = Helper.GetEastAsianWidthCount(fromText) - Helper.GetEastAsianWidthCount(toText)
        if result < 0:
            result = 0
        return result

