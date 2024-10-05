# import os

# if __name__ == '__main__':
#     print("Welcome to the Robo Speaker")
#     while True:
#         x = input("Enter what you want to speak : ")
#         if x=="q":
#             break
#         command=f"say  + {x}"
#         os.system(command)

# from win32com.client import Dispatch # type: ignore

# speak = Dispatch("SAPI.SpVoice").Speak

# speak("Ciao")

# import requests
# city=input("City : ")
# url=f"http://api.weatherapi.com/v1/current.json?key=b13989793f184149a9114153823010&q={city}"
# r=request.get(url)


# age=int(input("Enter teh age : "))
# if (age>18):
#     print("You can drive")
# else:
#     print("Not to drive")


# for i in range(1,11):
#     print(5*i )
# pip install schedule

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import schedule
# import time

# def send_email():
#     # Email Configuration
#     sender_email = "your_email@gmail.com"
#     sender_password = "your_password"
#     receiver_email = "recipient_email@example.com"
    
#     # Email Content
#     subject = "Daily Report"
#     body = "This is your daily report email."
    
#     # Setup Email
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message["Subject"] = subject
#     message.attach(MIMEText(body, "plain"))
    
#     # Connect to SMTP Server
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#         server.login(sender_email, sender_password)
#         server.sendmail(sender_email, receiver_email, message.as_string())
#     print("Email sent successfully.")

# # Schedule the Email to be Sent Daily
# schedule.every().day.at("09:00").do(send_email)

# # Main Loop
# while True:
#     schedule.run_pending()
#     time.sleep(1)



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# class InstagramBot:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.driver = webdriver.Chrome()  # You need to have Chrome webdriver installed and in your PATH

#     def login(self):
#         self.driver.get("https://www.instagram.com/")
#         time.sleep(2)  # Let the page load
#         username_input = self.driver.find_element_by_name("username")
#         password_input = self.driver.find_element_by_name("password")
#         username_input.send_keys(self.username)
#         password_input.send_keys(self.password)
#         password_input.send_keys(Keys.ENTER)
#         time.sleep(4)  # Let the page load

#     def like_posts(self, hashtag):
#         self.driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
#         time.sleep(5)  # Let the page load
#         for i in range(1, 4):
#             self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(2)  # Let the page scroll
#         hrefs = self.driver.find_elements_by_tag_name('a')
#         post_hrefs = [elem.get_attribute('href') for elem in hrefs if '/p/' in elem.get_attribute('href')]
#         for post_href in post_hrefs:
#             self.driver.get(post_href)
#             time.sleep(2)  # Let the page load
#             like_button = self.driver.find_element_by_xpath('//span[@aria-label="Like"]')
#             like_button.click()
#             time.sleep(18)  # Wait before liking next post

#     def close(self):
#         self.driver.quit()

# # Usage
# username = "YourInstagramUsername"
# password = "YourInstagramPassword"
# bot = InstagramBot(username, password)
# bot.login()
# bot.like_posts("nature")  # Replace "nature" with any hashtag you want to like posts from
# bot.close()




# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Generate some sample data
# np.random.seed(0)
# x = np.random.normal(size=1000)
# y = np.random.normal(size=1000)

# # Create a DataFrame
# data = pd.DataFrame({'X': x, 'Y': y})

# # Scatter plot
# plt.figure(figsize=(8, 6))
# plt.scatter(data['X'], data['Y'], alpha=0.5)
# plt.title('Scatter Plot')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# # Histogram and density plot
# plt.figure(figsize=(8, 6))
# sns.distplot(data['X'], bins=30, color='skyblue', kde=True, hist_kws={'edgecolor':'black'})
# plt.title('Histogram and Density Plot of X')
# plt.xlabel('X')
# plt.ylabel('Density')
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# # Box plot
# plt.figure(figsize=(8, 6))
# sns.boxenplot(data=data, x='X')
# plt.title('Box Plot of X')
# plt.xlabel('X')
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# # Violin plot
# plt.figure(figsize=(8, 6))
# sns.violinplot(data=data, y='Y')
# plt.title('Violin Plot of Y')
# plt.ylabel('Y')
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# # Pairplot
# plt.figure(figsize=(8, 6))
# sns.pairplot(data)
# plt.suptitle('Pairplot of X and Y', y=1.02)
# plt


# a = int(input("Enter the value of a : "));
# b = int(input("Enter the value of b : "));
# c = int(input("Enter the value of c : "));
# d = int(input("Enter the value of d : "));
# e = a+b+c;
# print(e)




# email = input("Enter Your Email: ").strip()

# username = email[:email.index('@')]
# domain = email[email.index('@') + 1:]

# print(f"Your username is {username} & domain is {domain}")




# # Run "pip install pyqrcode" before running this program
# import pyqrcode

# data = input("Enter the text or link to generate QR code: ")

# # Using pyqrcode.create() to create a qr code of the input data 
# qr = pyqrcode.create(data)

