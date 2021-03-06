#最大公共子序列
def lcs(str1,str2):
    len1= len(str1)
    len2= len(str2)
    res = [[0]*(len2+1) for _ in range(len1+1)]
    for i,x in enumerate(str1, start=1):
        for j,y in enumerate(str2, start=1):
            if x == y:
                res[i][j] = res[i-1][j-1]+1
            else:
                res[i][j] = max(res[i-1][j], res[i][j-1])
    return res[len1][len2]

#全排列
def Permutation(string,level):
    if level == len(string)-1:
        print("%s\n"%string)
        return
    for i in range(level,len(string)):
        string[level],string[i] = string[i],string[level]
        Permutation(string,level+1)
        string[level],string[i] = string[i],string[level]

#string='abc'
#Permutation(list(string),0)