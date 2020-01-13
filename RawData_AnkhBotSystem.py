#---------------------------------------
#	Import Libraries
#---------------------------------------
import clr, sys, json, os, codecs
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")
import time

#---------------------------------------
#	[Required]	Script Information
#---------------------------------------
ScriptName = "raw data"
Website = "https://www.AnkhBot.com"
Creator = "Yaz12321"
Version = "1.0"
Description = "Gather raw data of messages. !startrawdata and !endrawdata"

settingsFile = os.path.join(os.path.dirname(__file__), "settings.json")

#---------------------------------------
#   Version Information
#---------------------------------------

# Version:
# > 1.1.0.1 <
    # fixed cost setting
    # removed enable/disable button in config

# > 1.1.0.0 <
    # Cleaned up code
    # fixed missing permission check
    # added "only live mode"

# > 1.0.1.0 < 
    # Cleaned up code 
    # fixed missing info in textboxes 

# > 1.0.0.0 < 
    # Official Release

class Settings:
    # Tries to load settings from file if given 
    # The 'default' variable names need to match UI_Config
    def __init__(self, settingsFile = None):
        if settingsFile is not None and os.path.isfile(settingsFile):
            with codecs.open(settingsFile, encoding='utf-8-sig',mode='r') as f:
                self.__dict__ = json.load(f, encoding='utf-8-sig') 
        else: #set variables if no settings file
            self.OnlyLive = False
            self.Permission = "Moderator"
            self.PermissionInfo = ""

            
            
    # Reload settings on save through UI
    def ReloadSettings(self, data):
        self.__dict__ = json.loads(data, encoding='utf-8-sig')
        return

    # Save settings to files (json and js)
    def SaveSettings(self, settingsFile):
        with codecs.open(settingsFile,  encoding='utf-8-sig',mode='w+') as f:
            json.dump(self.__dict__, f, encoding='utf-8-sig')
        with codecs.open(settingsFile.replace("json", "js"), encoding='utf-8-sig',mode='w+') as f:
            f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8-sig')))
        return


#---------------------------------------
# Initialize Data on Load
#---------------------------------------
def Init():
    # Globals
    global MySettings

    # Load in saved settings
    MySettings = Settings(settingsFile)
    global t
    t = time.time()
    global trigger
    trigger = False

    # End of Init
    return

#---------------------------------------
# Reload Settings on Save
#---------------------------------------
def ReloadSettings(jsonData):
    # Globals
    global MySettings

    # Reload saved settings
    MySettings.ReloadSettings(jsonData)

    # End of ReloadSettings
    return



def Execute(data):
    if trigger == True:
        Parent.SendTwitchMessage(data.RawData)

    if data.IsChatMessage() and data.GetParam(0).lower() == "!startrawdata":
        if Parent.HasPermission(data.User, MySettings.Permission, MySettings.PermissionInfo):
            global trigger
            trigger = True

    if data.IsChatMessage() and data.GetParam(0).lower() == "!endrawdata":
        if Parent.HasPermission(data.User, MySettings.Permission, MySettings.PermissionInfo):
            global trigger
            trigger = False    
    
        
        
       

        


                
                

    return

def Tick():
    
    
    return

def UpdateSettings():
    with open(m_ConfigFile) as ConfigFile:
        MySettings.__dict__ = json.load(ConfigFile)
    return
