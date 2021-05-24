import math

def soluction(A, S):
    res_count = 0

    for index, value in enumerate(A):
        sum_res = 0
        count_char = 0
        for value_int in range(index, len(A)):
            count_char = count_char + 1
            sum_res = sum_res + A[value_int]
            average_res = sum_res/count_char

            # print(f" Contador = {count_char}")
            # print(f" soma = {sum_res}")
            # print(f" media = {average_res}")

            if average_res == S:
                res_count = res_count + 1

    return res_count

if __name__ == '__main__':
    # A = [2, 1, 4]
    # S = 3

    # A = [2,1,3]
    # S = 2

    A = [0,4,3,-1]
    S = 2

    result = soluction(A, S)

    print(f"Resultado é {result}")