import arcpy, pythonaddins
import sys, os, urllib
from array import array
sys.path.append(r"C:\Python27\Lib\site-packages")
from portalpy import *

#Ash 2/17: Output location for Nohe
output = r"C:\Users\AlexanderN\Documents\GitHub\PortalPy-AddIn\102version\test\Install\Output\output.txt"

global portalLogin
global portalID
#Get bad syntac error when declaring global portalLogin = () or portalLogin = portalpy.Portal()

class SignOn(object):
    """Implementation for test_addin.signonbutton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        global portalLogin
        """  While the GPToolDialog runs asynchronously from the tool, it does have the option
            to import the global variable and then  reassign the variable to the
            portal object.  This allows our users to access the portal object in
            other classes that we create from this.
        """
        pythonaddins.GPToolDialog(r"C:\Users\AlexanderN\Documents\GitHub\PortalPy-AddIn\102version\test\Install\Tools\Toolbox.tbx", "SignOn")

        #Ash 2/18: Assuming portalLogin is a portal object...
        host = r"http://services.arcgis.com"
        rest = r"ArcGIS/rest/services?f=pjson"
        org_ID = portalLogin.info().properties['id']

        #Ash 2/17: Creates output.txt that contains names of all public services in the organization.
        FILE = open(output, "w")
        filehandle = urllib.urlopen(host + org_ID + rest)
        for lines in filehandle.readlines():
            #[16:-5]      "name" : "      
            if '"name"' in lines:
                FILE.write(lines[16:-5])
                FILE.write('\n')
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
