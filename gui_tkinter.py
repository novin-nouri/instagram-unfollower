from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from instagram import Insta


class FirstScreen:
    """This class is for the main screen
    takes information such as username, password and ...for us
    """

    def __init__(self, master):
        self.master = master
        self.master.title("Instagram unfollower")
        self.master.geometry("375x580")
        self.master.resizable(False, False)
        self.master.attributes('-topmost', 'true')
        """Initializes a FirstScreen

        Args:
            master: In order to create a tkinter application, we generally 
                create an instance of tkinter frame,It helps to display the 
                root window and manages all the other components of the 
                tkinter application.
        """

    def __repr__(self):
        return f"{self.__class__.__name__!r}({self.__dict__!r})"

    def add_logo(self):
        """Add logo for our app"""
        logo = PhotoImage(file="files/icon.png")
        self.master.iconphoto(False, logo)

    @staticmethod
    def add_image():
        """Add image in main screen"""
        image = Image.open("files/with_white.png")
        img = ImageTk.PhotoImage(image)
        label1 = Label(image=img)
        label1.image = img
        label1.pack(pady=15)

    def description(self):
        """Add description and user information label"""
        # Seperate line
        seperate_text = "." * 87
        seperate_line2 = ttk.Label(self.master,
                                   text=seperate_text,
                                   foreground="#616161")
        seperate_line2.place(x=11, y=230)
        # description label
        descriotion_text = "Description:\nthis app shows you the people's" \
                           " id who you\nhave followed in instagram but " \
                           "they haven't\nfollowed you."
        description_label = ttk.Label(self.master,
                                      text=descriotion_text,
                                      foreground="#616161")
        description_label.pack(padx=11, pady=0)
        # now we add username, password, ... label
        self._information_label()

    def _information_label(self):
        """Add username, password, desired page label"""
        label_name = ttk.Label(self.master, text="username:")
        label_name.place(x=11, y=256)
        label_pass = ttk.Label(self.master, text="password:")
        label_pass.place(x=11, y=322)
        label_desired = ttk.Label(self.master, text="desired page:")
        label_desired.place(x=11, y=388)
        self._information_entry()

    def _information_entry(self):
        """Add entry box for username, passwor,... label"""
        self.entry_user = ttk.Entry(self.master, width=34)
        self.entry_user.place(x=14, y=287)
        self.entry_pass = ttk.Entry(self.master, width=34, show="*")
        self.entry_pass.place(x=14, y=353)
        self.entry_desired = ttk.Entry(self.master, width=34)
        self.entry_desired.place(x=14, y=419)
        # This is radio button for ask about sms verification
        self._sms_verification_code()
        self._confirm_button()

    def _sms_verification_code(self):
        """This is radio button for ask about sms verification"""
        label_sms_text = "did you enable verification Code ?"
        label_sms = ttk.Label(self.master, text=label_sms_text)
        label_sms.place(x=13, y=457)
        # Create radio button
        self.stringvar = StringVar()
        self.radio1 = ttk.Radiobutton(self.master,
                                      text="Yes",
                                      variable=self.stringvar,
                                      value="Yes")
        self.radio1.place(x=13, y=488)
        self.radio2 = ttk.Radiobutton(self.master,
                                      text="No",
                                      variable=self.stringvar,
                                      value="No")
        self.radio2.place(x=69, y=488)

    def _confirm_button(self):
        """Add confirm button"""
        confirm = ttk.Button(self.master,
                             text="Confirm",
                             command=self._confirm_command)
        confirm.place(x=120, y=527)

    def _confirm_command(self):
        """When click on confirm button these codes are executed"""
        self._waiting_label()
        # Take user input include:uername, password and ...
        get_user = self.entry_user.get()
        get_pass = self.entry_pass.get()
        get_desired = self.entry_desired.get()
        # sms verification radio button
        if self.stringvar.get() == "Yes":
            get_sms = "y"
        else:
            get_sms = "n"
        get_list = [get_user, get_pass, get_desired, get_sms]
        self.insta(get_list)

    def _waiting_label(self):
        """Convert confirm button to waiting label"""
        # First we fill the confirm button with empty label
        empty_label = ttk.Label(self.master,
                                text=" " * 30,
                                font=("Arial", 15),
                                foreground="#616161")
        empty_label.place(x=105, y=525, height=30)
        # Add waiting label
        waiting_label = ttk.Label(self.master, text="   waiting...   ",
                                  font=("Arial", 15),
                                  foreground="#616161")
        waiting_label.place(x=105, y=531, height=30)
        # update main screen
        self.master.update()

    def insta(self, input_list):
        """Now we initialize Insta class with user inputs from main screen"""
        insta = Insta(username=input_list[0],
                      password=input_list[1],
                      desired_page=input_list[2],
                      verification=input_list[3])
        # Login with user input
        insta.login()
        # about activate sms verification code
        if insta.verification == "y":
            # scondScreen class for take sms verification code from uesr
            second_screen = SecondScreen(self.master, insta)
            second_screen.screen()
        else:
            find_list = insta.find()
            # now third screen or last screen is open
            third_screen = ThirdScreen(self.master)
            third_screen.screen()
            third_screen.show_id(find_list)
        # for change waiting label to finish label
        self._finish_label()

    def _finish_label(self):
        """Convert waiting label to finish label"""
        # First we fill the waiting label with empty label
        finish = ttk.Label(self.master,
                           text=" " * 30,
                           font=("Arial", 15),
                           foreground="#616161")
        finish.place(x=105, y=525, height=30)
        # Add finish label
        finish = ttk.Label(self.master,
                           text="       finish   ",
                           font=("Arial", 15),
                           foreground="#616161")
        finish.place(x=105, y=531, height=30)
        # update main screen
        self.master.update()


