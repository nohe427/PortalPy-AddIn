import arcpy
import pythonaddins
import sys
sys.path.append(r"C:\Python27\Lib\site-packages")
from portalpy import *

global portalLogin

class SignOn(object):
    """Implementation for test_addin.signonbutton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        print "You are very lucky my friend"
        global portalLogin
        portalLogin = pythonaddins.GPToolDialog(r"C:\Users\AlexanderN\Documents\GitHub\PortalPy-AddIn\102version\test\Install\Tools\Toolbox.tbx", "SignOn")
        #This is used to select datasets which is a possibility
        #value = pythonaddins.OpenDialog('Credentials', True, r'C:\'', 'Add')
        #I am thinking of just creating tools to do all of this then prompting
        #the button with: pythonaddins.GPToolDialog(toolbox, tool_name)
        if portalLogin is not None:
            print "True"
        else:
            print "False"
