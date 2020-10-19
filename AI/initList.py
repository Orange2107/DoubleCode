import string

str1 = ''
str2 = [1,2,3,4,5,6,7,8,0]
for i in range(9):
    str1 = str1 +'%d'%str2[i]

print (str1)
