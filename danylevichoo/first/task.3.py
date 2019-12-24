
list_1=[1,2,77,'Sann','-','Sarca',True, {}]

sum = 0
String = " "


for i in range(len(list_1)):
    if (type(list_1[i])) == int:
        sum += int(list_1[i])
    elif (type(list_1[i])) == str:
        String=String+list_1[i]+' '
    else:
        print("Nothing to do - ", list_1[i])

print("Summ =", sum, "\nStrings -",String)


