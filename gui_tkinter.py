from tkinter import *
from tkinter import ttk
from tkinter.tix import *
from PIL import ImageTk, Image
from instagram import Insta


class FirstScreen:

    def __init__(self, master):
        self.master = master
        self.master.title("Instagram unfollower")
        self.master.geometry("375x580")        # ("340x492")
        self.master.resizable(False, False)

    def add_logo(self):
        logo = PhotoImage(file="icon.png")
        self.master.iconphoto(False, logo)

    @staticmethod
    def add_image():
        image = Image.open("with_white.png")
        img = ImageTk.PhotoImage(image)
        # create label and add resize image
        label1 = Label(image=img)
        label1.image = img
        label1.pack(pady=15)

    def information(self):
        self._description()
        self._information_label()
        self._information_entry()
        self._sms_verification()
        self._submit_button()

    def _description(self):
        seperate_text = "." * 87
        seperate_line2 = ttk.Label(self.master, text=seperate_text,
                                   foreground="#616161")
        seperate_line2.place(x=11, y=230)
        descriotion_text = "Description:\nthis app shows you the people's" \
                           " id who you\nhave followed in instagram but " \
                           "they haven't\nfollowed you."
        labe_name = ttk.Label(self.master, text=descriotion_text,
                              foreground="#616161")
        labe_name.pack(padx=11, pady=0)

    def _information_label(self):
        labe_name = ttk.Label(self.master, text="username:")
        labe_name.place(x=11, y=256)
        labe_pass = ttk.Label(self.master, text="password:")
        labe_pass.place(x=11, y=322)
        labe_desired = ttk.Label(self.master, text="desired page:")
        labe_desired.place(x=11, y=388)

    def _information_entry(self):
        self.entry_user = ttk.Entry(self.master, width=34)
        self.entry_user.place(x=14, y=287)
        self.entry_pass = ttk.Entry(self.master, width=34, show="*")
        self.entry_pass.place(x=14, y=353)
        self.entry_desired = ttk.Entry(self.master, width=34)
        self.entry_desired.place(x=14, y=419)

    def _sms_verification(self):
        labe_sms = ttk.Label(self.master,
                             text="did you enable verification Code ?")
        labe_sms.place(x=13, y=457)
        self.stringvar = StringVar()
        self.radio1 = ttk.Radiobutton(self.master, text="Yes",
                                      variable=self.stringvar, value="Yes")
        self.radio1.place(x=13, y=488)
        self.radio2 = ttk.Radiobutton(self.master, text="No",
                                      variable=self.stringvar, value="No")
        self.radio2.place(x=69, y=488)

    def _submit_button(self):
        submit = ttk.Button(self.master, text="Confirm",
                            command=self._submit_command)
        submit.place(x=120, y=527)

    def _submit_command(self):
        get_user = self.entry_user.get()
        get_pass = self.entry_pass.get()
        get_desired = self.entry_desired.get()
        if self.stringvar.get() == "Yes":
            get_sms = "y"
        else:
            get_sms = "n"
        get_list = [get_user, get_pass, get_desired, get_sms]
        # self.master.destroy()

        self.insta(get_list)

    def insta(self, input_list):
        insta = Insta(username=input_list[0], password=input_list[1],
                      desired_page=input_list[2], verification=input_list[3])
        if insta.verification == "y":
            insta.login()
            second_screen = SecondScreen(self.master)
            second_screen.screen()
            insta._verification_code()
            find_unfollowed = insta.find()
        else:
            insta.login()
            find_unfollowed = insta.find()
        third_screen = ThirdScreen(self.master, find_unfollowed)
        third_screen.screen()


class SecondScreen(FirstScreen):

    def __init__(self, master):
        super().__init__(master)
        self.toplevel = Toplevel(master)
        self.toplevel.geometry("270x295")

    def add_logo2(self):
        logo = PhotoImage(file="icon.png")
        self.toplevel.iconphoto(False, logo)

    def screen(self):
        self.add_logo2()
        # image
        self.lock_image()
        text = "Enter the code they sent\n" + 7 * " " + "to your number"
        ttk.Label(self.toplevel, text=text).pack(pady=0)
        self.entry_code = ttk.Entry(self.toplevel, width=11)
        self.entry_code.pack(pady=10)
        submit_code = ttk.Button(self.toplevel, text="Confirm", command=self.get_code).pack(pady=10)

    def lock_image(self):
        image = Image.open("sms.png")
        img = ImageTk.PhotoImage(image)
        # create label and add resize image
        label1 = Label(self.toplevel, image=img)
        label1.image = img
        label1.pack(pady=20)

    def get_code(self):
        get_code_ = self.entry_code.get()
        with open("smscode.txt", "w") as f:
            f.write(get_code_)
            # self.master.destroy()
        self.toplevel.destroy()


class ThirdScreen(FirstScreen):

    def __init__(self, master, find_unfollowed):
        super().__init__(master)
        self.toplevel3 = Toplevel(master)
        self.find_unfollowed = find_unfollowed
        self.toplevel3.geometry("375x580")     # ("270x295")
        self.add_logo3()

    def add_logo3(self):
        logo = PhotoImage(file="icon.png")
        self.toplevel3.iconphoto(False, logo)

    def screen(self):
        self.add_logo3()
        text = f"These page's id didn't follow you:"
        seperate_line2 = ttk.Label(self.toplevel3, text=text)  # , foreground="#616161, e6e6e6"
        seperate_line2.place(x=10, y=10)

        s = Scrollbar(self.toplevel3)
        text = Text(self.toplevel3, height=40, width=50, foreground="#2f2f2f")
        s.pack(side=RIGHT, fill=Y)
        text.pack(padx=10, pady=40)
        s.config(command=text.yview)
        text.config(yscrollcommand=s.set)
        for num, id_ in enumerate(self.find_unfollowed):
            word = f"{num}-{id_}"
            text.insert(END, word)
            text.insert(END, "\n")
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()

    first_screen = FirstScreen(root)
    first_screen.add_logo()
    first_screen.add_image()
    first_screen.information()

    root.mainloop()
