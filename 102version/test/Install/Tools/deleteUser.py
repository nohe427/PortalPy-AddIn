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

import sys,os
import arcpy
workDir = os.path.dirname(sys.argv[0])
portalpyScriptPath = workDir + "\\Tools\\Tools\\portalpy.py"
sys.path.append(portalpyScriptPath)
from portalpy import *
import test_addin

def main():
    username = arcpy.GetParameterAsText(0)
    reassign_to = arcpy.GetParameterAsText(1)
    portalLogin = test_addin.portalLogin
    portalLogin.delete_user(username, cascade = False)
    print "Deleted user: " + username + " and reassigned their content to: " + reassign_to    

main()
