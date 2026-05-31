# with open  ("D:/Python/Chapter9/file.txt") as f:
#     content = f.read()
#     if ("twinkle"  in content):
#         print(content)
#     else:
#         print("The word 'twinkle' is not present in the file.")  
    
    
# import random

# def game():
#     print("You are playing the game..")

#     score = random.randint(1, 62)

#     with open("D:/Python/Chapter9/hiscore.txt") as f:
#         hiscore = f.read()

#     if hiscore == "":
#         hiscore = 0
#     else:
#         hiscore = int(hiscore)

#     print(f"Your score: {score}")
#     print(f"High score: {hiscore}")

#     if score > hiscore:
#         print("New High Score!")

#         with open("D:/Python/Chapter9/hiscore.txt", "w") as f:
#             f.write(str(score))

#     return score


# game()
# # genrate table 1 to 20
# def genratetable(n):
#  table =""
#  for i in range(1,11):
#   table+=f"{n} X {i}={n*i}\n"
  
#   with open(f"tables/table_{n}.txt","w")as f :
#       f.write(table) 
# for i in range(1,21):
#     genratetable(i)      

word = "Donkey"

with open("D:/Python/Chapter9/file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "Zebra")

with open("D:/Python/Chapter9/file.txt", "w") as f:
    f.write(contentNew)
print("Replacement done.")    