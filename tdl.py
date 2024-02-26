to_do_list=[]

def addtask():
    task = input("Please enter a task: ")
    to_do_list.append(task)
    print(f"Task {task} added to the list.")

def listtasks():
    if not to_do_list:
        print("There are no tasks currently.")
    else:
        print("Current tasks")
        for task in enumerate(to_do_list):
            print(f"Task {task}")

def removetask():
    listtasks()
    try:
      r_delete = int(input("Enter the to delete: "))
      if r_delete >= 0 and r_delete < len(to_do_list):
        to_do_list.pop(r_delete)
        print(f"Task {r_delete} has been removed.")
      else:
       print(f"Task {r_delete} was not found.")
    except:
       print("Invalid input.")

if __name__== "__main__":
   print("Welcome to the to the To Do List app")
   while True:
      print("\n")
      print("1.add a  task")
      print("2.remove a task.")
      print("3.display tasks.")
      print("4.quit.")

      choice = input("Enter your choice: ")

      if choice == "1":
         addtask()
      elif choice == "2":
         removetask()
      elif choice == "3":
         listtasks()
      elif choice == "4":
         break
      else:
         print("Please try again.")

print("Goodbye!")


