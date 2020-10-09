
def showAll():
    #print("showAll")
    f = open("db.txt", "r")
    print(f.read())

def showByID():
    #print("showByID")
    
    ID = input("> ID?")
    while not valid("db.txt",ID):
        print("invalid ID")
        ID = input("> ID?")
    
    f = open("db.txt", "r")
    lines = f.readlines()
    for line in lines:
        if ID in line:
            print(line)
            break
    
def showByName():
    #print("showByName")
    
    name = input("> Name?")
    while not valid("db.txt",name):
        print("invalid Name")
        name = input("> Name?")
    
    f = open("db.txt", "r")
    lines = f.readlines()
    for line in lines:
        if name in line:
            print(line)
            break
    
    
    
def update():
    #print("update")
    
    ID = input("> ID?")
    while not valid("db.txt",ID):
        print("invalid ID")
        ID = input("> ID?")
        
        
    print("*****************************")
    print("***    UPDATE MENU        ***")
    print("* 1 Name    3 In Stock      *")
    print("* 2 Price   4 Exit          *")
    print("*****************************")
    
    ch = int(input("> "))
    f = open("db.txt", "r")
    lines = f.readlines()
    c = False
    while(ch != 4 ):
        if ch == 1:
           c =True
           new_name = input("> Name?") 
          
           for line in lines:
               if ID in line:
                   updated = line.replace(line.split()[0], new_name)
                   #print(updated)
                   f.close()
                   deleteLine("db.txt",ID)
                   break
               
           f = open("db.txt", "a")
           f.write("{}".format(updated))
           f.close()
           print("> Done")
           break
           
        elif ch == 2:
            c = True
            new_price = float(input("> Price?")) 
          
            for line in lines:
                if ID in line:
                    updated = line.replace(line.split()[2], str(new_price))
                    #print(updated)
                    f.close()
                    deleteLine("db.txt",ID)
                    break
               
            f = open("db.txt", "a")
            f.write("{}".format(updated))
            f.close()
            print("> Done")
            break
        
        elif ch == 3:
            c =True
            new_stock = int(input(">In Stock?")) 
          
            for line in lines:
                if ID in line:
                    updated = line.replace(line.split()[3], str(new_stock)) 
                    #print(updated)
                    #print(line)
                    f.close()
                    deleteLine("db.txt",ID)
                    break
               
            f = open("db.txt", "a")
            f.write("{}".format(updated))
            f.close()
            print("> Done")
            break
        
    else:
        if not c:
            print("> Update aborted")
             

def delete():
    #print("delete")
    
    ID = input("> ID?")
    while not valid("db.txt",ID):
        print("invalid ID")
        ID = input("> ID?")
    deleteLine("db.txt",ID)
    print("> Deleted")
    
    
    
def add():
    #print("add")
    
    name = input("> Name?")
    
    while(valid("db.txt",name)):
        print("> ERROR Name	EXISTS")
        name = input("Name?")
    
    ID = input("> ID?")
    print(len(ID))
    while(valid("db.txt",ID)):
        print("> ERROR ID	EXISTS")
        ID = input("ID?")
        print("> ID MUST BE 10 DIGIT")
    price = float(input("> PRICE?"))
    
    stock = int(input("> ADD STOCK?"))
    
    
    f = open("db.txt", "a")
    f.write("{} {} {} {} \n".format(name,ID,str(price),str(stock)))
    f.close()
    print('OK')


def valid(fname,txt):
    with open(fname) as f:
        return any(txt in line for line in f)



def deleteLine(fname, ID):
    #print("dataline")
    f = open(fname)
    output = []
    for line in f:
        if not ID in line:
            output.append(line)
    f.close()
    f = open(fname, 'w')
    f.writelines(output)
    f.close()
    #print("deletion done")






if __name__ == "__main__":
    
    print("*****************************")
    print("***WELCOME TO DATAMANAGER ***")
    print("***        MENU           ***")
    print("* 1 List All    4 Delete ID *")
    print("* 2 List ID     5 Update ID *")
    print("* 3 List Name   6 Add       *")
    print("* 7 Exit                    *")
    print("*****************************")
    
    ch = int(input("> "))
    
    while(ch != 7 ):
        if ch == 1:
            showAll()
            ch = int(input("> "))
            
        elif ch == 2:
            showByID()
            ch = int(input("> "))
            
        elif ch == 3:
            showByName()
            ch = int(input("> "))
            
        elif ch == 4:
            delete()
            ch = int(input("> "))
            
        elif ch == 5:
            update()
            ch = int(input("> "))
            
        elif ch == 6:
            add()
            ch = int(input("> "))
        
        else:
            print("Sorry!")
            ch = int(input("> "))
    else:
        print("bye")


