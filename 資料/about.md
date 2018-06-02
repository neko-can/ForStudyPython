# プログラムについて

### 目次
* <a href="#目的">目的</a>
* <a href="#プログラム概要">プログラム概要</a>
* <a href="#フローチャート">フローチャート</a>
* <a href="#処理内容">処理内容</a>


<div id="目的"></div>

## 目的

対話画面で動くプログラム製作を通じて、
Pythonの基礎を学ぼう！  
構文の基礎を学ぼう！

<div id="プログラム概要"></div>

## プログラム概要

* GUIを意識したライブラリを使わないため、print等の出力はPython対話画面に表示される。
* すべてキーボードからの入力になり、入力されたキーボード情報の違いから処理を分岐させるしかない。
* モードに応じてコマンドを変更し、入力文字に対応して処理を実行する。

* **cmd上で動くアプリと動作が同じということになる**
  * 似た動作として下にPython対話ウィンドウの使用を載せておく


```
>>> help　←入力文字
Type help() for interactive help, or help(object) for help about object.
>>> help()　←入力文字

Welcome to Python 3.6's help utility!

If this is ... 説明が続く

help> 
numpy.random.rand　←入力文字

Help on built-in function rand in numpy.random:
... 説明が続く

```

<div id="フローチャート"></div>

## フローチャート

↓フローチャートに表すとこんな感じ

<img src="../Pictures/MyProgramFlowChart.png" height="200">


<div id="処理内容"></div>

## 処理内容

* モードは以下に分かれる