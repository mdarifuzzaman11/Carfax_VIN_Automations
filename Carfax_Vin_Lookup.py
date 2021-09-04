#Simple Project 
#Price Checker using VIN# in Carfax
#Created by MD Arifuzzaman
#This Project will automatially show the Price of the Car for Private Party Value and Trade-In Value
#this helps eleminate pressing too many keys to get price of the car 
#all we have to do is enter the VIN# and it does the rest of the work for us.

from selenium import webdriver
import time 
driver = webdriver.Chrome(executable_path = '/Users/mdarifuzzaman/Documents/All Programming/Python Single Projects/drivers/chromedriver')

#the Website to go to for the automation
driver.get('https://www.carfax.com/value/')


#this will enter your local zipcode
driver.find_element_by_id("zip").send_keys("11218")

#this will enter the VIN Number of the Car make sure to change it according to the car
driver.find_element_by_id("vin").send_keys("1HGCP26488A068973")

#this will click on the check box
driver.find_element_by_css_selector("div.app main.app__main div.app__page div.landing div.landing__container div.vehicle-input-form__container form.vehicle-input-form__form label.checkbox-input.vehicle-input-form__input__isVehicleOwner:nth-child(7) > div.checkbox-input_box:nth-child(2)").click()

#this will wait 1 sec and then click on the submit button
time.sleep(1)

#this button will click on the submit button
driver.find_element_by_css_selector("div.app main.app__main div.app__page div.landing div.landing__container div.vehicle-input-form__container form.vehicle-input-form__form > button.button.vehicle-input-form__input__submit:nth-child(8)").click()