# # Using .svg method to save the qr code as SVG file of provided name & scale 
# qr.svg('qr_code.svg', scale = 8)




# import random

# # Storing random data into lists to create story.
# when = ['A long time ago', 'Yesterday', 'Before you were born', 'In future', 'Before Thanos arrived']
# who = ['Shazam', 'Iron Man', 'Batman', 'Superman', 'Captain America']
# went = ['Arkham Asylum', 'Gotham City', 'Stark Tower', 'Bat Cave', 'Avengers HQ']
# what = ['to eat a lot of cakes', 'to fight for justice', 'to steal ice cream', 'to dance']

# # Using string concatenition & randome.choice() to print a random element from all the lists 
# print(random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(went) + ' ' + random.choice(what) + '.')





    # # ==== Importing all necessary libraries for PythonGeeks Python 2048 Game
    # from tkinter import *
    # import random
    # # ==== creating main class
    # class Play_2048(Tk):

    # # ==== adding necessary class variables
    # game_board = []
    # new_random_tiles = [2, 2, 2, 2, 2, 2, 4]
    # score = 0
    # high_score = 0
    # game_score = 0
    # highest_score = 0

    # # ==== creating user window
    # def __init__(self, *args, **kwargs):
    #     Tk.__init__(self, *args, **kwargs)
    #     # ==== create user interface
    #     self.game_score = StringVar(self)
    #     self.game_score.set("0")
    #     self.highest_score = StringVar(self)
    #     self.highest_score.set("0")

    #     # ==== adding new game , score and highest score option
    #     self.button_frame = Frame(self)
    #     self.button_frame.grid(row=2, column=0, columnspan=4)
    #     Button(self.button_frame, text="New Game", font=("times new roman", 15), command=self.new_game).grid(row=0, column=0)
    #     self.button_frame.pack(side="top")

    #     Label(self.button_frame, text="Score:", font=("times new roman", 15)).grid(row=0, column=1)
    #     Label(self.button_frame, textvariable=self.game_score, font=("times new roman", 15)).grid(row=0, column=2)
    #     Label(self.button_frame, text="Record:", font=("times new roman", 15)).grid(row=0, column=3)
    #     Label(self.button_frame, textvariable=self.highest_score, font=("times new roman", 15)).grid(row=0, column=4)

    #     self.canvas = Canvas(self, width=410, height=410, borderwidth=5, highlightthickness=0)
    #     self.canvas.pack(side="top", fill="both", expand="false")

    #     # ==== create new game
    #     self.new_game()
        
    #     # ==== add new tiles in python 2048 game
    # def new_tiles(self):
    #     index = random.randint(0, 6)
    #     x = -1
    #     y = -1

    #     # ==== check while game is not over
    #     while self.full() == False:
    #         x = random.randint(0, 3)
    #         y = random.randint(0, 3)

    #         if (self.game_board[x][y] == 0):
    #             self.game_board[x][y] = self.new_random_tiles[index]
    #             x1 = y * 105
    #             y1 = x * 105
    #             x2 = x1 + 105 - 5
    #             y2 = y1 + 105 - 5
    #             num = self.game_board[x][y]
    #             if num == 2:
    #                 self.square[x, y] = self.canvas.create_rectangle(x1, y1, x2, y2, fill="#e0f2f8", tags="rect",
    #                                                                 outline="", width=0)
    #                 self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, font=("Arial", 36), fill="#f78a8a", text="2")
    #             elif num == 4:
    #                 self.square[x, y] = self.canvas.create_rectangle(x1, y1, x2, y2, fill="#b8dbe5", tags="rect",
    #                                                                 outline="", width=0)
    #                 self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, font=("Arial", 36), fill="#f78a8a", text="4")

    #             Break
                
    # # ==== showing game board
    # def show_board(self):
    #     cellwidth = 105
    #     cellheight = 105
    #     self.square = {}

    #     for column in range(4):
    #         for row in range(4):
    #             x1 = column * cellwidth
    #             y1 = row * cellheight
    #             x2 = x1 + cellwidth - 5
    #                 y2 = y1 + cellheight - 5
    #                 num = self.game_board[row]<div class="grid one-third"></div>
    #                 if num == 0:
    #                     self.show_number0(row, column, x1, y1, x2, y2)
    #                 else:
    #                     self.show_number(row, column, x1, y1, x2, y2, num)

    # # ==== showing game board in python 2048 game
    # def show_board(self):
    #     cellwidth = 105
    #     cellheight = 105
    #     self.square = {}

    #     for column in range(4):
    #         for row in range(4):
    #             x1 = column * cellwidth
    #             y1 = row * cellheight
    #             x2 = x1 + cellwidth - 5
    #             y2 = y1 + cellheight - 5
    #             num = self.game_board[row]<div class="grid one-third"></div>
    #             if num == 0:
    #                 self.show_number0(row, column, x1, y1, x2, y2)
    #             else:
    #                 self.show_number(row, column, x1, y1, x2, y2, num)
    # # ==== show board block when it is empty
    # def show_number0(self, row, column, a, b, c, d):
    #     self.square[row, column] = self.canvas.create_rectangle(a, b, c, d, fill="#f5f5f5", tags="rect", outline="")

    # # ==== show board number
    # def show_number(self, row, column, a, b, c, d, num):
    #     bg_color = {'2': '#eee4da', '4': '#ede0c8', '8': '#edc850', '16': '#edc53f', '32': '#f67c5f', '64': '#f65e3b', '128': '#edcf72', '256': '#edcc61', '512': '#f2b179', '1024': '#f59563', '2048': '#edc22e',}
    #     color = {'2': '#776e65', '4': '#f9f6f2', '8': '#f9f6f2', '16': '#f9f6f2', '32': '#f9f6f2', '64': '#f9f6f2', '128': '#f9f6f2', '256': '#f9f6f2', '512': '#776e65', '1024': '#f9f6f2', '2048': '#f9f6f2', }
    #     self.square[row, column] = self.canvas.create_rectangle(a, b, c, d, fill=bg_color[str(num)], tags="rect", outline="")
    #     self.canvas.create_text((a + c) / 2, (b + d) / 2, font=("Arial", 36), fill=color[str(num)], text=str(num))
        
    # # ==== moves by user
    # def moves(self, event):

    #     if event.keysym == 'Down':
    #         for j in range(0, 4):
    #             shift = 0
    #             for i in range(3, -1, -1):
    #                 if self.game_board[i][j] == 0:
    #                     shift += 1
    #                 else:
    #                     if i - 1 >= 0 and self.game_board[i - 1][j] == self.game_board[i][j]:
    #                         self.game_board[i][j] *= 2
    #                         self.score += self.game_board[i][j]
    #                         self.game_board[i - 1][j] = 0
    #                     elif i - 2 >= 0 and self.game_board[i - 1][j] == 0 and self.game_board[i - 2][j] == self.game_board[i][j]:
    #                         self.game_board[i][j] *= 2
    #                         self.score += self.game_board[i][j]
    #                         self.game_board[i - 2][j] = 0
    #                     elif i == 3 and self.game_board[2][j] + self.game_board[1][j] == 0 and self.game_board[0][j] == self.game_board[3][
    #                         j]:
    #                         self.game_board[3][j] *= 2
    #                         self.score += self.game_board[3][j]
    #                         self.game_board[0][j] = 0
    #                     if shift > 0:
    #                         self.game_board[i + shift][j] = self.game_board[i][j]
    #                         self.game_board[i][j] = 0
    #         self.show_board()
    #         self.new_tiles()
    #         self.game_over()
    #     elif event.keysym == 'Right':
    #         for i in range(0, 4):
    #             shift = 0
    #             for j in range(3, -1, -1):
    #                 if self.game_board[i][j] == 0:
    #                     shift += 1
    #                 else:
    #                     if j - 1 >= 0 and self.game_board[i][j - 1] == self.game_board[i][j]:
    #                         self.game_board[i][j] *= 2
    #                         self.score += self.game_board[i][j]
    #                         self.game_board[i][j - 1] = 0
    #                     elif j - 2 >= 0 and self.game_board[i][j - 1] == 0 and self.game_board[i][j - 2] == self.game_board[i][j]:
    #                         self.game_board[i][j] *= 2
    #                         self.score += self.game_board[i][j]
    #                         self.game_board[i][j - 2] = 0
    #                     elif j == 3 and self.game_board[i][2] + self.game_board[i][1] == 0 and self.game_board[0][j] == self.game_board[3][
    #                         j]:
    #                         self.game_board[i][3] *= 2
    #                         self.score += self.game_board[i][3]
    #                         self.game_board[i][0] = 0
    #                     if shift > 0:
    #                         self.game_board[i][j + shift] = self.game_board[i][j]
    #                         self.game_board[i][j] = 0
    #         self.show_board()
    #         self.new_tiles()
    #         self.game_over()
    #     elif event.keysym == 'Left':
    #         for i in range(0, 4):
    #             shift = 0
    #             for j in range(0, 4):
    #                 if self.game_board[i][j] == 0:
    #                     shift += 1
    #                 else:
    #                     if j + 1 < 4 and self.game_board[i][j + 1] == self.game_board[i][j]:
    #                         self.game_board[i][j] *= 2
    #                         self.score += self.game_board[i][j]
    #                         self.game_board[i][j + 1] = 0
    #                     elif j + 2 < 4 and self.game_board[i][j + 1] == 0 and self.game_board[i][j + 2] == self.game_board[i][j]:
    #                         self.game_board[i][j] *= 2
    #                         self.score += self.game_board[i][j]
    #                         self.game_board[i][j + 2] = 0
    #                     elif j == 0 and self.game_board[i][1] + self.game_board[i][2] == 0 and self.game_board[i][3] == self.game_board[i][
    #                         0]:
    #                         self.game_board[i][0] *= 2
    #                         self.score += self.game_board[i][0]
    #                         self.game_board[i][3] = 0
    #                     if shift > 0:
    #                         self.game_board[i][j - shift] = self.game_board[i][j]
    #                         self.game_board[i][j] = 0
    #         self.show_board()
    #         self.new_tiles()
    #         self.game_over()
    #     elif event.keysym == 'Up':
    #         for j in range(0, 4):
    #             shift = 0
    #             for i in range(0, 4):
    #                 if self.game_board[i][j] == 0:
    #                     shift += 1
    #                 else:
    #                     if i + 1 < 4 and self.game_board[i + 1][j] == self.game_board[i][j]:
    #                         self.game_board[i][j] *= 2
    #                         self.score += self.game_board[i][j]
    #                         self.game_board[i + 1][j] = 0
    #                     elif i + 2 < 4 and self.game_board[i + 1][j] == 0 and self.game_board[i + 2][j] == self.game_board[i][j]:
    #                         self.game_board[i][j] *= 2
    #                         self.score += self.game_board[i][j]
    #                         self.game_board[i + 2][j] = 0
    #                     elif i == 0 and self.game_board[1][j] + self.game_board[2][j] == 0 and self.game_board[3][j] == self.game_board[0][
    #                         j]:
    #                         self.game_board[0][j] *= 2
    #                         self.score += self.game_board[0][j]
    #                         self.game_board[3][j] = 0
    #                     if shift > 0:
    #                         self.game_board[i - shift][j] = self.game_board[i][j]
    #                         self.game_board[i][j] = 0
    #         self.show_board()
    #         self.new_tiles()
    #         self.game_over()

    #     self.game_score.set(str(self.score))
    #     if self.score > self.high_score:
    #         self.high_score = self.score
    #         self.highest_score.set(str(self.high_score))

    # # ==== to create new python 2048 game
    # def new_game(self):
    #     self.score = 0
    #     self.game_score.set("0")
    #     self.game_board = []
    #     self.game_board.append([0, 0, 0, 0])
    #     self.game_board.append([0, 0, 0, 0])
    #     self.game_board.append([0, 0, 0, 0])
    #     self.game_board.append([0, 0, 0, 0])
    #     while True:
    #         x = random.randint(0, 3)
    #         y = random.randint(0, 3)
    #         if (self.game_board[x][y] == 0):
    #             self.game_board[x][y] = 2
    #             break

    #     index = random.randint(0, 6)
    #     while self.full() == False:
    #         x = random.randint(0, 3)
    #         y = random.randint(0, 3)
    #         if (self.game_board[x][y] == 0):
    #             self.game_board[x][y] = self.new_random_tiles[index]
    #             break
    #     self.show_board()
        
    # # ==== check for game over
    # def game_over(self):
    #     for i in range(0, 4):
    #         for j in range(0, 4):
    #             if (self.game_board[i][j] == 2048):
    #                 self.game_won()
    #     for i in range(0, 4):
    #         for j in range(0, 4):
    #             if (self.game_board[i][j] == 0):
    #                 return False
    #     for i in range(0, 4):
    #         for j in range(0, 3):
    #             if (self.game_board[i][j] == self.game_board[i][j + 1]):
    #                 return False
    #     for j in range(0, 4):
    #         for i in range(0, 3):
    #             if self.game_board[i][j] == self.game_board[i + 1][j]:
    #                 return False
    #     gameover = [["G", "A", "M", "E", ], ["", "", "", ""], ["O", "V", "E", "R"], ["", "", "", ""]]
    #     cellwidth = 105
    #     cellheight = 105
    #     self.square = {}

    #     for column in range(4):
    #         for row in range(4):
    #             a = column * cellwidth
    #             b = row * cellheight
    #             c = a + cellwidth - 5
    #             d = b + cellheight - 5
    #             self.square[row, column] = self.canvas.create_rectangle(a, b, c, d, fill="#ede0c8", tags="rect",
    #                                                                     outline="")
    #             self.canvas.create_text((a + c) / 2, (b + d) / 2, font=("Arial", 36), fill="#494949",
    #                                     text=gameover[row]<div class="grid one-third"></div>)
    #     return True
    
    # # ==== check for game won
    # def game_won(self):
    #     gameover = [["Y", "O", "U", "", ], ["", "", "", ""], ["W", "O", "N", "!"], ["", "", "", ""]]
    #     cellwidth = 105
    #     cellheight = 105
    #     self.square = {}
    #     for column in range(4):
    #         for row in range(4):
    #             a = column * cellwidth
    #             b = row * cellheight
    #             c = a + cellwidth - 5
    #             d = b + cellheight - 5
    #             self.square[row, column] = self.canvas.create_rectangle(a, b, c, d, fill="#ede0c8", tags="rect",
    #                                                                     outline="")
    #             self.canvas.create_text((a + c) / 2, (b + d) / 2, font=("Arial", 36), fill="#494949",
    #                                     text=gameover[row]<div class="grid one-third"></div>)
                
    # if __name__ == "__main__":
    # # ==== preparing main window
    # app = Play_2048()
    # app.bind_all('<Key>', app.moves)
    # app.wm_title("2048 by PythonGeeks")
    # app.minsize(430, 470)
    # app.mainloop()
    
    
    
    
    
    
    
