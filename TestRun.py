from InitiateAutomation import Automation
from sys import modules

auto = Automation()

class TestRun():

    def config_browser( self, defaultbrowser, defaulturl ):
        auto.browser.configureBrowser( defaultbrowser, defaulturl )

    def execute_step( self, stepname, params ):
        callmethod = getattr( modules[__name__], stepname )
        callmethod( params )

class ConfigRun():
    browser = ''
    url = ''

class StepParam():
    duration = None
    

class ActionRun():

    def open_browser( self ):
        auto.browser.openBrowser()

    def open_url( self, params ):
        auto.browser.openURL( params.url )

    def pause( self, params ):
        auto.util.pause( params.duration )
