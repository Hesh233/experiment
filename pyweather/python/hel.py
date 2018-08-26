import sys
from Tkgui import location
def getLocation():
    """get location from user input
    default beijing
    """
    argvs = sys.argv
    locationa = argvs[1] if len(argvs) >= 2 else location
    return locationa

