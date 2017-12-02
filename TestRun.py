from InitiateAutomation import Automation
from sys import modules

auto = Automation()

class TestRun():

    def configBrowser( self, defaultbrowser, defaulturl ):
        auto.browser.configureBrowser( defaultbrowser, defaulturl )

    def executeStep( self, stepname, params ):
        callmethod = getattr( modules[__name__], stepname )
        callmethod( params )

class ConfigRun():
    browser = ''
    url = ''

class StepParam():
    duration = None
    

class ActionRun():

    def OPEN_BROWSER( self ):
        auto.browser.openBrowser()

    def OPEN_URL( self, params ):
        auto.browser.openURL( params.url )

    def PAUSE( self, params ):
        auto.util.pause( params.duration )