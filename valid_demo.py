def checkname(name,linames):
        if len(name)<3:
                return 1 #too small recipe_name
        elif name in linames:
                return 2 #recipe available
        elif type(name)==str:
                #for i in range(len(name)):
                if name.isalpha():#(name[i]>'a' and name[i]<'z') or (name[i]>'A' and name[i]<'Z') or (name[i]==' ' and i>0):
                        return 3 #recipe not available
                else:# i!=isalpha():#ord(i)<65 or ord(i)>90 and ord(i)<97 or ord(i)>122:
                        return 4 #invalid characters used
	
def checkcuisine(cuisine):
	#print(type(cuisine))
	if len(str(cuisine))<3:
		return 1#too small name
	elif cuisine=="indian" or "italian" or "thai" or "chinese":
		return 3
	elif type(name)==str:
		if name.isalpha():#(name[i]>'a' and name[i]<'z') or (name[i]>'A' and name[i]<'Z') or (name[i]==' ' and i>0):
			return 2 #recipe not available
		else:
			return 4 #invalid characters used

		
