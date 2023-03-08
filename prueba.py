from selenium import webdriver
import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import time
driver = webdriver.Chrome(executable_path=r'E:\\Proyectos\\pruebas\\chromedriver.exe') 
driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://accounts.google.com/AccountChooser/signinchooser?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser")
driver.set_window_size(1044, 600) #ventana
buscador = webdriver.find_element_by_name("q") #asigna
buscador.send_keys("accounts gmail",Keys.ENTER) # envia y busca 

print ("La aplicacion accounts gmail es:",driver.title)
print ("La aplicacion URL es:",driver.current_url)
driver.quit()

time.sleep(16)
