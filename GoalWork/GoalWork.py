"""
作品概要
・実験で行うような分析を計算してくれるmodule作成
・近似直線、誤差を計算
・コマンドは後で被った時に変更できるようにdictionary使用

・教える関係上、バージョン管理するか
"""

import numpy as np
from MyCommonModule import *
from MyFileModule import *


class MyAnalysis:
    def __init__(self):
        
        #ソース管理
        self.CMM = CommonMainModule(self)
        self.fileNameListClass = FileNameListClass()
        self.fileClass = FileClass(self.fileNameListClass) #初期ファイルデータ生成
        self.FMM = MenuModule(self)
        
        #ver3
        self.startphase = ["file", "analysis"]
        self.startfunc = {}
        self.filephase = ["start"]
        self.filefunc = {"save" : self.FMM.Save,
                         "saveasnew" : self.FMM.SaveAsNew, #未実装
                         "open" : self.FMM.OpenMode.Main,
                         "newfile" : self.FMM.NewFile, #未実装
                         "renamefile" : self.FMM.RenameFile,
                         "showdata" : self.FMM.ShowData,
                         "showfile" : self.FMM.ShowFileList,
                         "showarray" : self.FMM.ShowArrayList,
                         "adddata" : self.FMM.AddData}
        self.analysisphase = ["start"]
        self.analysisfunc = {}

        self.isPlay = True
        self.StartMode = OriginalClass(MyAnalysis=self, funclist=self.startfunc,phaselist=self.startphase, question="スタートメニュー選択 : ")
        self.FileMode = FileMode(self, funclist=self.filefunc, phaselist=self.filephase)
        self.AnalysisMode = OriginalClass(MyAnalysis=self, funclist=self.analysisfunc, phaselist=self.analysisphase, question="分析メニュー選択 : ")
        self.AllMode = {"start" : self.StartMode,
                        "file" : self.FileMode,
                        "analysis" : self.AnalysisMode}
        self.MainClass = self.StartMode
        self.MainClass.ShowCommand()

    def Main(self):
        while self.isPlay:
            self.MainClass.Main()

#ver 3
MyAnalysis().Main()