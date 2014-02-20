import arcpy, pythonaddins, sys, os, urllib
from array import array

tbxpath = r"C:\Users\Ashley\Documents\GitHub\PortalPy-AddIn\1021version\TestFailure\Install\Tools"
sys.path.append(tbxpath + "\\Tools")

list_services_path1 = r"http://services.arcgis.com/"
list_services_path2 = r"/ArcGIS/rest/services?f=pjson"

#2/18 Ash: Accessing rest URL will only print public services. I suppose that is all the rage with tokens.
#          Need to get a list of item ids.

output = r"C:\Users\Ashley\Documents\GitHub\PortalPy-AddIn\1021version\TestFailure\Install\Output\output.txt"

import portalpy

global portalLogin

class SignIn(object):
    """Implementation for TestFailure_addin.button (Button)"""
    def __init__(self):
        
        self.enabled = True
        self.checked = False

    def onClick(self):

        #pythonaddins.GPToolDialog(tbxpath + "\\Toolbox.tbx", "SignIn")

        URL = r"http://www.arcgis.com/"
        user = 'eek'
        password = 'eek'

        portalLogin = portalpy.Portal(URL, user, password)
        org_ID = portalLogin.info().properties['id']

        FILE = open(output, "w")
        
        filehandle = urllib.urlopen(list_services_path1 + org_ID + list_services_path2)
        for lines in filehandle.readlines():
            #[16:-5]      "name" : "      
            if '"name"' in lines:
                FILE.write(lines[16:-5])
                FILE.write('\n')

        FILE.close()
        print 'Woot.'
