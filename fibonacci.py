def fibonacci(sayi):
    if sayi < 0:
        return -1
    if sayi == 0:
        return 0
    if sayi == 1:
        return 1
    return fibonacci(sayi-1) + fibonacci(sayi-2)
fib = int(input("Fibonacci sayisi giriniz: "))
print("Fibonacci : ",fibonacci(fib))