#additions

HEADER = "\033[95m"
FOOTER = "\033[95m"
OKGREEN = "\033[92m"
RULES = "\033[36m"
FAIL = "\033[91m"
ENDC = "\033[0m"
CLEAR_SCREEN = "\033[H\033[J"
MOVE_CURSOR_TO_BOTTOM = "\033[40D"
HEADER1 =(HEADER + "\n*--*--*--*--*--*--*--*--*--*--*--*--*--*--*\t"
          "\n\t\tTHE QUIZ GAME"
          "\n*--*--*--*--*--*--*--*--*--*--*--*--*--*--*\n" + ENDC)
FOOTER1 =(FOOTER + "\n*--*--*--**  MADE BY SARTHAK<3  **--*--*--*" + ENDC)

while True:
    #start with clear screen
    print(CLEAR_SCREEN, end="")
    print(HEADER1)
    print("Press:")
    print(" |1| - Start")
    print(" |2| - Stop\n")
    choice = int(input("Your choice: "))
    print(MOVE_CURSOR_TO_BOTTOM, FOOTER1)


    if choice == 1:
        #Clearing screen to start the game
        print(CLEAR_SCREEN, end="")

        #taking the name
        print(HEADER1)
        name = input("Enter your name: ").strip()
        score = 0

        #rules before starting the game
        print(CLEAR_SCREEN,end ="")
        print(HEADER1)
        print(RULES + "\n================= RULES =================\n")
        print("\t\t --> Players must answer by typing the correct option (e.g., A, B, C, or D).")
        print("\t\t --> Scoring: Each correct answer awards 1 point.")
        print("\t\t --> No negative marking for wrong answers.")
        print("\t\t --> The final score will be displayed at the end of the Quiz." + ENDC)
        print(MOVE_CURSOR_TO_BOTTOM, FOOTER1, "\n")
        input("Press Enter to start the quiz questions...")

        # Question 1
        print(CLEAR_SCREEN, end="")
        print(HEADER1)
        print(f"Name: {name} || Score: {score}\n")
        print("Question 1: Who discovered the law of gravitation?")
        print(" A) Albert Einstein")
        print(" B) Isaac Newton")
        print(" C) Galileo Galilei")
        print(" D) Johannes Kepler")
        answer = input("Your answer: ").strip().upper()
        if answer == "B":
            score += 1
            print(OKGREEN + "Correct!" + ENDC)
        else:
            print(FAIL + "Wrong! The correct answer is B) Isaac Newton." + ENDC)
        print(MOVE_CURSOR_TO_BOTTOM, FOOTER1, "\n")
        input("Press Enter to see the next question...")

        # Question 2
        print(CLEAR_SCREEN, end="")
        print(HEADER1)
        print(f"Name: {name} || Score: {score}\n")
        print("Question 2: Which is the largest desert in the world?")
        print(" A) Sahara Desert")
        print(" B) Arctic Desert")
        print(" C) Antarctic Desert")
        print(" D) Gobi Desert")
        answer = input("Your answer: ").strip().upper()
        if answer == "C":
            score += 1
            print(OKGREEN + "Correct!" + ENDC)
        else:
            print(FAIL + "Wrong! The correct answer is C) Antarctic Desert." + ENDC)
        print(MOVE_CURSOR_TO_BOTTOM, FOOTER1, "\n")
        input("Press Enter to see the next question...")

        # Question 3
        print(CLEAR_SCREEN, end="")
        print(HEADER1)
        print(f"Name: {name} || Score: {score}\n")
        print("Question 3: What is the smallest prime number?")
        print(" A) 0")
        print(" B) 1")
        print(" C) 2")
        print(" D) 3")
        answer = input("Your answer: ").strip().upper()
        if answer == "C":
            score += 1
            print(OKGREEN + "Correct!" + ENDC)
        else:
            print(FAIL + "Wrong! The correct answer is C) 2." + ENDC)
        print(MOVE_CURSOR_TO_BOTTOM, FOOTER1, "\n")
        input("Press Enter to see the next question...")

        # Question 4
        print(CLEAR_SCREEN, end="")
        print(HEADER1)
        print(f"Name: {name} || Score: {score}\n")
        print("Question 4: Which element has the highest melting point?")
        print(" A) Iron")
        print(" B) Tungsten")
        print(" C) Carbon")
        print(" D) Platinum")
        answer = input("Your answer: ").strip().upper()
        if answer == "B":
            score += 1
            print(OKGREEN + "Correct!" + ENDC)
        else:
            print(FAIL + "Wrong! The correct answer is B) Tungsten." + ENDC)
        print(MOVE_CURSOR_TO_BOTTOM, FOOTER1, "\n")
        input("Press Enter to see the next question...")

        # Question 5
        print(CLEAR_SCREEN, end="")
        print(HEADER1)
        print(f"Name: {name} || Score: {score}\n")
        print("Question 5: Who developed the theory of relativity?")
        print(" A) Nikola Tesla")
        print(" B) Isaac Newton")
        print(" C) Albert Einstein")
        print(" D) Marie Curie")
        answer = input("Your answer: ").strip().upper()
        if answer == "C":
            score += 1
            print(OKGREEN + "Correct!" + ENDC)
        else:
            print(FAIL + "Wrong! The correct answer is C) Albert Einstein." + ENDC)
        print(MOVE_CURSOR_TO_BOTTOM, FOOTER1, "\n")
        input("Press Enter to see the results...")

        # Final Score
        print(CLEAR_SCREEN, end="")
        print(HEADER1)
        print(f"Name: {name} || Final Score: {score}\n")
        print("Thanks for playing!\n\n")
        print(MOVE_CURSOR_TO_BOTTOM, FOOTER1, "\n")
        input("Press Enter to return to the menu...")

    elif choice == 2:
        # Exit the loop and stop the program
        print(CLEAR_SCREEN, end="")
        print("Goodbye! Thanks for playing the quiz.")
        print(MOVE_CURSOR_TO_BOTTOM, FOOTER1, "\n")
        break
    else:
        print("Invalid choice. Please choose 1 or 2.")

    if choice == 2:
        break

