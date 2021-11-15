# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_l = name1.lower()
name2_l = name2.lower()

name1_score = 0
name2_score = 0
total = 0


name1_score += name1_l.count("t")
name1_score += name1_l.count("r")
name1_score += name1_l.count("u")
name1_score += name1_l.count("e")
name1_score += name1_l.count("l")
name1_score += name1_l.count("o")
name1_score += name1_l.count("v")
name1_score += name1_l.count("e")

name2_score += name2_l.count("t")
name2_score += name2_l.count("r")
name2_score += name2_l.count("u")
name2_score += name2_l.count("e")
name2_score += name2_l.count("l")
name2_score += name2_l.count("o")
name2_score += name2_l.count("v")
name2_score += name2_l.count("e")



total = int(str(name2_score) + str(name1_score))

if total < 10 or total > 90:
  print(f"Your score is {total}%, you go together like coke and mentos.")
elif total > 40 and total < 50:
  print(f"Your score is {total}%, you are alright together.")
else:
  print(f"Your score is {total}%.")