import os


class Generate:
    """Class to create a text file and show text file"""

    def __init__(self, page_id, unfollowed):
        self.page_id = page_id
        self.unfollowed = unfollowed
        self.file_name = f"{self.page_id}-file.txt"

    def write_txt(self):
        with open(self.file_name, "w") as f:
            f.write(f"These people did not follow this page({self.page_id}):")
            for num, name in enumerate(self.unfollowed):
                f.write(f"\n{num}- {name}")

    def show_txt(self):
        os.startfile(self.file_name)