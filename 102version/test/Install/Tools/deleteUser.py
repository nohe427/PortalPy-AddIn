#-------------------------------------------------------------------------------
# Name:        deleteUser.py
# Purpose:     Deletes a user from ArcGIS Online
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
    username = arcpy.GetParameterAsText(0)
    reassign_to = arcpy.GetParameterAsText(1)
    portalLogin = test_addin.portalLogin
    portalLogin.delete_user(username, cascade = False, reassign_to)
    print "Deleted user: " + username + " and reassigned their content to: " + reassign_to    

main()
