# Part 3 - List/Tuple/Directory (extension)

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID: 20210249

# Date: 04.12.2021 

# SETTING VARIABLES
progress_count=0
trailer_count=0
retriever_count=0
exclude_count=0

# List
progressList = []
trailerList = []
retriverList = []
excludedList = []

print()

def rangeChecker(inputCredit):
    if inputCredit in range(0,121,20):
        return True
    print("------------------ \nOut of range  \n------------------")
    
def progressionChecker(passCredits, deferCredits, failCredits):
    global progress_count,trailer_count,retriever_count,exclude_count

    if passCredits == 120:
        progressList.append(str(passCredits) + ", " + str(deferCredits) + ", " + str(failCredits))
        print("------------------ \nResult - Progress \n------------------")
        progress_count = progress_count + 1
        
    elif passCredits == 100:
        trailerList.append(str(passCredits) + ", " + str(deferCredits) + ", " + str(failCredits))
        print("----------------------------------- \nResult - Progress (module trailer) \n-----------------------------------")
        trailer_count = trailer_count + 1
        
    elif (passCredits == 40 and failCredits == 80) or (passCredits == 20 and (deferCredits <= 20)) or (passCredits == 0 and (failCredits >= 80)):
        excludedList.append(str(passCredits) + ", " + str(deferCredits) + ", " + str(failCredits))
        print("----------------- \nResult - Exclude \n-----------------")
        exclude_count = exclude_count + 1
        
    else:
        retriverList.append(str(passCredits) + ", " + str(deferCredits) + ", " + str(failCredits))
        print("-------------------------- \nResult - Module retriever \n--------------------------")
        retriever_count = retriever_count + 1

# Get passCredits,deferCredits,failCredits and Validation

def getUserInput():
    while True:
        try:
            while True:
                passCredits = int(input("Please enter your credits at pass: "))
                if rangeChecker(passCredits):
                    break

            while True:
                deferCredits = int(input("Please enter your credits at defer: "))
                if rangeChecker(deferCredits):
                    break
                
            while True:
                failCredits = int(input("Please enter your credits at fail: "))
                if rangeChecker(failCredits):
                    break
            
            if passCredits + deferCredits + failCredits != 120:
                print("------------------ \nTotal incorrect  \n------------------")
                continue

            progressionChecker(passCredits, deferCredits, failCredits)
            break

        except ValueError:
            print("------------------ \nInteger required  \n------------------")
            passCredits = 0
            deferCredits = 0
            failCredits = 0
            continue



# Display List

def printAllValues():
    print("\n------------------------------------------------------")
    for i in progressList:
        print("Progress -", i)

    for i in trailerList:
        print("Progress (module trailer) -", i)
    
    for i in retriverList:
        print("Module retriever -", i)
    
    for i in excludedList:
        print("Exclude -", i)
    print("--------------------------------------------------------")
    print()

# Result Menu 

def resultsMenu():
    onceLoop = False
    while True:
           printAllValues()
           break

while True:
    getUserInput()
    while True:
        print()
        wantLoop = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
        print()
        if wantLoop == 'y' or wantLoop == 'q':
            break
    if wantLoop == 'q':
        resultsMenu()
        break
