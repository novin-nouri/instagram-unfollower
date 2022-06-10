from instagram import Insta
from print import print_, print_find
from generate import Generate


print_()
user = input("pleas enter your username= ")
pass_ = input("pleas enter your password= ")
desired = input("-The desired page for find those= ")
ask = input("-Did you enable verification Code?[y/n] ")

insta = Insta(username=user, password=pass_, desired_page=desired,
              verification=ask)
insta.login()
find_unfollowed = insta.find()

print_find(find_unfollowed, insta.desired_page)

txt = Generate(page_id=insta.desired_page, unfollowed=find_unfollowed)
txt.write_txt()
txt.show_txt()