# import tkinter as tk
# from tkinter import messagebox
# from time import gmtime, strftime


# def is_number(s):
#     try:
#         float(s)
#         return 1
#     except ValueError:
#         return 0

# def check_acc_nmb(num):
# 	try:
# 		fpin=open(num+".txt",'r')
# 	except FileNotFoundError:
# 		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
# 		return 0
# 	fpin.close()
# 	return 

# def home_return(master):
# 	master.destroy()
# 	Main_Menu()

# def write(master,name,oc,pin):
	
# 	if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)or name==""):
# 		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
# 		master.destroy()
# 		return 

# 	f1=open("Accnt_Record.txt",'r')
# 	accnt_no=int(f1.readline())
# 	accnt_no+=1
# 	f1.close()

# 	f1=open("Accnt_Record.txt",'w')
# 	f1.write(str(accnt_no))
# 	f1.close()

# 	fdet=open(str(accnt_no)+".txt","w")
# 	fdet.write(pin+"\n")
# 	fdet.write(oc+"\n")
# 	fdet.write(str(accnt_no)+"\n")
# 	fdet.write(name+"\n")
# 	fdet.close()

# 	frec=open(str(accnt_no)+"-rec.txt",'w')
# 	frec.write("Date                             Credit      Debit     Balance\n")
# 	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+oc+"              "+oc+"\n")
# 	frec.close()
	
