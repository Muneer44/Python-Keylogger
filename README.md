# Keylogger with email capability

> ### _This cross platform Python keylogger is capable of recording all keystrokes and remotely send them via email._

_This application is tested and tried on Python 3.10.7 and works on different platforms like: MAC, Windows and Linux._

_Along with 'email capability', it also includes a 'debug mode': `[dev_mode]` which displays the keystrokes in the cmd screen and stores in 'log_file.txt'_

### Use cases:
- Educational purpose: To understand the working of a keylogger.
- Self-analysis and assessment: Be aware of your system usage.
- Workforce Area: [With consent] Monitor employees' system usage.
- Company Security: Company data exchange and search query monitoring.
- Educational instituitions: Log keystrokes and analyse system usage.
- Parental Control: Monitor childrens' system activity.

## Snippets
![Python_Keylogger](https://user-images.githubusercontent.com/31078414/201460606-6ffa5ad7-34d3-43d7-8cac-a5c95bb69e82.gif)

### Generate App Password
Gmail requires you to use "App password" on your applications instead of your actual "email password".

![App_pwd](https://user-images.githubusercontent.com/31078414/201460604-6f080b47-a39c-4dae-8a11-06d21bd5d24b.gif)

## Installation process
clone this repository with `git clone`, install the `pynput` module and execute the `handler.py` file.
```
> git clone https://github.com/Muneer44/python-keylogger.git
> cd Python Keylogger
> pip install pynput
```
*Update arguments in the Python-Keylogger/handler.py file*

- _email, pwd, duration, receive_email, display_onscreen_
```
> sudo python3 "Python-Keylogger/handler.py"
```

*Notice that the existence of `pynput` may require the virtual environment to have the "pynput" module installed for execution in the venv interpreter (if you use one),
instead of just using the system interpreter.*


## Mitigations

- use multi factor authentication
- use a password manager
- use anti-malwares to detect keylogging softwares
- use a virtual keyboard
- avoid downloading unknown files
- do a software inventory and browser extensions check

## Disclaimer
The use of code contained in this repository, either in part or in its totality,
for engaging targets without prior mutual consent is illegal. **It is
the end user's responsibility to obey all applicable local, state and
federal laws.**

This application is a Proof-of-Concept [PoC] to understand the working of a keylogger, purely intended for educational purposes. Do not use it to compromise any unauthorized device; demonstrate on your own devices only.

> NOTE: This application is deliberately not packaged as an executable to avoid malicious usage.
