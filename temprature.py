import sys

if len(sys.argv)==1:
    script_name=sys.argv[0]
    temprature=sys.argv[1]

else:
    script_name=sys.argv[0]
    temprature=25
    print("Input not provided, using default temprature")





temp=int(temprature)
if(temp<15):
    condition="Cold"
elif(temp>=15 and temp<=25):
    condition="Normal"
else:
    condition="Hot"


print("Script Name:",script_name)
print("Temprature:",temprature)
print("Condition:",condition)   
