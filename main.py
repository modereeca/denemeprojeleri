from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("https://1290sqm.com/sitemap_products_1.xml?from=4705003765893&to=6652895428773")
time.sleep(4)

urls = browser.find_element_by_xpath('//*[@id="folder6"]/div[2]/div[1]/span[2]')
print(urls.text)

for url in urls:
    print(url.text)
    if "hoodie" in url.text:
        print("---------------------------------")
        print(url.text)
        print("---------------------------------")

browser.quit()
