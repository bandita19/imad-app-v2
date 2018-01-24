def checkname(name):
    if name.isalpha():
        return True
    else:
        return False


'''def checkdesignation(designatiom):
    if name.isaplha():
        return True
    else:
        return False'''

def checkusername(username):
    if username.isidentifier():
        return True
    else:
        return False
    

def checkpassword(password):
        if len(password)<6 :
            return False
        else:
            return True


def checkconfirm_password(password,confirm_password):
    if password==confirm_password:
        return True
    else:
        return False
    
    
