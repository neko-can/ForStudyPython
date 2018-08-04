#目標 : 構造の構築

class SequenceModule:
    def __init__(self, MainClass):
        self.MainClass = MainClass

    def End(self):
        print("プログラムを終了します。")
        self.MainClass.enable = False

class FileModule:
    def __init__(self):
        pass

    def Save(self):
        print("保存しました。")

    def Write(self):
        print("データの書き込みが完了しました。")

    def Show(self):
        print("データの表示が完了しました。")

    def Select(self):
        print("編集するデータ群を選択しました。")

class AnalysisModule:
    def __init__(self):
        pass

    def Average(self):
        print("平均値を計算しました。")

    def Dispersion(self):
        print("分散を計算しました。")

    def StandardDeviation(self):
        print("標準偏差を計算しました。")

# sample 1 if文による制御
class Sample1 : 
    def __init__(self):
        self.enable = True
        self.phase = [1, 0, 0]

        self.phase0Menu = \
            """
            初期画面
            0 : 終了
            1 : 初期画面
            2 : ファイル
            3 : データ分析
            """

        self.phaseFileMenu = \
            """
            ファイルメニュー選択
            0 : 戻る
            1 : 保存
            2 : 書き込み
            3 : 表示
            4 : 選択
            """

        self.phaseAnalysisMenu = \
            """
            データ分析メニュ－
            0 : 戻る
            1 : 平均値
            2 : 分散
            3 : 標準偏差
            """

        self.phase0Menu = self.phase0Menu.replace(" ", "")
        self.phaseFileMenu = self.phaseFileMenu.replace(" ", "")
        self.phaseAnalysisMenu = self.phaseAnalysisMenu.replace(" ", "")

        self.SequenceModule = SequenceModule(self)
        self.FileModule = FileModule()
        self.AnalysisModule = AnalysisModule()

    def Main(self):

        while self.enable:
            if self.phase[0] == 0:
                self.SequenceModule.End()

            if self.phase[0] == 1:
                print(self.phase0Menu)
                self.InputPhase(phaseIndex=0, question="mode : ")

            if self.phase[0] == 2:
                print(self.phaseFileMenu)
                self.InputPhase(phaseIndex=1, question="file : ")

                if self.phase[1] == 0:
                    self.ChangePhase(phaseIndex=0, newIndex=1)

                if self.phase[1] == 1:
                    self.FileModule.Save()

                if self.phase[1] == 2:
                    self.FileModule.Write()

                if self.phase[1] == 3:
                    self.FileModule.Show()

                if self.phase[1] == 4:
                    self.FileModule.Select()

            if self.phase[0] == 3:
                print(self.phaseAnalysisMenu)
                self.InputPhase(phaseIndex=1, question="analysis : ")

                if self.phase[1] == 0:
                    self.ChangePhase(phaseIndex=0, newIndex=1)

                if self.phase[1] == 1:
                    self.AnalysisModule.Average()

                if self.phase[1] == 2:
                    self.AnalysisModule.Dispersion()

                if self.phase[1] == 3:
                    self.AnalysisModule.StandardDeviation()


    def InputPhase(self, phaseIndex, question="command : "):
        self.ResetPhase(fromIndex=phaseIndex, toIndex=len(self.phase)-1)
        self.phase[phaseIndex] = int(input(question))

    def ChangePhase(self, phaseIndex, newIndex):
        self.ResetPhase(fromIndex=phaseIndex, toIndex=len(self.phase)-1)
        self.phase[phaseIndex] = newIndex

    def ResetPhase(self, fromIndex, toIndex):
        targetIndexes = list(range(fromIndex, toIndex+1))
        for i in targetIndexes:
            self.phase[i] = 0

# sample 2 delegate
class Sample2 : 
    def __init__(self):
        pass

    def Main(self):
        pass

# 実際に試してみる
Sample1().Main()