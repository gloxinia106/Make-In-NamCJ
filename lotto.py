#lotto.py
from random import choice
import os

print("="*7 + "로또 번호" + "="*7)

for i in range(1,6):
    num= list(range(1,46))
    lot = []
    while len(lot) != 6:
        lot_num = choice(num)
        lot.append(lot_num)
        num.remove(lot_num)
    lot.sort()
    print(lot)
    print("\n")

os.system("Pause")
