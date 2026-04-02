#NUIST Quiz Game in Python
#name:Chen Sihan
#Date:2026/4/2
def quiz():
	print("Welcome to the Animal Quiz!")
	print("Answer the following questions:")

#Questions and Answers
	questions = [
		"1.What is the largest animal on Earth?: a. Blue Whale, b. Mouse, c. Cat",
		"2. Which bird can fly backwards?: a. Cuckoo,b.Eagle, c.Hummingbird",
		"3. What is the only mammal capable of flight?: a. Bat, b. Squirrel, c.Dolphin " 
		]
	correct_options = ["a","c","a"]
	full_answers = [
		"blue whale",
		"hummingbird",
		"bat"
		]
	score = 0

#Ask question
	for i in range(len(questions)):
		user_answer = input(questions[i]+"\nYour answer:").strip().lower()
		if user_answer == correct_options[i]:
			print("Correct!")
			score += 1
		else:
			print("Incorrect!")
#provide final score
	print("\nQuiz completed!")
	print(f"You got {score}/{len(questions)}questions correct.")

#run the quiz function
quiz()
