import arcpy, pythonaddins, sys, shutil, os, time, datetime, math, urllib
from array import array

tbxpath = r"C:\Users\Ashley\Documents\GitHub\PortalPy-AddIn\1021version\TestFailure\Install\Tools"
sys.path.append(tbxpath + "\\Tools")

list_services_org = []
list_services_org2 = []
list_services_path1 = r"http://services.arcgis.com"
ESS_org_ID = "//Wl7Y1m92PbjtJs5n//"    #How to get this in portalpy?
list_services_path2 = r"ArcGIS/rest/services?f=pjson"  #Converted to JSON format

output_html = r"C:\Users\Ashley\Documents\GitHub\PortalPy-AddIn\1021version\TestFailure\Install\Output\output_html.txt"
output_txt = r"C:\Users\Ashley\Documents\GitHub\PortalPy-AddIn\1021version\TestFailure\Install\Output\output_txt.txt"

import portalpy

global portalLogin

class SignIn(object):
    """Implementation for TestFailure_addin.button (Button)"""
    def __init__(self):
        
        self.enabled = True
        self.checked = False

    def onClick(self):
        
        portalLogin = pythonaddins.GPToolDialog(tbxpath + "\\Toolbox.tbx", "SignIn")

        #Write to HTML
        filehandle = urllib.urlopen(list_services_path1 + ESS_org_ID + list_services_path2)
        for lines in filehandle.readlines(): list_services_org.append(lines)

"""
        FILE = open(output_html, "w")
        for i in list_services_org: FILE.write(i)
        FILE.close()
"""
        for i in list_services_org:
            if '"name"' in i: list_services_org2.append(i)

        for i in list_services_org2: print i

        print "Check your output folder for a list of services in your organization."
            
        #This is used to select datasets which is a possibility
        #value = pythonaddins.OpenDialog('Credentials', True, r'C:\'', 'Add')
        #I am thinking of just creating tools to do all of this then prompting
        #the button with: pythonaddins.GPToolDialog(toolbox, tool_name)
        
        if portalLogin == "True":
            #ButtonClass2.enabled = True
            print "True"
        else:
            print "False"

