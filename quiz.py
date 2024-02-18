questions=["What is the capital of France?",
           "Which planet is known as the red planet?",
           "Who pained the mona lisa?"]

answers=["paris","mars","leonar do vinci"]

def run_quiz(questions,answers):
    print("Welcome to you from quiz game!")
    print("You can play game now!")
    while True:
        
        for i,question in enumerate (questions):
                score=0
     
                user_answer=input(f"{question}")
                if user_answer ==answers[i]:
                    print("You right!")
                    score += 1
                    print(f"You got {score} score in quiz game!")
            
        else:
            print("Wrong!")
        ans=input("Do you want to play game!:yes or no:")
        if ans == 'no'and ans == 'n':
            exit(0)
     
    
    

run_quiz(questions,answers)

    