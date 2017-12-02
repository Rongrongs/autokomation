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
    def configureBrowser( self, browserName, defaultUrl):
        self.setDefaultBrowser( browserName )
        self.setDefaultURL( defaultUrl )

    def setDefaultBrowser( self, browserName ):
        self.defaultbrowser = browserName

    def openBrowser( self ):
        if self.defaultbrowser == 'Firefox':
            self.browser = webdriver.Firefox()
        elif self.defaultbrowser == 'Chrome':
            self.browser = webdriver.Chrome()

    def checkBrowserActive( self ):
        return self.browser is not None

    def closeBrowser( self ):
        self.browser.quit()

    def setDefaultURL( self, url ):
        self.defaulturl = url

    def openURL( self, url ):
        # Check if Browser Still Inactive
        if not self.checkBrowserActive():
            self.openBrowser()

        newurl = self.defaulturl + url
        self.browser.get( newurl )

    '''''''''''''''''
    Browser Elements 
    '''''''''''''''''
    def getElement( self, elementString ):
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