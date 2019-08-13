# Import Automation
from TestRun import ConfigRun
from TestRun import TestRun

# Start Test
run = TestRun()

url = 'https://m.tokopedia.com/'
browser = 'Firefox'

# Configure Browser
run.configBrowser( 'Firefox', url )

# Open m.tokopedia.com

auto.browser.openURL( url )

koplakmenu = browser.getElement('//koplak')

categorymenu = auto.browser.getElement( '//div[@class="pdp-shop__action-holder"]//span[contains(@class, "favorite__btn-fav")]' )
categorymenu.click()

run.executeStep( 'PAUSE',  )

# Close Browser
browser.closeBrowser()
