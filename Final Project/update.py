from lib2to3.pgen2 import driver
import unittest
import time
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestUpdate(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_update_user(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click() # klik fitur admin
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click() # klik button edit
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]').click() #dropdown user role
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys("Odis Adalwin") # isi employee name
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys("lulala") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]//html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div').click() #dropdown status
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys("Lulalula28*") # isi PASSWORD 
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys("Lulalula28*") # isi Konfirmasi Password
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]//html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click # tombol save
        time.sleep(1)

    def test_b_success_update_employee(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click() # klik fitur PIM
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click() # klik edit
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]').click() #dropdown user role
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys("Odis Adalwin") # isi employee name
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys("lulala") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]//html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div').click() #dropdown status
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys("Lulalula28*") # isi PASSWORD 
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys("Lulalula28*") # isi Konfirmasi Password
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]//html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click # tombol save
        time.sleep(1)

    def test_c_success_update_MyTimesheet(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click() # klik fitur Time
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click() # klik edit
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]').click() #dropdown user role
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys("Odis Adalwin") # isi employee name
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys("lulala") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]//html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div').click() #dropdown status
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys("Lulalula28*") # isi PASSWORD 
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys("Lulalula28*") # isi Konfirmasi Password
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]//html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click # tombol save
        time.sleep(1)
    
    def test_d_success_update_MyTimesheet_empty_project_activity(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click() # klik fitur Time
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click() # klik edit
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]').click() #dropdown user role
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys("Odis Adalwin") # isi employee name
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys("lulala") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]//html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div').click() #dropdown status
        browser.find_element(By.XPATH,'//*[@id="app"]//html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click # tombol save
        time.sleep(1)
    
    def test_e_success_update_candidates_empty_vacancies(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click() # klik fitur Recruitmen
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click() # klik add
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]').click() #dropdown user role
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys("Odis Adalwin") # isi employee name
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys("lulala") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]//html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div').click() #dropdown status
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys("Lulalula28*") # isi PASSWORD 
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys("Lulalula28*") # isi Konfirmasi Password
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]//html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click # tombol save
        time.sleep(1)
    
    def test_f_success_update_myinfo(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click() # klik fitur MyInfo
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click() # klik edit
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]').click() #dropdown user role
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys("Odis Adalwin") # isi employee name
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys("lulala") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]//html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div').click() #dropdown status
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys("Lulalula28*") # isi PASSWORD 
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys("Lulalula28*") # isi Konfirmasi Password
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]//html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click # tombol save
        time.sleep(1)

    
    def tearDown(self): 
      self.browser.close() 

if __name__ == "__main__": 
    unittest.main()