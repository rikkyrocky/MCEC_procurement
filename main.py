from selenium import webdriver
from time import sleep
from logindetails import email, password, batchname
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import traceback
import re
class Invoice:
    pass



class Ubot:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def openUbock(self): #opening browser
        self.driver.get('https://mcec.ungerboeck.net/prod/app85.cshtml')
        sleep(2)
        self.login()
    def login(self):
        def input_fields(xpath_input, str):
            field = self.driver.find_element('xpath', xpath_input)
            field.send_keys(str)

        def button_click(xpath_button):
            button = self.driver.find_element('xpath', xpath_button)
            button.click()
        try: # Username
            sleep(0.5)
            input_fields("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]", email)
            button_click('/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div[2]/input')
        except: #retry in case of slow loading
            sleep(0.5)
            input_fields(
                "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]",
                email)
            button_click(
                '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div[2]/input')
        try: #password
            sleep(2.5)
            input_fields('/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input', password)
            button_click('/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input')
        except:
            print("slow loading")
            sleep(1.5)
            input_fields(
                '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input',
                password)
            button_click(
                '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input')
        try: # ask user input for two factor authentification and subsequent buttons
            sleep(1)
            button_click('/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div')
            twofa = input("Enter Code:")
            input_fields("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/input", twofa)
            button_click("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[6]/div/div/div/div[2]/input")
            sleep(3)
            button_click("/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input")
        except Exception as e:
            print(f"timing exception, error {e}")
            try:
                button_click(
                    "/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input")
                print("no 2fa required")
            except:
                print("fail")
    def open_batch(self): #opening a batch
        def input_fields(xpath_input, str):
            field = self.driver.find_element('xpath', xpath_input)
            field.send_keys(str)

        def button_click(xpath_button):
            button = self.driver.find_element('xpath', xpath_button)
            button.click()
        try:
            sleep(2)
            button_click("/html/body/div[2]/ux-dialog-container/div/div/div/div[2]/div/div/section/div/ul/li[1]/div[1]/div/section/div/div/div[1]/div/div/button")

            '''sleep(2)
            button_click("/html/body/div[2]/ux-dialog-container[2]/div/div/div/div[2]/div/div/section/div/div[1]/div[2]/nav/div[1]/div/div/div[1]/a/span")
            print("success1")
            sleep(2)
            input_fields("/html/body/div[2]/ux-dialog-container[3]/div/div/div/div[2]/div/div/section/form/div/div/div[1]/div[1]/div[3]/fieldset/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/input", "test")
            sleep(1.5)
            button_click("/html/body/div[2]/ux-dialog-container[3]/div/div/div/div[2]/div/div/footer/section/nav/div/div[1]/a[2]")
            sleep(4.5)
            button_click("/html/body/div[2]/ux-dialog-container[3]/div/div/div/div[2]/div/div/header/nav[1]/div[2]/a[4]")
            print("batch opened")'''
        except Exception as e:
            print(f"failed to open batch, error: {e}")
    def process(self):
        def input_fields(xpath_input, str):
            field = self.driver.find_element('xpath', xpath_input)
            field.send_keys(str)

        def button_click(xpath_button):
            button = self.driver.find_element('xpath', xpath_button)
            button.click()

        actions = ActionChains(self.driver)
        def click_coords(xpath, x, y):
            element = self.driver.find_element('xpath', xpath)
            actions.move_to_element_with_offset(element, x, y).click().perform()
        def double_click_coords(xpath, x, y):
            element = self.driver.find_element('xpath', xpath)
            actions.move_to_element_with_offset(element, x, y).double_click().perform()
        def date_in(date, xpath_input):
            button = self.driver.find_element('xpath', xpath_input)
            button.click()
            field = self.driver.find_element('xpath', xpath_input)
            for i in date:
                num = [Keys.NUMPAD0, Keys.NUMPAD1, Keys.NUMPAD2, Keys.NUMPAD3, Keys.NUMPAD4, Keys.NUMPAD5, Keys.NUMPAD6, Keys.NUMPAD7, Keys.NUMPAD8, Keys.NUMPAD9]
                sleep(0.05)
                field.send_keys(num[int(i)])
        def read_element(xpath):
            element = self.driver.find_element('xpath', xpath)
            content = element.text
            return content
        sleep(1)
        #investigate what this is, I forgot
        '''try:
            for i in range(2):
                sleep(0.1)
                button_click("/html/body/div[2]/ux-dialog-container[2]/div/div/div/div[2]/div/div/section/div/div[1]/div[2]/section/div/div/div[1]/div/div[1]/div[1]/div[2]/div[2]")
            print("success2")'''
        # click "changed on" column twice to ensure newest batch appears at the top
        try:
            for i in range(2):
                sleep(0.25)
                button_click("/html/body/div[2]/ux-dialog-container[2]/div/div/div/div[2]/div/div/section/div/div[1]/div[2]/section/div/div/div[1]/div/div[5]/div/div/div[8]")
            print('1')
            double_click_coords("/html/body/div[2]/ux-dialog-container[2]/div/div/div/div[2]/div/div/section/div/div[1]/div[2]/section/div/div/div[1]/div/div[5]/div/div/div[8]", 0, 20)
        except Exception as e:
            print(f"failed to start process, error: {e}")

        path = "/Users/ricksarkar/PycharmProjects/MCEC_procurement/Invoices"
        Invoices = os.listdir(path)
        print(f"There are {len(Invoices)} Invoices to process")
        for invoice in Invoices:
            invoice_info = {}
            invoice_info['Invoice_path'] = f"{path}/{invoice}"
            print(invoice_info['Invoice_path'])
            invoice_info['invoice_number'] = "F17777369" #input("Invoice number?:")
            invoice_info['PO'] = "10359498" #input("PO #?:")
            invoice_info['date'] = "170223" #input("date? (ddmmyy):")
            invoice_info['gst'] = "2" #input("gst amount?:")
            invoice_info['amount'] = "219.64" #input("Invoice amount?:")
            invoice_info['#lineitems'] = "1" #str(input("# of line items?"))

        sleep(2)
        #click add and add from PO item
        try:
            button_click("/html/body/div[2]/ux-dialog-container[3]/div/div/div/div[2]/div/div/section/form/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/a[2]")
            sleep(0.2)
            click_coords("/html/body/div[2]/ux-dialog-container[3]/div/div/div/div[2]/div/div/section/form/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/a[2]", 0, 85)
        except Exception as e:
            print(f"failed to open process window, Error: {e}")

        sleep(2)

        #input items in first window
        try:
            input_fields("/html/body/div[2]/ux-dialog-container[4]/div/div/div/div[2]/div/div/section/form/div/div/div[1]/div[1]/div[3]/fieldset/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/input", invoice_info['invoice_number'])
            date_in(invoice_info['date'], "/html/body/div[2]/ux-dialog-container[4]/div/div/div/div[2]/div/div/section/form/div/div/div[1]/div[1]/div[3]/fieldset/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/input")
        except Exception as e:
            print("failed to load process window")
            sleep(0.4)
            button_click("/html/body/div[2]/ux-dialog-container[3]/div/div/div/div[2]/div/div/section/form/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/span[1]/span[2]/span[2]")
            button_click(
                "/html/body/div[2]/ux-dialog-container[3]/div/div/div/div[2]/div/div/section/form/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/a[2]")
            sleep(0.15)
            click_coords(
                "/html/body/div[2]/ux-dialog-container[3]/div/div/div/div[2]/div/div/section/form/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/a[2]",
                0, 90)


        try:
            sleep(0.7)
            input_fields("/html/body/div[2]/ux-dialog-container[4]/div/div/div/div[2]/div/div/section/form/div/div/div[2]/div[2]/div/div/div[2]/section/form/div/nav/div[1]/div/div/div/div[1]/div[1]/fieldset/div/div/div/div/div/div[2]/div/div/div/div/div/input", invoice_info['PO'])
            button_click("/html/body/div[2]/ux-dialog-container[4]/div/div/div/div[2]/div/div/section/form/div/div/div[2]/div[2]/div/div/div[2]/section/form/div/nav/div[2]/div[2]/a[1]")
            openPOlineitems = self.driver.find_elements('xpath', "//input[@type='checkbox']")
            openPOlineitems1 = self.driver.find_elements('xpath', "//input[@id='checkBoxInput']")
            print(openPOlineitems)
            '''for checkbox in openPOlineitems:
                print("Checkbox id:", checkbox.get_attribute("id"))
                print("Checkbox status:", checkbox.is_selected())'''
            print(f"there are {len(openPOlineitems)} open PO line items")
            print(f"there are {len(openPOlineitems1)} open PO line items1")
        except Exception as e:
            traceback_lines = traceback.format_exc().splitlines()
            print(f"error: {e}")
            print("".join(traceback_lines[:3]))



        #try: ask for input again and retry'''


bot = Ubot()
bot.openUbock()
sleep(4) #usually 8
bot.open_batch()
sleep(1)
bot.process()
sleep(300)