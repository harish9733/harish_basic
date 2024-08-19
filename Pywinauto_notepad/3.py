from pywinauto import application,timings
# Connect to the Notepad application
app = application.Application().start("notepad.exe")
# Type text into Notepad
# app.Notepad.Edit.type_keys("Hello, this is an automated message!", with_spaces=True)
app = application.Application().connect(title_re=".*Notepad")
#The title_re=".*Notepad" part is a regular expression that matches any window title containing "Notepad".
notepad_window = app.top_window()
# Identifies main window.
notepad_window.edit.type_keys("Hello, pywinauto!")
# Type keys menthod simulates the keyboard.
