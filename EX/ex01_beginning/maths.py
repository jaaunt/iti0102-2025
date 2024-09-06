"""EX01 Maths."""

"""
Find the average of a, b, c and d, but first the numbers must be multiplied. a multiplied by 1, b multiplied by 2,
c multiplied by 3 and d multiplied by 4.
After the multiplication find the average of the numbers and print it out.

 """
# kasutan mul kuna short multiplicationist
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))
a_mul = a * 1
b_mul = b * 2
c_mul = c * 3
d_mul = d * 4
sum1 = a_mul + b_mul + c_mul + d_mul
average = sum1 / 4

print(average)

"""
Calculate the sum of two fractions.

One fraction is x/y where x and y are numbers given as input.
The other fraction is u/t where u and t are also numbers given as input.

Find and print the sum of x/y + u/t.

NB! the fraction does not have to be in the simplest form.
NB! the answer should be given as a string and should not contain any commas.


"""
x = int(input("Enter the value of x: "))  # lug1
y = int(input("Enter the value of y: "))  # nim1
u = int(input("Enter the value of u: "))  # lug2
t = int(input("Enter the value of t: "))  # nim2
# et liita peab leidma uhise nimetaja
lownr = y * t
# korrutab lugejad uksteise nimetajatega nimetajatega kuna neil polnud sama nimetaja
upper1st = x * t
upper2nd = u * y
# lugejate summa
sum_uppr = upper1st + upper2nd
print(str(sum_uppr) + "/" + str(lownr))

"""
Calculate and print how many hours are needed per week with given ECTS and amount of weeks, if each ECTS is 26 hours.

If it is not possible, print out -1.

Example 1
ects = 30
weeks = 12

Output
65

Example 2
ects = 1
weeks = 1

output
26

Example 3
ects = 1
weeks = 0

output
-1
"""
ects = int(input("Enter the amount of ECTS: "))
weeks = int(input("Enter the number of weeks: "))
# nadal 168 h
# eap 26 h
neededh = ects * 26
availableh = weeks * 168
if neededh > availableh or weeks <= 0:
    print(-1)
else:
    weekly_amnt = neededh / weeks
    print(weekly_amnt)
