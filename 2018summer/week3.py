import os
import week3Base
import statistics

class SampleClass(week3Base.SampleBase):
    def __init__(self):
        super().__init__()

        self.Helper = Helper(self)
        self.AnalizeTool = AnalizeTool(self)
        self.main = self.AnalizeTool.Start

class AnalizeTool(week3Base.AnalizeTool):
    def __init__(self, MainClass):
        super().__init__(MainClass)

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

class Helper(week3Base.Helper):
    def __init__(self, MainClass):
        super().__init__(MainClass)

SampleClass().Main()

#==========メモ=============
#Σxi = [xi], Σyi = [yi]
#a = ([yi][xi^2] - [xi][xiyi]) / (n[xi^2] - [xi]^2)
#b = (n[xiyi] - [yi][xi]) / (n[xi^2] - [xi]^2)
#σy = (Σ{yi - (a + b*xi)}^2 / (n - 2))^(1/2)
#σa = σy([xi^2]/{n[xi^2] - [xi]^2}^2)^(1/2)
#σb = σy{n/(n[xi^2] - [xi]^2)}^(1/2)
#y = (a±σa) + (b±σb)x