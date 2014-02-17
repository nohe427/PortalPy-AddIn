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

import sys
import arcpy
sys.path.append(r".\Tools")
import portalpy

def main():
    # Get the parameters for the tool
    URL = r"http://www.arcgis.com/"
    user = arcpy.GetParameterAsText(0)
    password = arcpy.GetParameterAsText(1)
    # Instantiate the portal object
    try:
        portalObject = portalpy.Portal(URL, user, password)
    except:
        portalObject = "False"
	return portalObject
    if portalObject.is_logged_in == "True":
        return "True"
    else:
        return "False"
