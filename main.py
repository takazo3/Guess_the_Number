from art import logo
from random import randint
from replit import clear
EASY_LEVEL = 10
HARD_LEVEL = 5
turns = 0
def check_answer(guess,answer,turns):
  if guess > answer:
    print("ãã£ã¨ä¸ð")
    return turns - 1
  elif guess < answer:
    print("ãã£ã¨ä¸ð")
    return turns - 1
  else:  
    print(f"ãã³ã´ð¥³{guess}ð¥³")
          
def set_difficulty():
  level =input("é£æåº¦ï¼'easy'ãorã'hard'ãå¥åãã¦ã­ã:") 
  if level == "easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL
   


def game():  
  print(logo)
  print("æ°å­ãã¦ã²ã¼ã ãå§ãããï¼\nï¼ãã100ã¾ã§ã®æ°å­ãå½ã¦ã¦ã­!")
  answer = randint(1,100)
  # print(f"answer is {answer}")
  
  turns = set_difficulty()
   
  guess = 0
  while guess != answer:
    print(f"{turns}åè©¦ãããï¼")
    guess = int(input("ã©ã®æ°å­ï¼:"))
    turns = check_answer(guess, answer,turns)
    if turns == 0:
      print(f"ããã­ãï¼ç­ãã¯ã{answer}ã§ãããðã²ã¼ã ãªã¼ãã¼ð")
      return
    elif guess != answer:
      print("ããä¸åææ¦ãããï¼")
while input("ããä¸åº¦ãã£ã¬ã³ã¸ãã? 'y' or 'n': ") == "y":
  clear()
  game()
