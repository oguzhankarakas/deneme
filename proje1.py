#Kök bulduran program
#b2-4ac
#-b-kökdelta/2a
#-b+kökdelta/2a

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

delta = b**2-4*a*c

x1= (-b - delta **0.5)/(2 * a)
x2= (-b + delta **0.5)/(2 * a)

print('Birinci kök : {}\n İkinci kök : {}\n'.format(x1,x2))


x2 = int(input("x^2li terimin katsayısını girin:"))
x1 = int(input("x'li terimin katsayısını girin:"))
sabit = int(input("sabit değerini girin:"))

delta = (x1**2) - (4*x2*sabit)
print(delta)
kök1 =  (-x1 - (delta**0.5))/2*x2
kök2 =  (-x1 + (delta**0.5))/2*x2
print("kök 1 = {}\nkök 2 = {}".format(kök1,kök2))
