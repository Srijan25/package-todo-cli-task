import sys

def mainMenu():
     while True:
        print()
        print('''### TODO LIST ###

        Select a number for the action that you would like to do:

        1. ADD A NEW TODO
        2. SHOW REMAINING TODO
        3. DELETE A TODO
        4. COMPLETE A TODO
        5. SHOW USAGE
        6. STATISTICS
        7. Exit
        ''')

        selection = input("Make your selection: ")
        count=0
        if selection == "1":
            addItem()            
        elif selection == "2":
            displayList()
        elif selection == "3":
            removeItem()
        elif selection == "4":
            completeItem()
        elif selection == "5":
            listLength()
        elif selection == "6":
            listReport()
        elif selection == "7":
            sys.exit()
        else:
            print("You did not make a valid selection.")

l1 = input("ENTER YOUR TODO")
list1=[l1]



def addItem():
    item = input("Enter the item you wish to add to your todo list: ")
    list1.append(item)
    print(item + " has been added to the todo list.")

def displayList():
    print()
    print("--- TODO LIST ---")
    for i in list1:
        print("* " + i)


def removeItem():
    item = input("Enter the item you wish to remove from the todo list: ")
    list1.remove(item)
    print(item + " has been removed from the todo list.")

count1=0
def completeItem():
    
    while True:
        count=0
        item = int(input("What item would you like to complete on the todo list: "))
        print(list1[item-1]+"has been completed")
        list1.pop(item-1)           
        global count1
        count1=count+1
        
        break

     
def listLength():    
    print("There are", len(list1), "items on the todo list.")
    
def listReport():
      
            print("There are", len(list1), " todo left")
            print(count1 ,"todo completed")    


    
 

mainMenu()
