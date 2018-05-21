
password = "SiD#@272"
flag = 0
while True:  
    if (len(password)<6 or len(password)>12):
        flag = 1
        break
    elif not 'a-z' in password:
        flag = 1
        break
    elif not '0-9' in password:
        flag = 1
        break
    elif not 'A-Z' in password:
        flag = 1
        break
    elif not '$#@' in password:
        flag = 1
        break
    
    else:
        flag == 0
        print("Valid Password")
        break
 
if flag ==1:
    print("Not a Valid Password")