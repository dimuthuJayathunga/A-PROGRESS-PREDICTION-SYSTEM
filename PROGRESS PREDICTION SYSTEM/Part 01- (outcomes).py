
# Part 1 - Main Version - Question no:1 (Outcomes)

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID: 20210249

# Date: 25.11.2021 


print()

# USER INPUTS
pass_mark=int(input("Please Enter Your Credits At Pass = "))
print()
defer_mark=int(input("Please Enter Your Credits At Defer = "))
print()
fail_mark=int(input("Please Enter Your Credits At Fail = "))
print()

# PROGRESSION OUTCOME SELECTION
if pass_mark == 120 :
    print("----------------------- \nProgress\n-----------------------")
elif pass_mark == 100:
    print("----------------------- \nProgress (module trailer)\n-----------------------")
elif pass_mark in (80, 60):
    print("----------------------- \nmodule retriever\n-----------------------")
elif pass_mark == 40: 
    if defer_mark == 0: 
        print("----------------------- \nExclude\n-----------------------")
    else:
        print("-----------------------\nmodule retriever\n-----------------------")
elif pass_mark == 20:
    if defer_mark in (20, 00):
        print("----------------------- \nExclude\n-----------------------")
    else:
        print("-----------------------\nmodule retriever \n-----------------------")
elif pass_mark == 0:
    if defer_mark in (40, 20, 00):
        print("----------------------- \nExclude\n-----------------------")
    else:
        print("-----------------------\nmodule retriever\n-----------------------")

