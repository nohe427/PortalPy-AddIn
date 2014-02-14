import arcpy
import pythonaddins
import sys
sys.path.append(r"C:\Python27\Lib\site-packages")
from portalpy import *

global portalLogin
#Get bad syntac error when declaring global portalLogin = () or portalLogin = portalpy.Portal()

class SignOn(object):
    """Implementation for test_addin.signonbutton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        global portalLogin
        #Modify this to return a value (listed below)
        #URL = input("what is the portal url?")
        portalLogin = pythonaddins.GPToolDialog(r"C:\Users\AlexanderN\Documents\GitHub\PortalPy-AddIn\102version\test\Install\Tools\Toolbox.tbx", "SignOn")
        #validation()
        #validation.enabled = True
        #This is used to select datasets which is a possibility
        #value = pythonaddins.OpenDialog('Credentials', True, r'C:\'', 'Add')
        #I am thinking of just creating tools to do all of this then prompting
        #the button with: pythonaddins.GPToolDialog(toolbox, tool_name)

class validation(object):
    """Implementation for test_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        global portalLogin
        print portalLogin
