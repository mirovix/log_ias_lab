import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class LogLab:
    def __init__(self, username: str, password: str, laboratory_name: str = "DEI/O | SSL Lab"):
        self.username = username
        self.password = password
        self.laboratory_name = laboratory_name

        self.login_url = "https://deilabs.dei.unipd.it/login"
        self.home_url = "https://deilabs.dei.unipd.it/home"
        self.laboratory_url = "https://deilabs.dei.unipd.it/laboratory_in_outs"

    @staticmethod
    def _set_driver() -> webdriver.Chrome:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("-private")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        print("Driver inizializzato!")
        return driver

    def _login(self, driver: webdriver.Chrome):
        driver.get(self.login_url)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "email")))
        user_email_field = driver.find_element(By.NAME, "email")
        user_email_field.send_keys(self.username)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(self.password)

        action_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
        driver.execute_script("arguments[0].scrollIntoView(true);", action_button)

        if action_button.is_displayed():
            action_button.click()
        else:
            print("Login: Elemento non visibile")

        WebDriverWait(driver, 10).until(EC.url_to_be(self.home_url))
        print("Pagina di login caricata!")

    def _select_laboratory(self, driver: webdriver.Chrome):
        time.sleep(2)
        laboratory_dropdown = driver.find_element(By.ID, "laboratory_id")
        select = Select(laboratory_dropdown)
        select.select_by_visible_text(self.laboratory_name)

        time.sleep(2)
        print("Laboratorio selezionato!")

        enter_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Enter']")
        enter_button.click()
        time.sleep(3)
        print("Pulsante 'Enter' cliccato!")

    def _check_login_status(self, driver: webdriver.Chrome) -> None:
        if driver.current_url == self.home_url:
            print("Pagina successiva caricata!")
        else:
            print("Errore nel caricamento della pagina successiva!")
            sys.exit(1)

    def _check_lab_status(self, driver: webdriver.Chrome) -> None:
        driver.get(self.laboratory_url)

        exit_button = driver.find_elements(By.CSS_SELECTOR, "input[type='submit'][value^='Exit from']")
        if exit_button:
            print("Il laboratorio è già stato selezionato!")
            sys.exit(0)
        print("Pagina dei laboratori caricata!")

    def run(self):
        driver = self._set_driver()
        try:
            self._login(driver)
            self._check_login_status(driver)
            self._check_lab_status(driver)
            self._select_laboratory(driver)
        except Exception as e:
            print(f"Si è verificato un errore: {e}")
        finally:
            driver.quit()
