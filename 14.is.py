#age = 12
#print(type(age))
#print(type(age) is int )


magham = int(input("lotfan magham khod ra vared konid :"))

if type(magham) is str :
    magham =int(magham)

    if magham == 1 :
        print("medal tala")
    elif magham == 2 :
        print("medal noghreh")
    elif magham == 3 :
        print("medal boronz")        
    else:
        print("medal nemigiri")      



