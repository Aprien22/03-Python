# Quiz Project
import random # Importing Libraries


question = { # Dictionarys "Key" : "Value"
    "What is the powerhouse of the cell?" : "Mitochondria",
    "The process of photosynthesis occurs in which part of the cell?" : "Chloroplast",
    "The main component of DNA is?" : "Nucleotide",
}

correct_responses = ["Correct +1 🥳", "You're on fire! 🔥", "Right answer! 👍"]

# Variables to keep track of the score and the user's response.
scores = 0
again = ''

name = (input("Hello, What's your name? ")).upper()
print("=" * 60)  # Separator line

while True:
    scores = 0
    
    # Shuffling the questions to randomize the order.
    question_items = list(question.items())
    random.shuffle(question_items)

    print(f"\nHello there {name}, Welcome to the QUIZ GAME!")
    print("DIRECTION: Please answer the following questions: \n")
    
    for questions, answer in question_items:
        print("=" * 60)  # Separator line
        user_answer = input(f"{questions} ").strip()
        
        # Re-prompt until user provides a non-empty response
        while not user_answer:
            print("Invalid response. Please provide an answer.")
            user_answer = input(f"{questions} ").strip()

        # Compare the response (case-insensitive, with minor flexibility)
        if user_answer.lower() == answer.lower() or user_answer.lower() == answer.lower() + 's':
            scores += 1
            print(random.choice(correct_responses))
        else:
            print(f"Sorry, the correct answer is {answer} 🥲")

   
    # Print the final score and the percentage of correct answers.
    print("=" * 60)
    print(f"\nYour final score is {scores}/{len(question)} 😁") # len() provide the number of items in question
    
    # Congratulatory messages
    if scores == len(question):
        print("Wow! Perfect score! You're a genius! 🎓")
    elif scores > len(question) / 2:
        print("Great job! You know your stuff! 🌟")
    else:
        print("Better luck next time! Keep learning! 💪")


    again = input("\nDo you want to play again? (Y/N) ").upper() # Ask if want to try again
    if again!= 'Y':
        print("Thanks for playing!") 
        break  # Exit if No




