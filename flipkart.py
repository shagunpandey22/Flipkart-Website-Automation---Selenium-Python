from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



web_browser=webdriver.Chrome()
web_browser.get("https://www.flipkart.com/")
web_browser.maximize_window()
try:
    close_button = WebDriverWait(web_browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]"))
    )
    close_button.click()
except:
    pass
searchbox=web_browser.find_element(By.NAME,"q")
searchbox.send_keys("Iphone 16")
searchbox.submit()
main_page=web_browser.current_window_handle #tells about current web handle

web_browser.find_element(By.XPATH,"//div[normalize-space()='Apple iPhone 16 (Black, 128 GB)']").click()
all_tabs=web_browser.window_handles #gives list of all tabs open
#print(all_tabs)

for i in all_tabs:
    if i!=main_page:
        web_browser.switch_to.window(i)

print(web_browser.current_window_handle)

# l=[]
# l=web_browser.find_elements(By.CLASS_NAME,"_7eSDEz")
# web_browser.implicitly_wait(5)
# for i in l:
#     print(i.text)
# print(f"Number of elements found: {len(l)}")
# assert len(l) == 4, f"Expected 4 elements, but found {len(l)}"

wait = WebDriverWait(web_browser, 15)
add_to_cart_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add to cart']"))
)
print(add_to_cart_button.text)

web_browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_button)
time.sleep(1)
web_browser.execute_script("arguments[0].click();", add_to_cart_button)
# Wait for "Go to Cart" button to appear
try:
    go_to_cart_button = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class='QqFHMw vslbG+ In9uk2']"))

    )
    print("✅ Add to cart was successful.")
    go_to_cart_button.click()
except:
    print("❌ Add to cart likely failed.")

#web_browser.save_screenshot("add_to_cart_debug.png")

try:
    placeorder = WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.XPATH,"//button[@class='QqFHMw zA2EfJ _7Pd1Fp']"))

    )
    print("✅ Clicked on place order.")
    placeorder.click()
except:
    print("❌ Not able to place order.")


# placeorder=web_browser.find_element(By.CSS_SELECTOR,".QqFHMw.zA2EfJ._7Pd1Fp")
# placeorder.click()

assert "/checkout/init" in web_browser.current_url, "❌ Not on checkout login page."
print("✅ Successfully landed on checkout login page.")




time.sleep(15)
