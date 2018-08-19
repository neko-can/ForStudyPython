import os

class SampleBase:
    def __init__(self):
        self.enable = True
        self.baseWindow = """
        {title:=^40}
        {mode:-^40}
        old cmd : {oldCmd}
        {text}
        """
        self.baseWindow = self.baseWindow.replace("  ", "")
        self.baseWindow = self.baseWindow.strip("\n")
        self.nowWindow = self.baseWindow
        self.previousWindow = None
        self.titleText = "Sample"
        self.modeText = ""
        self.oldCmdText = ""
        self.windowText = ""
        self.delRecordSwith = False

        #派生クラスで実装
        self.AnalizeTool = None
        self.main = None
        self.Helper = None

        #データファイルは選択済みとする
        self.dataCollectionX = ["test collection X", 0, 2, 3, 4]
        self.dataCollectionY = ["test collection Y", -2, 6, 3, -10]

    def Main(self):
        while self.enable:
            self.delRecordSwith = False

            if self.main != None:
                self.main()
            self.nowWindow = self.baseWindow.format(
                title=self.titleText,
                mode=self.modeText,
                oldCmd=self.oldCmdText,
                text=self.windowText)
            if self.nowWindow != self.previousWindow or self.delRecordSwith:
                os.system("cls")
                print(self.nowWindow)
            self.previousWindow = self.nowWindow

class AnalizeTool:
    def __init__(self, MainClass):
        self.MainClass = MainClass
        self.baseWindow = """
        {menu}

        {result}
        """

        self.windowText = self.baseWindow
        self.menuText = """
        0 : 平均
        1 : 分散
        2 : 標準偏差
        3 : 最小二乗法
        """
        self.resultBaseText = """
        {menu}
        {collectionX:<15} : {resultX}
        {collectionY:<15} : {resultY}
        """
        self.resultBaseText = self.resultBaseText.replace("  ", "")
        self.resultBaseText = self.resultBaseText.strip("\n")

        self.resultText = None
        self.oldCmdText = ""
        self.Action = None

        self.command = 0

        self.dataCollectionX = None
        self.dataCollectionY = None

        self.Helper = self.MainClass.Helper

    def Start(self):
        self.MainClass.main = self.Update
        self.MainClass.modeText ="Analize Tool"
        self.Action = self.InputTool
        self.resultText = ""
        self.SetWindow()
        self.GetData()

    def GetData(self):
        self.dataCollectionX = self.MainClass.dataCollectionX
        self.dataCollectionY = self.MainClass.dataCollectionY

    def Update(self):
        self.Action()
        self.SetWindow()

    def InputTool(self):
        self.command = int(input("command >> "))
        self.Action = self.SelectTools
        
    def SelectTools(self):
        if self.command == 0:
            self.Action = self.Average
        if self.command == 1:
            self.Action = self.Dispersion
        if self.command == 2:
            self.Action = self.StandardDeviation
        if self.command == 3:
            self.Action = self.LeastSquaresMethod

    def SetWindow(self):

        self.menuText = self.menuText.replace("  ", "")
        self.menuText = self.menuText.strip("\n")

        self.windowText = self.baseWindow.format(
            menu=self.menuText,
            result=self.resultText)

        self.windowText = self.windowText.replace("  ", "")
        self.windowText = self.windowText.strip("\n")

        self.windowText = self.Helper.LineInsertSentence(self.windowText, 10)
        self.MainClass.windowText = self.windowText
        self.MainClass.oldCmdText = self.oldCmdText

    def Average(self):
        [meanX, meanY] = self.CalcAverage()
        self.oldCmdText = "平均値を計算しました。"
        self.MainClass.delRecordSwith = True
        self.Action = self.InputTool
        self.resultText = self.resultBaseText.format(
            menu="平均値",
            collectionX=self.dataCollectionX[0],
            collectionY=self.dataCollectionY[0],
            resultX=meanX,
            resultY=meanY)
    def CalcAverage(self):
        return 0

    def Dispersion(self):
        [dispersionX, dispersionY] = self.CalcDispersion()
        self.oldCmdText = "分散を計算しました。"
        self.MainClass.delRecordSwith = True
        self.Action = self.InputTool
        self.resultText = self.resultBaseText.format(
            menu="分散",
            collectionX=self.dataCollectionX[0],
            collectionY=self.dataCollectionY[0],
            resultX=dispersionX,
            resultY=dispersionY)
    def CalcDispersion(self):
        return 0

    def StandardDeviation(self):
        [stdevX, stdevY] = self.CalcStandardDeviation()
        self.oldCmdText = "標準偏差を計算しました。"
        self.MainClass.delRecordSwith = True
        self.Action = self.InputTool
        self.resultText = self.resultBaseText.format(
            menu="標準偏差",
            collectionX=self.dataCollectionX[0],
            collectionY=self.dataCollectionY[0],
            resultX=stdevX,
            resultY=stdevY)
    def CalcStandardDeviation(self):
        return 0

    def LeastSquaresMethod(self):
        [a, b, sigmaA, sigmaB] = self.CalcLeastSquaresMethod()
        self.oldCmdText = "最小二乗法を計算しました。"
        self.MainClass.delRecordSwith = True
        self.Action = self.InputTool
        self.resultText = """
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
        pass

    def LineInsertSentence(self, sentence, n):
        newLineCount = sentence.count("\n")
        additionNewLine = n - newLineCount if n > newLineCount else 0
        return sentence + additionNewLine*"\n"