# 	messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
# 	master.destroy()
# 	return

# def crdt_write(master,amt,accnt,name):

# 	if(is_number(amt)==0):
# 		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
# 		master.destroy()
# 		return 

# 	fdet=open(accnt+".txt",'r')
# 	pin=fdet.readline()
# 	camt=int(fdet.readline())
# 	fdet.close()
# 	amti=int(amt)
# 	cb=amti+camt
# 	fdet=open(accnt+".txt",'w')
# 	fdet.write(pin)
# 	fdet.write(str(cb)+"\n")
# 	fdet.write(accnt+"\n")
# 	fdet.write(name+"\n")
# 	fdet.close()
# 	frec=open(str(accnt)+"-rec.txt",'a+')
# 	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+str(amti)+"              "+str(cb)+"\n")
# 	frec.close()
# 	messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
# 	master.destroy()
# 	return

# def debit_write(master,amt,accnt,name):

# 	if(is_number(amt)==0):
# 		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
# 		master.destroy()
# 		return 
			
# 	fdet=open(accnt+".txt",'r')
# 	pin=fdet.readline()
# 	camt=int(fdet.readline())
# 	fdet.close()
# 	if(int(amt)>camt):
# 		messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
# 	else:
# 		amti=int(amt)
# 		cb=camt-amti
# 		fdet=open(accnt+".txt",'w')
# 		fdet.write(pin)
# 		fdet.write(str(cb)+"\n")
# 		fdet.write(accnt+"\n")
# 		fdet.write(name+"\n")
# 		fdet.close()
# 		frec=open(str(accnt)+"-rec.txt",'a+')
# 		frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"              "+str(amti)+"              "+str(cb)+"\n")
# 		frec.close()
# 		messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
# 		master.destroy()
# 		return

