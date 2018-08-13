import week2Base

#========内容=========
#・継承・overrideを使って書いた。
#・基底クラスで大まかな関数の実行順序を記述。
#・派生クラスで細かい関数の中身を実装している。

class Sample(week2Base.SampleBase):
    def __init__(self):
        super().__init__()

        self.FileEditer = FileEditer(self)
        self.main = self.FileEditer.Start

class FileEditer(week2Base.FileEditer):
    def __init__(self, MainClass):
        super().__init__(MainClass)

    #load
    def Load(self):
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

    #select menu
    def SelectFirstCollection(self):
        if self.targetCollection == None:
            self.targetCollection = self.defaultCollection
    def SelectMenu(self):
        commandIndex = int(input("{targetCollection} >> ".format(targetCollection=self.targetCollection[0])))
        if commandIndex == 0:
            self.command = self.StartSave
        elif commandIndex == 1:
            self.command = self.StartWrite
        elif commandIndex == 2:
            self.command = self.StartDelete
        elif commandIndex == 3:
            self.command = self.StartShow
        elif commandIndex == 4:
            self.command = self.StartSelect
        elif commandIndex == 5:
            self.command = self.StartNewCollection

    #save
    def MakeSentenceForSave(self):
        alldataText = ""
        for collection in self.allCollections:
            collectionText = [str(i) for i in collection]
            alldataText += ",".join(collectionText)+"\n"
        return alldataText
    def WriteInFileForSave(self, alldataText):
        self.file.write(alldataText)
    def ReflectData(self):
        collectionNameList = list(map(lambda collection : collection[0], self.allCollections))
        try:
            dataIndex = collectionNameList.index(self.targetCollection[0])
            self.allCollections[dataIndex] = self.targetCollection
        except ValueError:
            self.allCollections.append(self.targetCollection)

    #write
    def InputKey(self):
        self.writeCommand = input("{targetCollection} No.{index} >> ".format(targetCollection=self.targetCollection[0], index=len(self.targetCollection)))
        self.MainClass.delRecOutSwitch = True
    def CommandAction(self):
        if self.writeCommand == "save":
            self.Save()
            self.MainClass.previousCommand = "保存が完了しました。"
        elif self.writeCommand == "back":
            if len(self.targetCollection) >1:
                del self.targetCollection[-1]
    def Adddata(self):
        try:
            self.targetCollection.append(float(self.writeCommand))
        except ValueError:
            pass
    def ShowEnrouteData(self):
        collectionText = [str(i) for i in self.targetCollection]
        text = "{collectionName} : {data}".format(collectionName=collectionText[0], data=", ".join(collectionText[1:]))
        self.MainClass.windowText = self.writeTextBase.format(action=text)

    #delete
    def DeleteAction(self):
        collectionNameList = list(map(lambda collection : collection[0], self.allCollections))
        try:
            dataIndex = collectionNameList.index(self.targetCollection[0])
            del self.allCollections[dataIndex]
        except ValueError:
            pass

        self.targetCollection = self.defaultCollection
    def CheckMessage(self):
        answer = input("本当に削除しますか(yes or no) >> ")
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            return False

    #show
    def Show(self):
        collectionText = [str(data) for data in self.targetCollection]
        text="{collectionName} : {data}".format(collectionName=self.targetCollection[0], data=", ".join(collectionText[1:]))
        self.selectMenuActionText = text

    #select
    def ShowAllCollection(self):
        collectionNameList = list(map(lambda collection : collection[0], self.allCollections))
        text = ""
        for i in range(len(collectionNameList)):
            text += "{index} : {data}\n".format(index=i, data=collectionNameList[i])
        self.MainClass.windowText = text
    def InputCollectionIndex(self):
        index = int(input("Collection Number : "))
        return index

    #new collection
    def InputForNewCollection(self):
        name = input("new name >> ")
        return name
    def ReflectToNewCollection(self, name):
        self.targetCollection = [name]
#===================実行部分===================
Sample().Main()