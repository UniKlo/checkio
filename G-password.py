def golf(password):
    if (len(password) >= 10 
        and password != password.upper() 
        and password != password.lower() 
        and any(c.isdigit() for c in password)):  
        return True
    else:
        return False
    
        

if __name__ == '__main__':
      #These "asserts" using only for self-checking and not necessary for auto-testing
     golf('A1213pokl') == False
     golf('bAse730onE') == True
     golf('asasasasasasasaas') == False
     golf('QWERTYqwerty') == False
     golf('123456123456') == False
     golf('QwErTy911poqqqq') == True
     print("Use 'Check' to earn sweet rewards!")