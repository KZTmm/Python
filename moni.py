import random
student_list=["alice","bob","charlie","david","eva","frank"]

def choose_monitor(students):
    
    
    if not students:
        print("no students provided.")
        return
    monitors=random.choice(students)
    print(f"the class monitor is {monitors}")

choose_monitor(student_list)    