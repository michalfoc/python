# Ex28. BOOLEAN PRACTICE
"""Choose wether you want to test a single phrase, or the whole lot."""

p1 = True and False
p2 = False and True
p3 = 1 == 1 and 1 == 2
p4 = "test" == "test"
p5 = 1 == 1 or 2 != 1
p6 = True and 1 == 1
p7 = False and 0 != 0
p8 = True or 1 == 1
p9 = "test" == "testing"
p10 = 1 != 0 and 2 == 1
p11 = "test" != "testing"
p12 = "test" == 1
p13 = not (True and False)
p14 = not (1 == 1 and 0 != 1)
p15 = not (10 == 1 or 1000 == 1000)
p16 = not (1 != 10 or 3 == 4)
p17 = not ("testing" == "testing" and "Zed" == "Cool Guy")
p18 = 1 == 1 and (not ("testing" == 1 or 1 == 0))
p19 = "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
p20 = 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))


x = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20]
y = int(input("What you want to test? (1 for single phrase, 2 for all) >"))
z = 0

if y == 1:
    y1 = int(input("Which phrase You want to test? > "))
    if y1 in range (21):
        print(y1, x[y1 - 1])
    else:
        print("Number out of range!")
elif y == 2:
    for i in x:
        z = z + 1
        print(f"{z}.", i)
