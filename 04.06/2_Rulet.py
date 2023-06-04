try:
    N = int(input())
    if N == 1:
        print(0)
    else:
        cuts = 0
        while N > 1:
            N = N / 2
            cuts += 1
        print(cuts)
    
except ValueError:
    print("Некорректный ввод")