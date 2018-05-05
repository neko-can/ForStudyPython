"""
作品概要
・実験で行うような分析を計算してくれるmodule作成
・近似直線、誤差を計算
・コマンドは後で被った時に変更できるようにdictionary使用

・教える関係上、バージョン管理するか
"""

import numpy as np
import MyCommonModule as CM
import MyFileModule as FM

class MyAnalysis:
    def __init__(self):
        
        #ソース管理
        self.CMM = CM.CommonMainModule(self)
        self.fileNameListClass = FM.FileNameListClass()
        self.fileClass = FM.FileClass(self.fileNameListClass) #初期ファイルデータ生成
        self.FMM = FM.MenuModule(self.fileClass, self.fileNameListClass)
        
        #メニューの変更方法：Menu宣言→menuListに登録
        self.startMenu = { "analysis" : self.MainAnalysis, 
                           "file" : self.MainFile}
        self.startSubMenu = {"end" : self.EndProgram}
        self.startAllMenu = {"main" : self.startMenu,
                             "sub" : self.startSubMenu}
        
        self.fileMenu = {"start" : self.MainStart}
        self.fileSubMenu = {"save" : self.FMM.Save,
                            "saveAsNew" : self.FMM.SaveAsNew,
                            "open" : self.FMM.OpenFile,
                            "newFile" : self.FMM.NewFile,
                            "renameFile" : self.FMM.RenameFile,
                            "showData" : self.FMM.ShowData,
                            "addData" : self.FMM.AddData}
        self.fileAllMenu = {"main" : self.fileMenu,
                            "sub" : self.fileSubMenu}

        self.analysisMenu = {"start" : self.MainStart}
        self.analysisSubMenu = {}
        self.analysisAllMenu = {"main" : self.analysisMenu,
                                "sub" : self.analysisSubMenu}

        self.menuList = {"start" : self.startAllMenu,
                         "file" : self.fileAllMenu,
                         "analysis" : self.analysisAllMenu}

        #mainの初期値
        self.main = None
        self.IsPlay = True
        self.mainMenu = {"start" : self.MainStart}

        ##ver2
        #self.menuModule = MenuModule(self)
        #self.phaselist = ["start", "file", "analysis"]
        #self.funclist = [self.menuModule.ChangeMenu for i in range(len(self.phaselist))]
        #self.cmddict = dict(zip(self.phaselist, self.cmddict))
        ##Start Command
        #self.transcommand = {"analysis" : self.menuModule.ChangeMenu,
        #                     "file" : self.menuModule.ChangeMenu}
        #self.Startcmd = CM.CommandModule(commandquestion="ファイルを開く : ", transcommand=transcommand, cancelstr="プログラムを終了します。", cancelcommand="end")
        ##File Command
        #self.transcommand = {}

        ##main
        #self.maincmd = self.Startcmd

    def Main(self):
        #変数初期化
        self.CMM.ChangeMenu("start")
        self.IsPlay = True

        while self.IsPlay:
            self.main()

    def EndProgram(self):
        self.IsPlay = False
        print("プログラムを終了します")

    def MainStart(self):
        self.CMM.InputChangeMenu("スタートメニュー選択  > ")

    def MainAnalysis(self):
        """
        機能
        ・分析メニュー選択
        ・分析対象ファイル選択→分析内容選択→結果表示
        """

        self.CMM.InputChangeMenu("分析 > ")

    def MainFile(self):
        self.CMM.InputChangeMenu("ファイル > ")

#class MenuModule:
#    def __init__(self, myAnalysis):
#        self.myAnalysis = myAnalysis

#    def ChangeMenu(self):
#        self.myAnalysis.maincmd = self.myAnalysis.cmddict[self.myAnalysis.maincmd.command]

MyAnalysis().Main()