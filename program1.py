def bonAppetit(bill, k, b):
    bill.pop(k)
    sum = 0
    for j in range(len(bill)):
        sum = sum + bill[j]
    total = sum/2
    if(b==total):
        print("BRIAN CALCULATED CORRECTLY AND HONESTLY!")
    else:
        a = (int)(b-total)
        print(a)


n,k = map(int, input().split())
bill = [int(x) for x in input().split()]
b = int(input())
bonAppetit(bill,k,b)