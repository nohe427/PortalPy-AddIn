import arcpy
import pythonaddins
import sys
sys.path.append(".\\Tools\\Tools\\")
from portalpy import *

class SignOn(object):
    """Implementation for test_addin.signonbutton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        print "FUCK YOU"

##        GPToolDialog(r".\Tools\Toolbox.tbx", "SignOn")
        #This is used to select datasets which is a possibility
        #value = pythonaddins.OpenDialog('Credentials', True, r'C:\'', 'Add')
        #I am thinking of just creating tools to do all of this then prompting
        #the button with: pythonaddins.GPToolDialog(toolbox, tool_name)
##        if portalLogin == "True":
##            #ButtonClass2.enabled = True
##            print "True"
##        else:
##            print "False"
