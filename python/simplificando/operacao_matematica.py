#AFTER
import operator
def __action__(self, other, op):
    if other.__m == self.__m and other.__n == self.__n:
        result = []

        for i in range(other.__m):
            lst = []

            for j in range(other.__n):
                    lst.append(op(self.elems[i][j], other.elems[i][j]))
                
                    #another operation


            result.append(lst)

        return Matrix(result)

#Calling method..
__add__(other, operator.add(fgh,xdfgh))
__add__(other, operator.sub)

#BEFORE

# def __add__(self, other):
#     if other.__m == self.__m and other.__n == self.__n:
#         result = []

#         for i in range(other.__m):
#             lst = []

#             for j in range(other.__n):
#                 lst.append(self.elems[i][j] + other.elems[i][j])

#             result.append(lst)

#         return Matrix(result)

# def __sub__(self, other):
#     if other.__m == self.__m and other.__n == self.__n:
#         result = []

#         for i in range(other.__m):
#             lst = []

#             for j in range(other.__n):
#                 lst.append(self.elems[i][j] - other.elems[i][j])     

#             result.append(lst)
#         return Matrix(result)