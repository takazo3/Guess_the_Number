from art import logo
from random import randint
from replit import clear
EASY_LEVEL = 10
HARD_LEVEL = 5
turns = 0
def check_answer(guess,answer,turns):
  if guess > answer:
    print("もっと下！")
    return turns - 1
  elif guess < answer:
    print("もっと上！")
    return turns - 1
  else:  
    print(f"ビンゴ！{guess}")
          
def set_difficulty():
  level =input("難易度：'easy'　or　'hard'を入力してね。:") 
  if level == "easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL
   


def game():  
  print(logo)
  print("数字あてゲームを始めるよ！\n１から100までの数字を当ててね!")
  answer = randint(1,100)
  # print(f"answer is {answer}")
  
  turns = set_difficulty()
   
  guess = 0
  while guess != answer:
    print(f"{turns}回試せるよ！")
    guess = int(input("どの数字？:"))
    turns = check_answer(guess, answer,turns)
    if turns == 0:
      print(f"ざんねん！答えは、{answer}でした。ゲームオーバー")
      return
    elif guess != answer:
      print("もう一回挑戦しよう！")
while input("もう一度チャレンジする? 'y' or 'n': ") == "y":
  clear()
  game()
