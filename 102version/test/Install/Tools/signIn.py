#-------------------------------------------------------------------------------
# Name:        signIn.py
# Purpose:      Sign into ArcGIS Online through Portal Py
#
# Author:      alex7370
#
# Created:     13/02/2014
# Copyright:   (c) alex7370 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys, os
import arcpy
workDir = os.path.dirname(sys.argv[0])
portalpyScriptPath = workDir + "\\Tools\\Tools\\portalpy.py"
sys.path.append(portalpyScriptPath)
from portalpy import *


def main():
    try:
        # Get the parameters for the tool
        URL = arcpy.GetParameterAsText(0)
        user = arcpy.GetParameterAsText(1)
        password = arcpy.GetParameterAsText(2)
        # Instantiate the portal object
        portalObject = portalpy.Portal(URL, user, password)
        #print portalObject
        import test_addin
        test_addin.portalLogin = portalObject
        test_addin.portalID = user
        uE = test_addin.updateEnabled()
        uE.go()
    except:
        arcpy.AddMessage("LOGIN FAILED, TRY AGAIN!")
    

main()
