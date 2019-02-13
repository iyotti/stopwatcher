import os, sys, time
import tkinter as tk
from datetime import datetime,timedelta
import csv


class Work_time():
	def __init__(self):
		self.start_time = ""
		self.end_time   = ""
		self.in_status  = True
		self.out_status = False

	def in_work(self):
		if self.in_status == False: return

		time = datetime.now()
		s_time = time.strftime("%Y-%m-%d %H:%M")
		self.start_time = datetime.strptime(s_time,"%Y-%m-%d %H:%M")
		self.switch_status()
		print(self.start_time)

	def out_work(self):
		if self.out_status == False: return

		time = datetime.now()
		e_time = time.strftime("%Y-%m-%d %H:%M")
		self.end_time = datetime.strptime(e_time,"%Y-%m-%d %H:%M")
		self.switch_status()

		print("et",self.end_time)
		print("st",self.start_time)
		print(self.end_time-self.start_time)
		csv_list = [self.end_time-self.start_time,self.start_time,self.end_time]
		#csv_list = ["a","b","c"]
		csv_rw.output(csv_list)

	def switch_status(self):
		self.switch_in_status()
		self.switch_out_status()

	def switch_in_status(self):
		self.in_status = True if self.in_status == False else False

	def switch_out_status(self):
		self.out_status = True if self.out_status == False else False



class Csv_rw():
	def __init__(self,name):
		self.name = name
		os.makedirs("csv",exist_ok=True)


	def output(self,arr):
		print(self.name)
		csv_file = open(os.path.join('csv',self.name),'a',newline='')
		csv_writer = csv.writer(csv_file, delimiter=',')
		csv_writer.writerow(arr)
		csv_file.close()

timer = Work_time()
csv_rw = Csv_rw("inout.csv")


#メインウインドウ作成
root = tk.Tk()
root.title("タイマーだよ")
root.geometry("640x480")

in_button = tk.Button(root, text="出勤", width=10, command=timer.in_work,background='#ffffff')
in_button.place(x=220, y=240)
out_button= tk.Button(root, text="退勤", width=10, command=timer.out_work,background='#ffffff')
out_button.place(x=340, y=240)

#rootを表示し無限ループ　必須
root.mainloop()

