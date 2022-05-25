# 練習題decorator

def revise_divide(func):
    def inner(n, d):
        if d == 0:
            print("除數不可為0")
        else:
            m = func(n, d)
            print(m)
    return inner

def divide(n, d):
    return n/d

n = input("請輸入被除數: ")
d = input("請輸入除數: ")
n = int(n)
d = int(d)
divide = revise_divide(divide)
divide(n, d)