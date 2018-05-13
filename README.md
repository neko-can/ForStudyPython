# ForStudyPython

Pythonの勉強のため

## 参照型と値型

変数の型によって決まる
* 値型 : int, float, str, tuple, bytes, frozenset等
* 参照型 : list, dict, set, bytearray等

## 変数のスコープ
* selfとは別にアンダーバーによってアクセスを制限できる。

```
self.test #外部からアクセス可能
self._test #呼び出すと警告が出る
self.__test #外部から呼び出せない。AttributeError。._Test__testとすれば呼び出せる。
```

## 宿題
 * [2018/05/13 宿題](参考プログラム/HW20180513.md)