# def Cr_Amt(accnt,name):
# 	creditwn=tk.Tk()
# 	creditwn.geometry("600x300") 
# 	creditwn.title("Credit Amount")
# 	creditwn.configure(bg="SteelBlue1")
# 	fr1=tk.Frame(creditwn,bg="blue")
# 	l_title=tk.Message(creditwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
# 	l_title.config(font=("Arial","50","bold"))
# 	l_title.pack(side="top")
# 	l1=tk.Label(creditwn,relief="raised",font=("Times",16),text="Enter Amount to be credited: ")
# 	e1=tk.Entry(creditwn,relief="raised")
# 	l1.pack(side="top")
# 	e1.pack(side="top")
# 	b=tk.Button(creditwn,text="Credit",font=("Times",16),relief="raised",command=lambda:crdt_write(creditwn,e1.get(),accnt,name))
# 	b.pack(side="top")
# 	creditwn.bind("<Return>",lambda x:crdt_write(creditwn,e1.get(),accnt,name))


# def De_Amt(accnt,name):
# 	debitwn=tk.Tk()
# 	debitwn.geometry("600x300")
# 	debitwn.title("Debit Amount")	
# 	debitwn.configure(bg="SteelBlue1")
# 	fr1=tk.Frame(debitwn,bg="blue")
# 	l_title=tk.Message(debitwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
# 	l_title.config(font=("Arial","50","bold"))
# 	l_title.pack(side="top")
# 	l1=tk.Label(debitwn,relief="raised",font=("Times",16),text="Enter Amount to be debited: ")
# 	e1=tk.Entry(debitwn,relief="raised")
# 	l1.pack(side="top")
# 	e1.pack(side="top")
# 	b=tk.Button(debitwn,text="Debit",font=("Times",16),relief="raised",command=lambda:debit_write(debitwn,e1.get(),accnt,name))
# 	b.pack(side="top")
# 	debitwn.bind("<Return>",lambda x:debit_write(debitwn,e1.get(),accnt,name))




