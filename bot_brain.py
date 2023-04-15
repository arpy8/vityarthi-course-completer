import time
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    ElementClickInterceptedException


class Bot_Brain:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")

    def login(self, GMAIL, PASS):
        self.driver.maximize_window()
        self.driver.get(url="https://vityarthi.com/login")
        time.sleep(1)

        self.driver.find_element(By.NAME, "username").send_keys(GMAIL)
        self.driver.find_element(By.ID, "password").send_keys(PASS)
        self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

    def toast_remover(self):
        pass

    #
    # /html/body/div[4]/div[4]/span[2]
    # /html/body/div[4]/div[2]/span[2]

    def engine(self, TO_CLICK):
        self.driver.get(url="https://vityarthi.com/course/learning/Python-Essentials")
        time.sleep(2)

        module_codes = [35, 37, 39, 42, 43, 44, 45, 46, 48, 56, 68, 77, 79]
        switch_on = True
        for i in TO_CLICK:
            while switch_on:
                try:
                    """opening the module"""
                    self.driver.find_element(By.ID, f'chapter_{module_codes[i]}').click()
                    time.sleep(1)
                    # //*[@id="collapseChapter48"]/div/div[1]/div/div[2]/div/label
                    j = 0
                    while True:
                        try:
                            j += 1
                            """clicking video box to open it"""
                            self.driver.find_element(By.XPATH,
                                                     f'//*[@id="collapseChapter{module_codes[i]}"]/div/div[{j}]').click()
                            time.sleep(1)

                            """clicking checkbox"""
                            self.driver.find_element(By.XPATH,
                                                     f'//*[@id="collapseChapter{module_codes[i]}"]/div/div[{j}]/div/div['
                                                     f'2]/div/label').click()
                            time.sleep(1)

                            """scrolling content page to avoid exception"""
                            pg.press("pagedown")
                            time.sleep(2)

                        except NoSuchElementException:
                            print(f"Module {i+1} completed.")
                            switch_on = False
                            break

                        except ElementNotInteractableException:
                            print(f"1. Inner ElementNotInteractableException; module: {i + 1}, vid: {j}")
                            # self.driver.find_element(By.XPATH, '//*[@id="collapseChapter{module_codes[i]}"]/div/div[{'
                            #                                    'j}]').send_keys(Keys.PAGE_DOWN)
                            pass

                        except ElementClickInterceptedException:
                            print(f"2. Inner ElementClickInterceptedException; module: {i + 1}, vid: {j}")

                except ElementNotInteractableException:
                    print(f"1. Outer ElementNotInteractableException:  {i + 1}, vid: {j}")
                    pass

                except ElementClickInterceptedException:
                    print(f"2. Outer ElementClickInterceptedException: Module {i + 1}, vid: {j}")
                    pass
