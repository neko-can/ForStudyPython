import numpy as np
import sys
from enum import Enum
from datetime import datetime

class ManageMoney2:
    def __init__(self):
        self.HC = HelpClass()
        self.DC = DataClass()
        self.commandMenu = {"adddata" : self.AddData,
                            "addkind" : self.AddKind,
                            "showdata" : self.ShowData,
                            "showkind" : self.ShowKind,
                            "showcommand" : self.ShowCommand,
                            "showdiary" : self.ShowDiary,
                            "deletedata" : self.DeleteData,
                            "save" : self.Save,
                            "end" : self.EndProgram}
        self.isPlaying = True

        self.today = datetime.today()
        self.checkyear = self.today.year
        self.checkmonth = self.today.month - 1

    def Main(self):
        self.isPlaying = True

        self.commandMenu["showdata"]()
        self.commandMenu["showcommand"]()
        while self.isPlaying:
            command = self.HC.inputInOption("command : ", [*self.commandMenu])
            self.commandMenu[command]()

    def AddData(self):
        print(self.DC.allkind)
        #year = self.HC.inputInt("年 : ", 1)
        #month = self.HC.inputInt("月 : ", 1)
        year = self.checkyear
        month = self.checkmonth
        day = self.HC.inputInt(str(year) + " 年 " + str(month) + " 月 : " + "日 > ", 1)
        kind = self.HC.inputInOption(str(year) + " 年 " + str(month) + " 月" + str(day) + " 日 : " + "種類 > ", self.DC.allkind)
        amount = self.HC.inputInt(str(year) + " 年 " + str(month) + " 月" + str(day) + " 日 : " + "金額 > ", 0)
        note = input(str(year) + " 年 " + str(month) + " 月" + str(day) + " 日 : " + "メモ > ")

        data = np.array([[year, month, day, kind, amount, note]])
        self.DC.alldata = np.r_[self.DC.alldata, data]

    def AddKind(self):
        kind = input("種類追加 : ")
        if kind in self.DC.allkind:
            print("既に登録されている種類です。")
        else:
            self.DC.allkind = np.append(self.DC.allkind, kind)

    def ShowData(self):
        self.DC.ShowData(self.checkyear, self.checkmonth)

    def ShowKind(self):
        print(self.DC.allkind)

    def ShowCommand(self):
        print([*self.commandMenu])

    def ShowDiary(self):
        self.HC.printWithNumber(self.DC.alldata)

    def Save(self):
        self.DC.Save()

    def DeleteData(self):
        linenumber = self.HC.inputInt("削除したいデータ番号 : ", 1, self.DC.alldata.shape[0]-1)
        self.DC.alldata = np.delete(self.DC.alldata, int(linenumber), 0)
        print("削除完了")

    def EndProgram(self):
        print("プログラムを終了します。")
        self.isPlaying = False

class DataClass:
    def __init__(self):
        self.filename = "ManageMoney2.npz"
        self.datastruct = Enum("datastruct", "year month day kind amount note")
        self.kindstruct = Enum("kindstruct", "収入 食費 交通費 学費 その他")
        self.alldata = None
        self.allkind = None

        self.HC = HelpClass()
        self.vToInt = np.vectorize(self.HC.ToInt)
        self.DHC = DataHelpClass(self)

        self.Load()

    def Save(self):
        np.savez(self.filename, alldata=self.alldata, allkind=self.allkind)
        print("保存完了しました。")

    def InitData(self):
        self.alldata = np.array([self.datastruct._member_names_]) #全てstring型で作成。後で項目追加できるように。
        self.allkind = np.array(self.kindstruct._member_names_)

    def Load(self):
        try:
            filedata = np.load(self.filename)
            self.alldata = filedata["alldata"]
            self.allkind = filedata["allkind"]

        except FileNotFoundError:
            print(self.filename + "ファイルがなかったので、ファイルを初期化します。")
            self.InitData()
            self.Save()

    def ShowData(self, checkyear, checkmonth):
        result = np.array([])
        sum = [0, 0, 0]
        sumstruct = Enum("sumstruct", "income spend difference")
        #year filter
        checkyeardata = self.alldata[:, self.datastruct.year.value-1]
        checkyeardata = checkyeardata.reshape((checkyeardata.shape[0], 1))
        self.checkdata = self.alldata[np.any(checkyeardata == str(checkyear), axis=1)]
        #month filter
        checkmonthdata = self.checkdata[:, self.datastruct.month.value-1]
        checkmonthdata = checkmonthdata.reshape((checkmonthdata.shape[0], 1))

        checkfilterdata = None
        checkfilterdata = self.checkdata[np.any(checkmonthdata == str(checkmonth), axis=1)]
        checkkinddata = checkfilterdata[:, self.datastruct.kind.value-1]
        checkkinddata = checkkinddata.reshape((checkkinddata.shape[0], 1))
        for kind in self.allkind:
            filterresult = checkfilterdata[np.any(checkkinddata == str(kind), axis=1)]
            if filterresult.shape[0] != 0:
                amountPerKind = filterresult[:, self.datastruct.amount.value-1]
                amountPerKind = self.vToInt(amountPerKind)
                result = np.append(result, str(checkyear) + "年" + str(checkmonth) + "月" + " " + str(kind) + " : " + str(np.sum(amountPerKind)) + " 円")

                #合計計算
                if kind == self.kindstruct.収入.name:
                    sum[sumstruct.income.value-1] += np.sum(amountPerKind)
                    sum[sumstruct.difference.value-1] += np.sum(amountPerKind)
                else:
                    sum[sumstruct.spend.value-1] += np.sum(amountPerKind)
                    sum[sumstruct.difference.value-1] -= np.sum(amountPerKind)

        #合計反映
        result = np.append(result, str(checkyear) + "年" + str(checkmonth) + "月" + " " + "支出合計" + " : " + str(sum[sumstruct.spend.value-1]) + " 円")
        result = np.append(result, str(checkyear) + "年" + str(checkmonth) + "月" + " " + "収入合計" + " : " + str(sum[sumstruct.income.value-1]) + " 円")
        result = np.append(result, str(checkyear) + "年" + str(checkmonth) + "月" + " " + "残高合計" + " : " + str(sum[sumstruct.difference.value-1]) + " 円")

        self.HC.printWithNumber(result)

class DataHelpClass:
    def __init__(self, dataClass):
        self.DC = dataClass

class HelpClass:
    def __init__(self):
        "補助"

    def inputInt(self, str, bottom=-sys.maxsize-1, top=sys.maxsize):
        try:
            result = input(str)
            check = int(result)
            if check < bottom or top < check:
                raise ValueError
        except ValueError:
            print("不適切")
            result = self.inputInt(str, bottom, top)

        return result

    def inputInOption(self, str, option):
        result = input(str)
        if result not in option:
            print("入力ミスです。")
            result = self.inputInOption(str, option)

        return result

    def printWithNumber(self, ndarray):
        noline = ndarray.shape[0]
        for i in range(noline):
            print(str(i) + ". " + str(ndarray[i]))

    def ToInt(self, target):
        try:
            result = int(target)
        except:
            result = 0

        return result