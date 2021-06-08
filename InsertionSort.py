def isort(a):
    for x in range(1, len(a)):
        print(x)
        k = a[x] #element present at index number 1
        j = x-1
        while j >= 0 and k < a[j]: #comparing elemnts with the nect until the last item
            print("entrou")
            a[j+1] = a[j]
            j -= 1
        a[j+1] = k


a = [24,56,1,50,17]
teste = (-1+1)

print(f"  teste {teste}")
isort(a)
print(a)