# def disp_bal(accnt):
# 	fdet=open(accnt+".txt",'r')
# 	fdet.readline()
# 	bal=fdet.readline()
# 	fdet.close()
# 	messagebox.showinfo("Balance",bal)




# def disp_tr_hist(accnt):
# 	disp_wn=tk.Tk()
# 	disp_wn.geometry("900x600")
# 	disp_wn.title("Transaction History")
# 	disp_wn.configure(bg="SteelBlue1")
# 	fr1=tk.Frame(disp_wn,bg="blue")
# 	l_title=tk.Message(disp_wn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
# 	l_title.config(font=("Arial","50","bold"))
# 	l_title.pack(side="top")
# 	fr1=tk.Frame(disp_wn)
# 	fr1.pack(side="top")
# 	l1=tk.Message(disp_wn,text="Your Transaction History:",font=("Times",16),padx=100,pady=20,width=1000,bg="blue4",fg="SteelBlue1",relief="raised")
# 	l1.pack(side="top")
# 	fr2=tk.Frame(disp_wn)
# 	fr2.pack(side="top")
# 	frec=open(accnt+"-rec.txt",'r')
# 	for line in frec:
# 		l=tk.Message(disp_wn,anchor="w",text=line,relief="raised",width=2000)
# 		l.pack(side="top")
# 	b=tk.Button(disp_wn,text="Quit",relief="raised",command=disp_wn.destroy)
# 	b.pack(side="top")
# 	frec.close()

# def logged_in_menu(accnt,name):
# 	rootwn=tk.Tk()
# 	rootwn.geometry("1600x500")
# 	rootwn.title("CopyAssignment Bank | Welcome - "+name)
# 	rootwn.configure(background='SteelBlue1')
# 	fr1=tk.Frame(rootwn)
# 	fr1.pack(side="top")
# 	l_title=tk.Message(rootwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
# 	l_title.config(font=("Arial","50","bold"))
# 	l_title.pack(side="top")
# 	label=tk.Label(text="Logged in as: "+name,relief="raised",bg="blue3",font=("Times",16),fg="white",anchor="center",justify="center")
# 	label.pack(side="top")
# 	img2=tk.PhotoImage(file="credit.gif")
# 	myimg2=img2.subsample(2,2)
# 	img3=tk.PhotoImage(file="debit.gif")
# 	myimg3=img3.subsample(2,2)
# 	img4=tk.PhotoImage(file="balance1.gif")
# 	myimg4=img4.subsample(2,2)
# 	img5=tk.PhotoImage(file="transaction.gif")
# 	myimg5=img5.subsample(2,2)
# 	b2=tk.Button(image=myimg2,command=lambda: Cr_Amt(accnt,name))
# 	b2.image=myimg2
# 	b3=tk.Button(image=myimg3,command=lambda: De_Amt(accnt,name))
# 	b3.image=myimg3
# 	b4=tk.Button(image=myimg4,command=lambda: disp_bal(accnt))
# 	b4.image=myimg4
# 	b5=tk.Button(image=myimg5,command=lambda: disp_tr_hist(accnt))
# 	b5.image=myimg5
	
# 	img6=tk.PhotoImage(file="logout.gif")
# 	myimg6=img6.subsample(2,2)
# 	b6=tk.Button(image=myimg6,relief="raised",command=lambda: logout(rootwn))
# 	b6.image=myimg6

	
# 	b2.place(x=100,y=150)
# 	b3.place(x=100,y=220)
# 	b4.place(x=900,y=150)
# 	b5.place(x=900,y=220)
# 	b6.place(x=500,y=400)

	
# def logout(master):
	
# 	messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
# 	master.destroy()
# 	Main_Menu()

# def check_log_in(master,name,acc_num,pin):
# 	if(check_acc_nmb(acc_num)==0):
# 		master.destroy()
# 		Main_Menu()
# 		return

# 	if( (is_number(name))  or (is_number(pin)==0) ):
# 		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
# 		master.destroy()
# 		Main_Menu()
# 	else:
# 		master.destroy()
# 		logged_in_menu(acc_num,name)


