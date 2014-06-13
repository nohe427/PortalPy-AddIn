import arcpy
import pythonaddins
import sys, os
workDir = os.path.dirname(__file__)
Tbx = workDir + "\\Tools\\Toolbox.tbx"
portalpyScriptPath = workDir + "\\Tools\\Tools\\portalpy.py"
sys.path.append(portalpyScriptPath)
from portalpy import *

global portalLogin
global portalID
#Get bad syntac error when declaring global portalLogin = () or portalLogin = portalpy.Portal()

class SignOn(object):
    """Implementation for test_addin.signonbutton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        workDir = os.path.dirname(__file__)
        Tbx = workDir + "\\Tools\\Toolbox.tbx"
        print Tbx
        global portalLogin
        """  While the GPToolDialog runs asynchronously from the tool, it does have the option
            to import the global variable and then  reassign the variable to the
            portal object.  This allows our users to access the portal object in
            other classes that we create from this.
        """
        pythonaddins.GPToolDialog(Tbx, "SignOn")

class folderList(object):
    """Implementation for test_addin.button (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        global portalLogin
        if portalLogin != None:
            self.enabled = True
        else:
            pass
        print "These are the folders you have currently on this Portal username:"
        for i in portalLogin.get_user(portalID):
            print i['role']


class newFolder(object):
    """Implementation for test_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(Tbx, "createFolderCU")


class portalpyUsers(object):
    """Implementation for test_addin.button_2 (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        for i in portalLogin.users(['username', 'fullName']):
            print i

class deleteUser(object):
    """Implementation for test_addin.button_3 (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(Tbx, "deleteUser")

class updateEnabled:
    def go(self):
        button.enabled = True
        button_1.enabled = True
        button_2.enabled = True
        button_3.enabled = True
