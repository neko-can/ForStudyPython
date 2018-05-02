#以下の行列の計算をせよ
#(3, 4) * (4, 5) = (3, 5)
array1 = [[i**2 for i in range(4)] for i in range(3)]
array2 = [[i for i in range(5)] for i in range(4)]
print("array1" + str(array1))
print("array2" + str(array2))

print("array1の１行目２列目の要素 = " + str(array1[0][1]))
print("array1の行数 = " + str(len(array1)))
print("array1の列数 = " + str(len(array1[0])))

c1 = len(array1)
r1 = len(array1[0])
c2 = len(array2)
r2 = len(array2[0])

for i in range(c1):
    for j in range(r1):
        ""

array3 = []
for i in range(len(array1)):
    "行１ループ"
    for j in range(len(array1[0])):
        "列１ループ"
        #print(array1[i][j])
        for k in range(len(array2[0])):
            ""
            #print(array2[i][k])
        