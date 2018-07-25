
input_list = [float(i) for i in input().split(" ")]
p = input_list[0]/(input_list[0]+input_list[1])
q = input_list[1]/(input_list[0]+input_list[1])
print (p,q)
sum = 0.0
coeff = [20.0, 15.0, 6.0, 1.0]
for i in range(4):
    temp = coeff[i]*p**(i+3)*q**(3-i)
    sum += temp
print ("%.3f"%(sum))
