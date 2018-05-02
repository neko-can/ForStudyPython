import numpy as np 

#dictionaryの保存のテスト

filename = "test.npz"
testDict = {"test" : np.array([1, 2, 3])}
np.savez(filename, testDict=testDict)
print("保存完了")

loadDict = np.load(filename)
print(type(loadDict["testDict"][()]))