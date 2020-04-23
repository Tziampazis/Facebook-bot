from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains



# Google Chrome pop up window for notifications disabled
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

#Opening Chrome
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='C:/Users/tziam/Documents/chromedriver.exe')
time.sleep(2)

print("Open Success!!")
driver.get("https://facebook.com")
driver.maximize_window()

time.sleep(2)


find_username_element = driver.find_element_by_name("email").send_keys("YOUR MAIL")
find_password_element = driver.find_element_by_name("pass").send_keys("YOUR PASSWORD")
time.sleep(2)
find_login_element = driver.find_element_by_id("u_0_b").send_keys(Keys.ENTER)
print("Loggin Success!!")
time.sleep(3)
# driver.get("https://www.facebook.com/messages/")
# print("Navigate to messages Success!!")
# time.sleep(2)
# find_conversation = driver.find_element_by_xpath("//span[contains(text(),'Lil Kourkoutaes')]").click()
# print("Find Conversation Success!!")

find_conversations = driver.find_element_by_id("u_0_e").click()
time.sleep(3)
find_conversation = driver.find_element_by_xpath("//span[contains(text(),'THE CHAT NAME')]").click()
time.sleep(2)

i=0
while i < 12:
	driver.find_element_by_xpath("//*[@data-editor]").click()
	time.sleep(1)
	actions = ActionChains(driver)
	time.sleep(1)
	actions.send_keys('YOUR MESSAGE')
	actions.perform()
	time.sleep(1)
	driver.find_element_by_xpath("//a[@label = \"send\"]").click()
	i += 1
	time.sleep(3)


time.sleep(2)
logout = driver.find_element_by_id("logoutMenu").click()
time.sleep(2)
find_conversation = driver.find_element_by_xpath("//span[contains(text(),'Log Out')]").click()
print("LOGGED OUT")
print("THE END")

var = input()

driver.quit();