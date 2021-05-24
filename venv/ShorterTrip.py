import math


def soluction(A):
    tours = set(A)
    countlist = list()
    for index, _ in enumerate(A):
        tours_intern = set()
        count = 0

        for sec_value in range(index, len(A)):

            tours_intern.add(int(A[sec_value]))
            count = count + 1
            if tours_intern == tours:
                countlist.append(count)
    return min(countlist)

if __name__ == '__main__':

    A = [2,1,1,3,2,1,1,3]
    #A = [7,5,2,7,2,7,4,7]
    #A = [7,3,7,3,1,3,4,1]
    result = soluction(A)
    print(result)
