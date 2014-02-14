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
sys.path.append(r"C:\Python27\Lib\site-packages")
import portalpy

def main():
    # Get the parameters for the tool
    URL = str(arcpy.GetParameterAsText(0))
    user = str(arcpy.GetParameterAsText(1))
    password = str(arcpy.GetParameterAsText(2))
    # Instantiate the portal object
    portalObject = portalpy.Portal(URL, user, password)
    return portalObject