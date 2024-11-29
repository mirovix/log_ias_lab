import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


def run():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("-private")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://deilabs.dei.unipd.it/login")

        user_email_field = driver.find_element(By.NAME, "email")
        user_email_field.send_keys("mihailovic")

        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("orimorim2.+")

        time.sleep(1)
        action_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')

        driver.execute_script("arguments[0].scrollIntoView(true);", action_button)

        if action_button.is_displayed():
            action_button.click()
        else:
            print("Elemento non visibile")

        time.sleep(3)
        if driver.current_url == "https://deilabs.dei.unipd.it/home":
            print("Pagina successiva caricata!")
        else:
            print("Errore nel caricamento della pagina successiva!")

        driver.get("https://deilabs.dei.unipd.it/laboratory_in_outs")
        print("Pagina dei laboratori caricata!")

        exit_button = driver.find_elements(By.CSS_SELECTOR, "input[type='submit'][value^='Exit from']")
        if exit_button:
            print("Il laboratorio è già stato selezionato!")
        else:
            laboratory_dropdown = driver.find_element(By.ID, "laboratory_id")
            select = Select(laboratory_dropdown)
            select.select_by_visible_text("DEI/O | SSL Lab")  # Seleziona per nome

            time.sleep(2)
            print("Laboratorio selezionato!")

            enter_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Enter']")
            enter_button.click()
            time.sleep(3)
            print("Pulsante 'Enter' cliccato!")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")

    finally:
        driver.quit()

run()
