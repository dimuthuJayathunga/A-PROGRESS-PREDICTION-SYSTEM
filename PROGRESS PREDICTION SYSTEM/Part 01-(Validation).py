
# Part 1 - Main Version - Question no:2 (Validation)

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID: 20210249

# Date: 26.11.2021 



# type_selector FUNCTION TO CHECK THE TYPE OF THE USER INPUT
def type_selector (mark):
    try:
        answer=int(mark)
        sign="true"
        return sign        
    except:
        print()
        print("------------------ \nInteger required  \n------------------")           

# range_check FUNCTION TO CHECK THE USER INPUT IN THE VALID RANGE
def range_check (value):
    if value not in ('0','00','20','40','60','80','100','120'):
        print()
        print("------------------ \nOut of range  \n------------------")
        
    else:
        sign="true"
        return sign

print()
    
while True:    
    
    # PASS CREDIT INPUT
    while True:
        pass_mark=input("Please Enter Your Credits At Pass : ")
        if type_selector (pass_mark) == "true" and range_check (pass_mark) == "true":
            break
        
    
    # DEFER CREDIT INPUT
    while True:
        defer_mark=input("Please Enter Your Credits At Defer : ")
        if type_selector (defer_mark) == "true" and range_check (defer_mark) == "true":
            break
     
    
    # FAIL CREDIT INPUT
    while True:
        fail_mark=input("Please Enter Your Credits At Fail : ")
        if type_selector (fail_mark) == "true" and range_check (fail_mark) == "true":
            break
                
        print()
    print()
    
    # CHANGE THE TYPE OF THE VARIABLES INTO INTEGER      
    pass_mark=int(pass_mark)
    defer_mark=int(defer_mark)
    fail_mark=int(fail_mark)
    
    # CALCULATING THE TOTAL CREDITS TO CHECK THE TOTAL
    total=pass_mark+defer_mark+fail_mark
    
    # CHECK WHETHER THE TOTAL IS CORRECT OR NOT
    if total != 120:
        print("------------------ \nTotal incorrect  \n------------------")
        continue
    
    # PROGRESSION OUTCOME SELECTION    
    else:
 
        if pass_mark == 120 :
            print("----------------------- \nProgress \n-----------------------")
            break
        elif pass_mark == 100:
            print("----------------------- \nProgress (module trailer) \n-----------------------")
            break
        elif pass_mark in (80, 60):
            print("------------------------------- \nDo not Progress – module retriever \n-------------------------------")
            break
        elif pass_mark == 40: 
            if defer_mark == 0: 
                print("----------------------- \nExclude \n-----------------------")
                break
            else:
                print("------------------------------- \nDo not Progress – module retriever \n-------------------------------")
                break
        elif pass_mark == 20:
            if defer_mark in (20, 00):
                print("----------------------- \nExclude \n-----------------------")
                break
            else:
                print("-------------------------------\nDo not Progress – module retriever \n-------------------------------")
                break
        elif pass_mark == 0:
            if defer_mark in (40, 20, 00):
                print("----------------------- \nExclude \n-----------------------")
                break
            else:
                print("-------------------------------\nDo not Progress – module retriever \n------------------------------- ")
                break
    

