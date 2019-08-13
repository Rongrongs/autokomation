from selenium import webdriver
import time

# BrowserUtil
class BrowserUtil():
    defaultbrowser = 'Chrome'
    defaulturl = ''
    errmsg = ''

    '''''''''''''''''''''
    Browser Management
    '''''''''''''''''''''
    def configure_browser( self, browser_name, default_url):
        self.setDefaultBrowser( browserName )
        self.setDefaultURL( defaultUrl )

    def set_default_browser( self, browser_name ):
        self.defaultbrowser = browserName

    def open_browser( self ):
        if self.defaultbrowser == 'Firefox':
            self.browser = webdriver.Firefox()
        elif self.defaultbrowser == 'Chrome':
            self.browser = webdriver.Chrome()

    def check_browser_active( self ):
        return self.browser is not None

    def close_browser( self ):
        self.browser.quit()

    def set_default_url( self, url ):
        self.defaulturl = url

    def open_url( self, url ):
        # Check if Browser Still Inactive
        if not self.checkBrowserActive():
            self.openBrowser()

        newurl = self.defaulturl + url
        self.browser.get( newurl )

    '''''''''''''''''
    Browser Elements 
    '''''''''''''''''
    def get_element( self, elementString ):
        return self.browser.find_element_by_xpath( elementString )

    # def getElement( self, byType, elementString ):
    #     try:
    #         if byType == 'xpath':
    #             self.browser.find_element_by_xpath( self, elementString )
    #         else:
    #             errmsg = 'No Element Type ''' + byType + ''' Found.'''
    #             raise
    #     except:
    #         self.assertEquals( errmsg )

# ActionUtil
class ActionUtil():
    def __init__( self ):
        self.component = 'component'

# Util
class Util():
    def pause( self, seconds ):
        time.sleep( seconds )
