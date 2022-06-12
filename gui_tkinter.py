from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


class FirstScreen:

	def __init__(self, master):
		self.master = master
		self.master.title("Instagram unfollower")
		self.master.geometry("380x450")

	def add_image(self):
		image = Image.open("with_white.png")
		img = ImageTk.PhotoImage(image)

		# create label and add resize image
		label1 = Label(image=img)
		label1.image = img
		label1.pack(pady=15)

	def information_label(self):
		labe_name = ttk.Label(self.master, text="username:")
		labe_name.place(x=10, y=10)
		labe_email = ttk.Label(self.master, text="password:")
		labe_email.place(x=10, y=40)
		labe_email = ttk.Label(self.master, text="desired page:")
		labe_email.place(x=10, y=70)

	def information_entry(self):
		entry_name = ttk.Entry(self.master, width=30)
		entry_name.place(x=100, y=10)
		entry_email = ttk.Entry(self.master, width=30, show="*")
		entry_email.place(x=100, y=40)
		entry_email = ttk.Entry(self.master, width=30)
		entry_email.place(x=100, y=70)

	def sms_verification(self):
		labe_sms = ttk.Label(self.master, text="Did you enable verification Code ?")
		labe_sms.place(x=10, y=100)
		stringvar = StringVar()
		radio1 = ttk.Radiobutton(self.master, text="Yes", variable=stringvar, value="Yes")
		radio1.place(x=225, y=100)
		radio2 = ttk.Radiobutton(self.master, text="No", variable=stringvar, value="No")
		radio2.place(x=225, y=120)

	def submit_button(self):
		submit = ttk.Button(self.master, text="Start")
		submit.pack(pady=150)


if __name__ == "__main__":
	root = Tk()

	first_screen = FirstScreen(root)
	# first_screen.information_label()
	# first_screen.information_entry()
	# first_screen.sms_verification()
	# first_screen.submit_button()
	first_screen.add_image()

	root.mainloop()

