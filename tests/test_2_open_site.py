import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



#def test_site_visit():
    #driver = webdriver.Chrome()
   # driver.get("https://demoqa.com/")

    #try:
        #driver.find_element(By.CSS_SELECTOR,'header > a > img') #в локаторах всегда идет поиск по последнему элементу
   ## except NoSuchElementException:
      #  assert False
    #assert True

#def test_banner_image():
    #driver = webdriver.Chrome()
    #driver.get("https://demoqa.com/")

    #try:
       ##except NoSuchElementException:
        #assert False
    #assert True


def test_banner_button():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")

    try:
        button_elements = driver.find_element(By.CSS_SELECTOR, 'div.home-body >div > div:nth-child(1)')
    except NoSuchElementException:
        assert False
    assert True

    button_elements.click()
    time.sleep(3) #ожидание

    assert driver.current_url == 'https://demoqa.com/elements'
