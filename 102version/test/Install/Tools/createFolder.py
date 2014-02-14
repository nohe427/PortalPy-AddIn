#-------------------------------------------------------------------------------
# Name:        createFolder
# Purpose:     Create a folder in your ArcGIS Online Account
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
import test_addin

def main():
    folderName = arcpy.GetParameterAsText(0)
    user = test_addin.portalID
    portalObject = test_addin.portalLogin
    portalObject.create_folder(user, folderName)
    print "New Folder Added"

main()

