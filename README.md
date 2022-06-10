# instagram-unfollower

This app shows you names of people you have followed in instagram but they have not followed you. 
you can even check it for your friends and find out who  have not followed your friend's.

## Installation & Requirements
- `pip install selenium` and download a [Drivers](https://pypi.org/project/selenium/) specific to your browser And put it in the address where the files are
- `pip install pyautogui`

## How to use it

- **RUN**:
```python
user8 = "your username"
pass8 = "your password"
id8 = input("-The desired page = ")         
ask = input("-Did you enable verification Code?[y/n] ")
test = Instabot(user8,pass8,id8)
#Run \|/
test.login()
test.follow()
```
> you **must** change **"your username"** and **"your password"**
