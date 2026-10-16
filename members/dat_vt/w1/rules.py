user_input1 = input("Please enter your credits: ")
user_input2 = input("Please enter your grades: ")
credits = int(user_input1)
GPA = float(user_input2)
 


def can_register_thesis(credits: int, gpa: float):
    if credits >= 120 and gpa >= 2.0: return True
    else: return False


def missing(credits: int, gpa: float): 
    if(can_register_thesis(credits, gpa)): print("Can register thesis!")
    else: 
        if credits < 120: print("Need ", 120 - credits, " more credits")
        else: 
            if gpa < 2.0: print("Need ", 2.0 - gpa, " higher grades")

if __name__ == "__main__": 
    missing(credits, GPA)
