import arcpy, pythonaddins, sys, shutil, os, time, datetime, math, urllib
from array import array

tbxpath = r"C:\Users\Ashley\Documents\GitHub\PortalPy-AddIn\1021version\TestFailure\Install\Tools"
sys.path.append(tbxpath + "\\Tools")

list_services_path1 = r"http://services.arcgis.com"
list_services_path2 = r"ArcGIS/rest/services?f=pjson"  #Converted to JSON format

ESS_org_ID = "//Wl7Y1m92PbjtJs5n//"    #How do we find out this info?

output = r"C:\Users\Ashley\Documents\GitHub\PortalPy-AddIn\1021version\TestFailure\Install\Output\output.txt"

import portalpy

global portalLogin

class SignIn(object):
    """Implementation for TestFailure_addin.button (Button)"""
    def __init__(self):
        
        self.enabled = True
        self.checked = False

    def onClick(self):
        
        portalLogin = pythonaddins.GPToolDialog(tbxpath + "\\Toolbox.tbx", "SignIn")

        FILE = open(output, "w")

        filehandle = urllib.urlopen(list_services_path1 + ESS_org_ID + list_services_path2)
        for lines in filehandle.readlines():
            #[16:-5]      "name" : "      
            if '"name"' in lines:
                FILE.write(lines[16:-5])
                FILE.write('\n')

        FILE.close()
        
        print "Check your output folder for a list of services in your organization."


