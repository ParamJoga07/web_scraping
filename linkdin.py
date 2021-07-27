from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")
email = driver.find_element_by_xpath('//*[@id="username"]')
email.send_keys("parmeshwar5jan@gmail.com")
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("Param@3630")
signin = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
signin.click()
searchbox = driver.find_element_by_xpath('//*[@id="search-box__overlay--hidden global-alert-offset-top"]')
searchbox.send_keys("sandeepletsmobility")
searchbutton= driver.find_element_by_xpath('//*[@id="search-button"]')
searchbutton.click()