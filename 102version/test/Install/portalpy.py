import arcpy, pythonaddins, sys, os
sys.path.append(os.path.dirname(__file__) + "\\Tools\\Tools")
from portalpy import *

output = r"C:\Users\AlexanderN\Documents\GitHub\PortalPy-AddIn\102version\test\Install\Output\output.txt"

global portalLogin
global portalID
#Get bad syntac error when declaring global portalLogin = () or portalLogin = portalpy.Portal()

TBXPATH = os.path.dirname(__file__) + "\\Tools\\Toolbox.tbx"

class SignOn(object):
    """Implementation for test_addin.signonbutton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        print "CLICK"
        global portalLogin
        """  While the GPToolDialog runs asynchronously from the tool, it does have the option
            to import the global variable and then  reassign the variable to the
            portal object.  This allows our users to access the portal object in
            other classes that we create from this.
        """
        pythonaddins.GPToolDialog(TBXPATH, "SignOn")

        fs = portalLogin.search(q='type:Feature Service',
                                sort_field = 'title', sort_order = 'asc')

        #Ash 2/17: Creates output.txt that contains names of all services in the organization.

        FILE = open(output, "w")
        for i in fs: FILE.write(i.get('title') + "\n")
        FILE.close()
        
        print "Check test\\Install\\Output" 

class folderList(object):
    """Implementation for test_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        global portalLogin
        print "These are the folders you have currently on this Portal username:"
        for i in portalLogin.folders(portalID):
            print i['title']

class newFolder(object):
    """Implementation for test_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(r"C:\Users\AlexanderN\Documents\GitHub\PortalPy-AddIn\102version\test\Install\Tools\Toolbox.tbx", "createFolderCU")


class portalpyUsers(object):
    """Implementation for test_addin.button_2 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        for i in portalLogin.users(['username', 'fullName']):
            print i

class deleteUser(object):
    """Implementation for test_addin.button_3 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(r"C:\Users\AlexanderN\Documents\GitHub\PortalPy-AddIn\102version\test\Install\Tools\Toolbox.tbx", "deleteUser")
