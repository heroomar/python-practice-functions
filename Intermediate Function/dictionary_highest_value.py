def gdc(dic):
    max=0
    for i in dic:
        if dic[i] > dic[max]:
            max = i
    return max

dic = {
0: 25,
1: 58,
2: 44,
3: 8,
4: 9,
5: 10,
6: 98,
7: 44,
8: 7,
9: 23,
}


print("dictionary highest value index is:",gdc(dic)," => ",(dic[gdc(dic)]))