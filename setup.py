import cx_Freeze
import sys
import os

base = None

if sys.platform=="win32":
    base="win32GUI"

os.environ['TCL_LIBRARY']= r"C:\Users\Bhanu\AppData\Local\Programs\Python\Python37\tcl\tcl8.6"
os.environ['TKL_LIBRARY']= r"C:\Users\Bhanu\AppData\Local\Programs\Python\Python37\tcl\tk8.6"

executables = [cx_Freeze.Executable("Student_Management_System.py",base=base)]

cx_Freeze.setup(
    name="Student Management System",
    options={"Bulid_exe":{"packages":["tkinter","os"],"include_files":["tcl86.dll","tk86t.dll"]}},
    version="0.01",
    description="Tkinter Application",
    executables=executables
)