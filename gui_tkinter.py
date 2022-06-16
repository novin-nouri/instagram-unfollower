from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


class FirstScreen:

    def __init__(self, master):
        self.master = master
        self.master.title("Instagram unfollower")
        self.master.geometry("340x492")

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
        seperate_text = "." * 103
        seperate_line2 = ttk.Label(self.master, text=seperate_text,
                                   foreground="#616161")
        seperate_line2.place(x=11, y=210)
        descriotion_text = "Description:\nfirst enter the your username " \
                           "and password and in \nthe desired page field" \
                           " enter the page's id you want \nto findout who" \
                           " unfollowed this page."
        labe_name = ttk.Label(self.master, text=descriotion_text,
                              foreground="#616161")
        labe_name.pack(pady=0)

    def _information_label(self):
        labe_name = ttk.Label(self.master, text="username:")
        labe_name.place(x=11, y=233)
        labe_email = ttk.Label(self.master, text="password:")
        labe_email.place(x=10, y=290)
        labe_email = ttk.Label(self.master, text="desired page:")
        labe_email.place(x=10, y=347)

    def _information_entry(self):
        self.entry_user = ttk.Entry(self.master, width=38)
        self.entry_user.place(x=12, y=259)
        self.entry_pass = ttk.Entry(self.master, width=38, show="*")
        self.entry_pass.place(x=12, y=316)
        self.entry_desired = ttk.Entry(self.master, width=38)
        self.entry_desired.place(x=12, y=373)

    def _sms_verification(self):
        labe_sms = ttk.Label(self.master,
                             text="did you enable verification Code ?")
        labe_sms.place(x=12, y=404)
        self.stringvar = StringVar()
        self.radio1 = ttk.Radiobutton(self.master, text="Yes",
                                      variable=self.stringvar, value="Yes")
        self.radio1.place(x=236, y=404)
        self.radio2 = ttk.Radiobutton(self.master, text="No",
                                      variable=self.stringvar, value="No")
        self.radio2.place(x=282, y=404)

    def _submit_button(self):
        submit = ttk.Button(self.master, text="Search",
                            command=self._submit_command)
        submit.place(x=120, y=445)

    def _submit_command(self):
        get_user = self.entry_user.get()
        get_pass = self.entry_pass.get()
        get_desired = self.entry_desired.get()
        if self.stringvar.get() == "Yes":
            get_sms = "y"
        else:
            get_sms = "n"


if __name__ == "__main__":
    root = Tk()

    first_screen = FirstScreen(root)
    first_screen.add_logo()
    first_screen.add_image()
    first_screen.information()

    root.mainloop()
