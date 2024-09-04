"""EX01 ATM."""

"""
Create a machine that dispenses money using 1€, 5€, 10€, 20€, 50€ and 100€ banknotes.

Given the sum, one must print out how many banknotes does it take to cover the sum. Task is to cover the sum with as little
banknotes as possible.

Example
The sum is 72€
We use four banknotes to cover it. The banknotes are 20€, 50€, 1€ and 1€.
"""

amount = int(input("Enter a sum: "))
banknotes = 0
note_options = [100, 50, 20, 10, 5, 1] # hulk et saaks kasutada for funktsiooni ja labi vaadata koik need alustades suurimast
for i in note_options:
    if amount == 0:
        break # lopetab ara kui summa on 0
    how_manyfit = amount // i # jagab suurima taisarvuni, jagab kogusumma hulga liikmega (i)
    banknotes += how_manyfit # lisab leitud koguse voi jatab samaks kui rahataht on liiga suur et seda anda
    # pikalt banknotes = how_manyfit + banknotes
    amount -= how_manyfit*i # lahutab algsummast selle palju rahatahtedes valja annab

print(f"Amount of banknotes needed: {banknotes}")