# def log_in(master):
# 	master.destroy()
# 	loginwn=tk.Tk()
# 	loginwn.geometry("600x300")
# 	loginwn.title("Log in")
# 	loginwn.configure(bg="SteelBlue1")
# 	fr1=tk.Frame(loginwn,bg="blue")
# 	l_title=tk.Message(loginwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
# 	l_title.config(font=("Arial","50","bold"))
# 	l_title.pack(side="top")
# 	l1=tk.Label(loginwn,text="Enter Name:",font=("Times",16),relief="raised")
# 	l1.pack(side="top")
# 	e1=tk.Entry(loginwn)
# 	e1.pack(side="top")
# 	l2=tk.Label(loginwn,text="Enter account number:",font=("Times",16),relief="raised")
# 	l2.pack(side="top")
# 	e2=tk.Entry(loginwn)
# 	e2.pack(side="top")
# 	l3=tk.Label(loginwn,text="Enter your PIN:",font=("Times",16),relief="raised")
# 	l3.pack(side="top")
# 	e3=tk.Entry(loginwn,show="*")
# 	e3.pack(side="top")
# 	b=tk.Button(loginwn,text="Submit",command=lambda: check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
# 	b.pack(side="top")
# 	b1=tk.Button(text="HOME",font=("Times",16),relief="raised",bg="blue4",fg="white",command=lambda: home_return(loginwn))
# 	b1.pack(side="top")
# 	loginwn.bind("<Return>",lambda x:check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	

# def Create():
	
# 	crwn=tk.Tk()
# 	crwn.geometry("600x300")
# 	crwn.title("Create Account")
# 	crwn.configure(bg="SteelBlue1")
# 	fr1=tk.Frame(crwn,bg="blue")
# 	l_title=tk.Message(crwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
# 	l_title.config(font=("Arial","50","bold"))
# 	l_title.pack(side="top")
# 	l1=tk.Label(crwn,text="Enter Name:",font=("Times",16),relief="raised")
# 	l1.pack(side="top")
# 	e1=tk.Entry(crwn)
# 	e1.pack(side="top")
# 	l2=tk.Label(crwn,text="Enter opening credit:",font=("Times",16),relief="raised")
# 	l2.pack(side="top")
# 	e2=tk.Entry(crwn)
# 	e2.pack(side="top")
# 	l3=tk.Label(crwn,text="Enter desired PIN:",font=("Times",16),relief="raised")
# 	l3.pack(side="top")
# 	e3=tk.Entry(crwn,show="*")
# 	e3.pack(side="top")
# 	b=tk.Button(crwn,text="Submit",font=("Times",16),command=lambda: write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
# 	b.pack(side="top")
# 	crwn.bind("<Return>",font=("Times",16),command=lambda x:write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
# 	return


# def Main_Menu():
# 	rootwn=tk.Tk()
# 	rootwn.geometry("1600x500")
# 	rootwn.title("Bank Management System - 	CopyAssignment")
# 	rootwn.configure(background='SteelBlue1')
# 	fr1=tk.Frame(rootwn)
# 	fr1.pack(side="top")
# 	l_title=tk.Message(text="BANK MANAGEMENT SYSTEM ",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
# 	l_title.config(font=("Verdana","40","bold"))
# 	l_title.pack(side="top")
# 	imgc1=tk.PhotoImage(file="new.gif")
# 	imglo=tk.PhotoImage(file="login.gif")
# 	imgc=imgc1.subsample(2,2)
# 	imglog=imglo.subsample(2,2)

# 	b1=tk.Button(image=imgc,command=Create)
# 	b1.image=imgc
# 	b2=tk.Button(image=imglog,command=lambda: log_in(rootwn))
# 	b2.image=imglog
# 	img6=tk.PhotoImage(file="quit.gif")
# 	myimg6=img6.subsample(2,2)

# 	b6=tk.Button(image=myimg6,command=rootwn.destroy)
# 	b6.image=myimg6
# 	b1.place(x=800,y=300)
# 	b2.place(x=800,y=200)	
# 	b6.place(x=920,y=400)

# 	rootwn.mainloop()

# Main_Menu()





# import re
# import tweepy
# from tweepy import OAuthHandler
# from textblob import TextBlob

# class TwitterClient(object):
# 	'''
# 	Generic Twitter Class for sentiment analysis.
# 	'''
# 	def __init__(self):
# 		'''
# 		Class constructor or initialization method.
# 		'''
# 		# keys and tokens from the Twitter Dev Console
# 		consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXX'
# 		consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# 		access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# 		access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

# 		# attempt authentication
# 		try:
# 			# create OAuthHandler object
# 			self.auth = OAuthHandler(consumer_key, consumer_secret)
# 			# set access token and secret
# 			self.auth.set_access_token(access_token, access_token_secret)
# 			# create tweepy API object to fetch tweets
# 			self.api = tweepy.API(self.auth)
# 		except:
# 			print("Error: Authentication Failed")

# 	def clean_tweet(self, tweet):
# 		'''
# 		Utility function to clean tweet text by removing links, special characters
# 		using simple regex statements.
# 		'''
# 		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])
# 									|(\w+:\/\/\S+)", " ", tweet).split())

