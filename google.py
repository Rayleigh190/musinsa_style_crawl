from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://store.musinsa.com/app/styles/lists?use_yn_360=&style_type=american_casual&brand=&model=&max_rt=2020&min_rt=2010&year_date=2018&month_date=&display_cnt=60&list_kind=small&sort=rt&page=1")


totalPagingNum = int(driver.find_element_by_css_selector(".totalPagingNum").text)
currentPagingNum = int(driver.find_element_by_css_selector(".currentPagingNum").text)
page_num = 2
name_count = 0

while currentPagingNum <= totalPagingNum:

    images = driver.find_elements_by_css_selector(".list_smallimg_coordi")
    count = 0
    for image in images:

        SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
    
        time.sleep(1.5)
        try:
            driver.find_elements_by_css_selector(".list_smallimg_coordi")[count].click()
        except:
            count = count + 1
            name_count = name_count + 1
            continue
        time.sleep(1)
        imgUrl = driver.find_elements_by_css_selector(".detail_img")[1].get_attribute("src")
        urllib.request.urlretrieve(imgUrl, "images/2018/casual/" + str(name_count) + ".jpg")
        driver.back()

        count = count + 1
        name_count = name_count + 1

    if page_num == 11:
        driver.find_element_by_css_selector(".paging-btn.next").click()
        page_num = 2
        currentPagingNum = currentPagingNum + 1
        continue

    time.sleep(2)
    driver.find_elements_by_css_selector(".paging-btn")[page_num + 1].click()
    page_num = page_num + 1
    currentPagingNum = currentPagingNum + 1


# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()ss