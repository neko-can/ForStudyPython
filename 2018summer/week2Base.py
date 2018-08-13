import os

class SampleBase:
    def __init__(self):
        self.enable = True

        self.baseWindow = """
        ==========Sample===========
        ---------{mode}----------
        old cmd : {previousCommand}
        {text}
        """
        self.baseWindow = self.baseWindow.replace("  ", "")
        self.nowWindow = self.baseWindow
        self.previousWindow = None
        self.delRecOutSwitch = False
        self.previousCommand = None
        self.modeText = None
        self.windowText = None

        #派生クラスで実装
        self.FileEditer = None
        self.main = None

    def Main(self):
        while self.enable:
            self.delRecOutSwitch = False
            self.main()
            self.nowWindow = self.baseWindow.format(
                mode=self.modeText, 
                previousCommand=self.previousCommand,
                text=self.windowText)
            if self.nowWindow != self.previousWindow or self.delRecOutSwitch:
                os.system("cls")
                print(self.nowWindow)
            self.previousWindow = self.nowWindow


class FileEditer:
    def __init__(self, MainClass):
        
        self.MainClass = MainClass

        #select menu
        self.command = None
        self.targetCollection = None
        #self.allCollections = [["collection title", 1, 2, 3], ["collection title2", 1, 2, 3]]
        self.allCollections = None
        self.isOnStart = True
        self.questionStr = ""
        self.selectMenuTextBase = """
        0 : save
        1 : write
        2 : delete
        3 : show
        4 : select
        5 : new collection
        {action}
        """
        self.selectMenuTextBase = self.selectMenuTextBase.replace("  ", "")
        self.selectMenuActionText = ""
        
        #save
        self.fileName = "documents/data.txt"
        self.dataTitle = ""
        self.data = []
        self.file = None

        #write
        self.writeCommand = None
        self.writeTextBase = """
        save : 保存
        back : 戻る
         end : 終了
        {action}
        """
        self.writeTextBase = self.writeTextBase.replace("  ", "")

        #delete
        self.defaultCollection = ["default collection"]

    def Start(self):
        self.MainClass.windowText = "file"
        self.MainClass.main = self.Update
        self.command = self.StartLoad

    def Update(self):
        if self.command != None:
            self.command()

    #load
    def StartLoad(self):
        self.MainClass.windowText = "start load"
        self.command = self.UpdateLoad
    def UpdateLoad(self):
        self.Load()
        self.command = self.StartSelectMenu
        self.MainClass.previousCommand = "ロードが完了しました。"
    ##override function
    def Load(self):
        pass

    #select menu
    def StartSelectMenu(self):
        text = self.selectMenuTextBase.format(action=self.selectMenuActionText)
        self.MainClass.windowText = text
        self.selectMenuActionText = ""

        self.SelectFirstCollection()
        self.command = self.UpdateSelectMenu
    def UpdateSelectMenu(self):
        self.SelectMenu()
    ##override function
    def SelectFirstCollection(self):
        pass
    def SelectMenu(self):
        pass

    #save
    def StartSave(self):
        self.MainClass.windowText = "start save"
        self.command = self.UpdateSave
    def UpdateSave(self):
        self.Save()
        self.command = self.StartLoad
    def Save(self):
        self.file = open(self.fileName, mode="w")

        self.ReflectData()
        alldataText = self.MakeSentenceForSave()
        self.WriteInFileForSave(alldataText)

        self.file.close()

        self.MainClass.previousCommand = "保存が完了しました。"
    def ReflectData(self):
        pass
    ##override
    def MakeSentenceForSave(self):
        pass
    def WriteInFileForSave(self, alldataText):
        pass

    #write
    def StartWrite(self):
        collectionText = [str(i) for i in self.targetCollection]
        text = "{collectionName} : {data}".format(collectionName=collectionText[0], data=", ".join(collectionText[1:]))
        self.MainClass.windowText = self.writeTextBase.format(action=text)
        self.command = self.UpdateWrite
    def UpdateWrite(self):
        self.MainClass.previousCommand = "データ書き込み中"
        self.InputKey()
        self.CommandAction()
        self.Adddata()
        self.ShowEnrouteData()

        if self.writeCommand == "end":
            self.command = self.StartSelectMenu
            self.MainClass.previousCommand = "書き込み完了"
    ##override
    def InputKey(self):
        pass
    def CommandAction(self):
        pass
    def Adddata(self):
        pass
    def ShowEnrouteData(self):
        pass

    #delete
    def StartDelete(self):
        collectionText = [str(data) for data in self.targetCollection]
        text="{collectionName} : {data}".format(collectionName=self.targetCollection[0], data=", ".join(collectionText[1:]))
        self.MainClass.windowText = text
        self.command = self.UpdateDelete
    def UpdateDelete(self):
        self.Delete()
        self.command = self.StartSelectMenu
    def Delete(self):
        if self.CheckMessage():
            self.DeleteAction()
            self.MainClass.previousCommand = "削除完了"
    ##override
    def DeleteAction(self):
        pass
    def CheckMessage(self):
        return False

    #show
    def StartShow(self):
        self.command = self.UpdateShow
    def UpdateShow(self):
        self.Show()
        self.MainClass.previousCommand = "データ表示完了"
        self.command = self.StartSelectMenu
    ##override
    def Show(self):
        pass

    #select
    def StartSelect(self):
        self.ShowAllCollection()
        self.command = self.UpdateSelect
    def UpdateSelect(self):
        self.Select()
        self.command = self.StartSelectMenu
        self.MainClass.previousCommand = "データ選択完了"
    def Select(self):
        index = self.InputCollectionIndex()
        self.targetCollection = self.allCollections[index]
    ##override
    def ShowAllCollection(self):
        pass
    def InputCollectionIndex(self):
        return 0

    #new collection
    def StartNewCollection(self):
        self.MainClass.windowText = "previous name : {name}".format(name=self.targetCollection[0])
        self.command = self.UpdateNewCollection
    def UpdateNewCollection(self):
        name = self.InputForNewCollection()
        self.ReflectToNewCollection(name)
        self.command = self.StartSelectMenu
        self.MainClass.previousCommand = "新規作成完了"
    ##override
    def InputForNewCollection(self):
        return self.defaultCollection[0]
    def ReflectToNewCollection(self, name):
        pass