# 	def get_tweet_sentiment(self, tweet):
# 		'''
# 		Utility function to classify sentiment of passed tweet
# 		using textblob's sentiment method
# 		'''
# 		# create TextBlob object of passed tweet text
# 		analysis = TextBlob(self.clean_tweet(tweet))
# 		# set sentiment
# 		if analysis.sentiment.polarity > 0:
# 			return 'positive'
# 		elif analysis.sentiment.polarity == 0:
# 			return 'neutral'
# 		else:
# 			return 'negative'

# 	def get_tweets(self, query, count = 10):
# 		'''
# 		Main function to fetch tweets and parse them.
# 		'''
# 		# empty list to store parsed tweets
# 		tweets = []

# 		try:
# 			# call twitter api to fetch tweets
# 			fetched_tweets = self.api.search(q = query, count = count)

# 			# parsing tweets one by one
# 			for tweet in fetched_tweets:
# 				# empty dictionary to store required params of a tweet
# 				parsed_tweet = {}

# 				# saving text of tweet
# 				parsed_tweet['text'] = tweet.text
# 				# saving sentiment of tweet
# 				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

# 				# appending parsed tweet to tweets list
# 				if tweet.retweet_count > 0:
# 					# if tweet has retweets, ensure that it is appended only once
# 					if parsed_tweet not in tweets:
# 						tweets.append(parsed_tweet)
# 				else:
# 					tweets.append(parsed_tweet)

# 			# return parsed tweets
# 			return tweets

# 		except tweepy.TweepError as e:
# 			# print error (if any)
# 			print("Error : " + str(e))

# def main():
# 	# creating object of TwitterClient Class
# 	api = TwitterClient()
# 	# calling function to get tweets
# 	tweets = api.get_tweets(query = 'Donald Trump', count = 200)

# 	# picking positive tweets from tweets
# 	ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
# 	# percentage of positive tweets
# 	print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
# 	# picking negative tweets from tweets
# 	ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
# 	# percentage of negative tweets
# 	print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
# 	# percentage of neutral tweets
# 	print("Neutral tweets percentage: {} % \
# 		".format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets)))

# 	# printing first 5 positive tweets
# 	print("\n\nPositive tweets:")
# 	for tweet in ptweets[:10]:
# 		print(tweet['text'])

# 	# printing first 5 negative tweets
# 	print("\n\nNegative tweets:")
# 	for tweet in ntweets[:10]:
# 		print(tweet['text'])

# if __name__ == "__main__":
# 	# calling main function
# 	main()




# from telegram.ext.updater import Updater 
# from telegram.update import Update 
# from telegram.ext.callbackcontext import CallbackContext 
# from telegram.ext.commandhandler import CommandHandler 
# from telegram.ext.messagehandler import MessageHandler 
# from telegram.ext.filters import Filters 

# updater = Updater("your_own_API_Token got from BotFather", 
# 				use_context=True) 


# def start(update: Update, context: CallbackContext): 
# 	update.message.reply_text( 
# 		"Hello sir, Welcome to the Bot.Please write\ 
# 		/help to see the commands available.") 

# def help(update: Update, context: CallbackContext): 
# 	update.message.reply_text("""Available Commands :- 
# 	/youtube - To get the youtube URL 
# 	/linkedin - To get the LinkedIn profile URL 
# 	/gmail - To get gmail URL 
# 	/geeks - To get the GeeksforGeeks URL""") 


# def gmail_url(update: Update, context: CallbackContext): 
# 	update.message.reply_text( 
# 		"Your gmail link here (I am not\ 
# 		giving mine one for security reasons)") 


# def youtube_url(update: Update, context: CallbackContext): 
# 	update.message.reply_text("Youtube Link =>\ 
# 	https://www.youtube.com/") 


# def linkedIn_url(update: Update, context: CallbackContext): 
# 	update.message.reply_text( 
# 		"LinkedIn URL => \ 
# 		https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/") 


# def geeks_url(update: Update, context: CallbackContext): 
# 	update.message.reply_text( 
# 		"GeeksforGeeks URL => https://www.geeksforgeeks.org/") 


# def unknown(update: Update, context: CallbackContext): 
# 	update.message.reply_text( 
# 		"Sorry '%s' is not a valid command" % update.message.text) 


# def unknown_text(update: Update, context: CallbackContext): 
# 	update.message.reply_text( 
# 		"Sorry I can't recognize you , you said '%s'" % update.message.text) 


# updater.dispatcher.add_handler(CommandHandler('start', start)) 
# updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url)) 
# updater.dispatcher.add_handler(CommandHandler('help', help)) 
# updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url)) 
# updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url)) 
# updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url)) 
# updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown)) 
# updater.dispatcher.add_handler(MessageHandler( 
# 	Filters.command, unknown)) # Filters out unknown commands 

# # Filters out unknown messages. 
# updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text)) 

# updater.start_polling() 





import random
import math

lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

x = random.randint(lower, upper)
print("\n\tYou've only ", 
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer!\n")

count = 0

while count < math.log(upper - lower + 1, 2):
	count += 1

	guess = int(input("Guess a number:- "))

	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")

