# Part 2 - (VERTICAL HISTOGRAM)

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID: 20210249

# Date: 28.11.2021 

print()

# SETTING VARIABLES
progress_count=0
trailer_count=0
retriever_count=0
exclude_count=0

outcomes_total=0

print()

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

# MAKE A LOOP TO REPEAT THE PROGRESSION OUTCOME PROCESS AGAIN AND AGAIN    
while True:        
    
    
    # PASS CREDIT INPUT
    while True:
        pass_mark=input("Enter your total PASS credits : ")
        if type_selector (pass_mark) == "true" and range_check (pass_mark) == "true":
            break
        
    
    # DEFER CREDIT INPUT
    while True:
        defer_mark=input("Enter your total DEFER credits : ")
        if type_selector (defer_mark) == "true" and range_check (defer_mark) == "true":
            break
      
    
    # FAIL CREDIT INPUT   
    while True:
        fail_mark=input("Enter your total FAIL credits : ")
        if type_selector (fail_mark) == "true" and range_check (fail_mark) == "true":
            break
                
        
    
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
        
        # CALCULATING THE TOTAL NUMBER OF OUTCOMES
        outcomes_total=outcomes_total+1
        
        if pass_mark == 120 :
            print("----------------------- \nProgress \n-----------------------")
            progress_count=progress_count+1
            
            
        elif pass_mark == 100:
            print("----------------------- \nProgress (module trailer) \n-----------------------")
            trailer_count=trailer_count+1
           
            
        elif pass_mark in (80, 60):
            print("------------------------------- \nModule retriever \n-------------------------------")
            retriever_count=retriever_count+1
         
            
        elif pass_mark == 40: 
            if defer_mark == 0: 
                print("----------------------- \nExclude \n-----------------------")
                exclude_count=exclude_count+1
               
                
            else:
                print("------------------------------- \nModule retriever \n-------------------------------")
                retriever_count=retriever_count+1
               
                
        elif pass_mark == 20:
            if defer_mark in (20, 00):
                print("----------------------- \nExclude \n-----------------------")
                exclude_count=exclude_count+1
              
                
            else:
                print("------------------------------- \nModule retriever \n-------------------------------")
                retriever_count=retriever_count+1
                
                
        elif pass_mark == 0:
            if defer_mark in (40, 20, 00):
                print("----------------------- \nExclude \n-----------------------")
                exclude_count=exclude_count+1
              
                
            else:
                print("------------------------------- \nModule retriever \n-------------------------------")
                retriever_count=retriever_count+1
               
                
    
    # ASKING FOR THE USER INPUT TO REPEAT THE PROGRESSION OUTCOME PROCESS
    print()
    print("Would you like to enter another set of data?")
    print()
    command=input("Enter 'y' for yes or 'q' to quit and view results:  ")
    print()
    if command == "q":
        break
    elif command == "y":
        continue

# CREATING A LIST FOR THE USE OF CONSTRUCTING HISOGRAM       
count_list=[[],[],[],[]]

# FILLING THE LIST (count_list) FOR THE USE OF CONSTRUCTING HISTOGRAM  
for count in range(progress_count):            
    count_list[0].append('*')

for count in range(trailer_count):              
    count_list[1].append('*')
        
for count in range(retriever_count):            
    count_list[2].append('*')

for count in range(exclude_count):
    count_list[3].append('*')


# THIS IS THE FIRST HORIZONTAL LINE OF THE VERTICAL HISTOGRAM   
print('----------------------------------------------------------')
print("Vertical Histogram")
header = ['Progress |', 'Trailer |', 'Retriever |', 'Exclude ']

# CONSTRUCTING AND DISPLAYING THE VERTICAL HISTOGRAM
print(' '.join(header))
for x in range(max(progress_count, trailer_count, retriever_count, exclude_count)):
    print("    {0}         {1}          {2}          {3}".format(
        '*' if x < progress_count else ' ',
        '*' if x < trailer_count else ' ',
        '*' if x < retriever_count else ' ',
        '*' if x < exclude_count else ' '
    ))
print()
# DISPLAYING THE TOTAL NUMBER OF OUTCOMES
print(outcomes_total," outcomes in total.")
print("----------------------------------------------------------")
