# Import Automation
from TestRun import ConfigRun
from TestRun import TestRun

# Start Test
run = TestRun()

url = 'https://m.tokopedia.com/'
browser = 'Firefox'

# Configure Browser
run.config_browser( 'Firefox', url )

# Open m.tokopedia.com

auto.browser.open_url( url )

koplakmenu = browser.get_element('//koplak')

categorymenu = auto.browser.get_element( '//div[@class="pdp-shop__action-holder"]//span[contains(@class, "favorite__btn-fav")]' )
categorymenu.click()

run.execute_step( 'PAUSE',  )

# Close Browser
browser.close_browser()
