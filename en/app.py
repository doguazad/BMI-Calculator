height=int(input("Enter Your Height [cm]: "))
weight=float(input("Enter Your Weight: "))
bmi=weight/((height/100)**2)
print("Your body mass index {}".format(round(bmi,2)))
print("Your status: ")
if bmi <=18.5:
    print("You Are Weak")
    print("{} you need to gain weightgrams".format(round(18.5*((height/100)**2)-weight,2)))
elif bmi <=24.9:
    print("Normal")
elif bmi<=29.9:
    print("you are overweight")
    print("{} you need to lose weightgrams".format(round(weight-24.9*((height / 100) ** 2)),2))
elif bmi<=39.9:
    print("Obezsiniz")
    print("{} you need to lose weightgrams".format(round(weight - 24.9 * ((height / 100) ** 2)), 2))
else:
    print("Aşırı obezsiniz")
    print("{} you need to lose weightgrams".format(round(weight - 24.9 * ((height / 100) ** 2)), 2))

