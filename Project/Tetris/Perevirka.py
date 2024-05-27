from Matrics import Matrics



# def Matr(x):
#     for i in range(0,10):
#         for m in range(0,10):
#             if x>5:
#                 break
#             x+=1
#     return x
# print(Matr(1))



# l=[]
# for el in l:
#     print(el)
# l = [[0, 0, 0],[1,1,1]]
# k = l[0]
# for el in l:
#     el = [11]
# print(len(l[0]))
# print(k,l)

#
# l = [1,3,4,6,7,9,10]
# for i in range(23, -1, -1):
#     print(i)



M = Matrics()
M.randomcreate()
M.figurefall()
M.fall()
print(M.matrics)
M.fall()
print(M.matrics)
for i in range(1, 30):
    M.fall()
print(M.matrics)

