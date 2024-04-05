# 1 - Bibliotecas
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe (Opicional)
class Test_Produtos():


    # 2.1 Atributos
    url = "https://www.saucedemo.com"             # endereço do site alvo

    # 2.2 Funções e Métodos
    def setup_method(self, method):                     # método de inicialização dos testes
        self.driver = webdriver.Chrome()                # instancia o objeto do Selenium WebDriver como Chrome
        self.driver.implicitly_wait(10)                 # define o tempo de espera padrão por elementos em 10 segundos

    def teardown_method(self, method):                  # método de finalização dos testes
        self.driver.quit()                              # encerra / destrói o objeto do Selenium WebDriver da memória

    def test_selecionar_produto(self):                  # método de teste
        self.driver.get(self.url)                       # abre o navegador
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")                     # escreve no campo user-name
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")                     # escreve a senha
        self.driver.find_element(By.CSS_SELECTOR, "input.submit-button.btn_action").click()         # click no botao de login
        
        #transição de página
        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"               # confirma se stá escrito Products no elemento
        assert self.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack"   #confirma se é a mochila
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == "$29.99" # confirma o preço da mochila
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        assert self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Your Cart"
        assert self.driver.find_element(By.CLASS_NAME, "cart_quantity").text == "1"
        assert self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"
        assert self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text == "$29.99"
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()