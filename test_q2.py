string=('hello world! 123')
count1=0
count2=0
for i in string:
      if(i.isdigit()):
            count1=count1+1
      else: 
            count2=count2+1
print("Digits:",count1)
print("Letters:",count2)
