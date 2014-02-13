import arcpy
import pythonaddins
import sys
sys.path.append(".\Tools\Tools")
import portalpy

class ButtonClass1(object):
    """Implementation for TestFailure_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        x = portalpy.Portal("ess.maps.arcgis.com","anohe_ess5","GeogWorks3!")
        #This is used to select datasets which is a possibility
        #value = pythonaddins.OpenDialog('Credentials', True, r'C:\'', 'Add')
        #I am thinking of just creating tools to do all of this then prompting
        #the button with: pythonaddins.GPToolDialog(toolbox, tool_name)
        for i in x.folders("anohe_ess5"):
            print i['title']