class SecondScreen(FirstScreen):
    """Class to get sms verification code from user"""

    def __init__(self, master, insta):
        super().__init__(master)
        self.toplevel = Toplevel(master)
        self.insta = insta
        self.toplevel.geometry("270x295")
        self.toplevel.attributes('-topmost', 'true')
        """Initializes a SecondScreen

        Args:
            master: In order to create a tkinter application, we generally 
                create an instance of tkinter frame,It helps to display the root 
                window and manages all the other components of the tkinter
                application.
            insta: Class to find who unfollowed you(from instagram.py)
        """

    def screen(self):
        """Add logo and image and entry code box for second screen"""
        self._add_logo2()
        self._lock_image()
        # Add label for take sms code
        text = "Enter the code they sent\n" + 7 * " " + "to your number"
        ttk.Label(self.toplevel, text=text).pack(pady=0)
        # add entry box for take sms code
        self.entry_code = ttk.Entry(self.toplevel, width=11)
        self.entry_code.pack(pady=10)
        # confim button
        confirm_code_button = ttk.Button(self.toplevel,
                                         text="Confirm",
                                         command=self._get_code)
        confirm_code_button.pack(pady=10)

    def _add_logo2(self):
        """Add logo for second screen"""
        logo = PhotoImage(file="files/icon.png")
        self.toplevel.iconphoto(False, logo)

    def _lock_image(self):
        """Add lock image for second screen"""
        image = Image.open("files/sms.png")
        img = ImageTk.PhotoImage(image)
        label1 = Label(self.toplevel, image=img)
        label1.image = img
        label1.pack(pady=20)

    def _get_code(self):
        """When click on confirm button these codes are executed"""
        get_sms_code = self.entry_code.get()
        # Save code in text file
        with open("smscode.txt", "w") as f:
            f.write(get_sms_code)
        # went to instagram and put sms code in
        self.insta.verification_code()
        # close second screen
        self.toplevel.destroy()
        find_list = self.insta.find()
        # now third screen or last screen is open
        third_screen = ThirdScreen(self.master)
        third_screen.screen()
        third_screen.show_id(find_list)


class ThirdScreen(FirstScreen):
    """Class to  shows those who unfollowed your page"""

    def __init__(self, master):
        super().__init__(master)
        self.toplevel2 = Toplevel(master)
        self.toplevel2.geometry("375x580")
        self.toplevel2.attributes('-topmost', 'true')
        """Initializes a ThirdScreen

        Args:
            master: In order to create a tkinter application, we generally 
                create an instance of tkinter frame,It helps to display the 
                root window and manages all the other components of the 
                tkinter application.
        """

    def screen(self):
        """Add logo and label for third screen"""
        self._add_logo3()
        # Add label
        text = f"These people didn't follow desired page:"
        top_label = ttk.Label(self.toplevel2, text=text)
        top_label.place(x=11, y=15)

    def _add_logo3(self):
        """Add logo for third screen"""
        logo = PhotoImage(file="files/icon.png")
        self.toplevel2.iconphoto(False, logo)

    def show_id(self, find_unfollowed):
        """create scrollbar and show page's id"""
        scroll_bar_ = Scrollbar(self.toplevel2)
        text_box = Text(self.toplevel2,
                        height=23,
                        width=27,
                        foreground="#2f2f2f")
        scroll_bar_.pack(side=RIGHT, fill=Y)
        text_box.place(x=12, y=50)
        scroll_bar_.config(command=text_box.yview)
        text_box.config(yscrollcommand=scroll_bar_.set)
        # Insert page's id in text box
        for num, id_ in enumerate(find_unfollowed):
            word = f"{num}-{id_}"
            text_box.insert(END, word)
            text_box.insert(END, "\n")
