import arcpy
import pythonaddins
import sys
sys.path.append(".\portalpy")
import portalpy

class ButtonClass1(object):
    """Implementation for TestFailure_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        x = portalpy.Portal("ess.maps.arcgis.com","anohe_ess5","GeogWorks3!")
        print x.folders("anohe_ess5")
        
