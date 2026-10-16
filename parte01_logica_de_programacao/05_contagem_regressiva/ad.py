import os
import time

os.system("cls")

n=int(input("informe um numero inteiro: "))

while n >= 0:
    os.system("cls")
    print(f"{n}...")
    time.sleep(1)
    n -=1
print("BOOOMMMM!!!!")