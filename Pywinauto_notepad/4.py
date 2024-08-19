import time
from pywinauto import application

# Start Notepad
app = application.Application().start("notepad.exe")

# Wait for Notepad to load
time.sleep(2)  # Adjust the sleep time if necessary

# List all running windows to verify Notepad is running
print(app.windows())

# Connect to the running Notepad instance
# app = application.Application().connect(title_re=".*Notepad")

# Get the top window and type text into Notepad
notepad_window = app.top_window()
notepad_window.Edit.type_keys("Hello, pywinauto!")


########fknslakfnlknslkfn
