import arcpy, pythonaddins, sys
from array import array

tbxpath = r"C:\Users\Ashley\Documents\GitHub\PortalPy-AddIn\1021version\TestFailure\Install\Tools"
output = r"C:\Users\Ashley\Documents\GitHub\PortalPy-AddIn\1021version\TestFailure\Install\Output\output.txt"

sys.path.append(tbxpath + "\\Tools")

import portalpy

class SignIn(object):
    """Implementation for TestFailure_addin.button (Button)"""
    def __init__(self):
        
        self.enabled = True
        self.checked = False

    def onClick(self):

        URL = r"http://www.arcgis.com/"
        user = 'ack'
        password = 'ack'

        portalLogin = portalpy.Portal(URL, user, password)

        fs = portalLogin.search(q='type:Feature Service',
                                sort_field = 'title', sort_order = 'asc')

        FILE = open(output, "w")
        
        for i in fs: FILE.write(i.get('title') + "\n")
            
        FILE.close()
        print 'Woot.'
