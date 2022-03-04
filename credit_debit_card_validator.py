card_no = "4622444224700682"
odd_sum = 0
even_sum= 0
double_list = [] #for storing the list elements after doubling it up
num = list(card_no) #converting the string value to kind of a list
for (idx,val) in enumerate(num): #enumerate is used for obtaining an indexed list
     if idx % 2 != 0:
        #print(str(idx)+ " => "+val) #for printing the index position
        odd_sum += int(val)
     else:
        double_list.append(int(val)*2)

#converting the list into a string
double_string = ""
for x in double_list:
    double_string += str(x)

#converting a string back to a list
double_list = list(double_string)

for x in double_list:
    even_sum += int(x)
net_sum = even_sum + odd_sum
if net_sum % 10 == 0:
    print("VALID CARD")
else:
    print("INVALID CARD")