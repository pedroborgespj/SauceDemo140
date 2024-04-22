import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    # Setup / Inicialização
    context.driver = webdriver.Chrome()    #instanciar o objeto do Selenium WebDriver especializado para o Chrome
    context.driver.maximize_window()       # maximizar a janela do navegador
    context.driver.implicitly_wait(10)     # esperar até 10 segundos por qualquer elemento
    # Passo em si
    context.driver.get("https://www.saucedemo.com")  #abrir o navegador no endereço do site alvo

# Preencher com usuário e senha
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.NAME, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

# Preencher com usuário em branco e senha
@when(u'preencho os campos de login com usuario  e senha {senha}')
def step_impl(context, senha):
    # não preenche usuário
    context.driver.find_element(By.NAME, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

# Preencher com usuário, mas deixar a senha em branco
@when(u'preencho os campos de login com usuario {usuario} e senha ')
def step_impl(context, usuario):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    # não preenche senha
    context.driver.find_element(By.ID, "login-button").click()

# Clica no botão de login sem ter preenchido o usuario e a senha
@when(u'preencho os campos de login com usuario  e senha ')
def step_impl(context):
    # não preenche usuário
    # não preenche senha
    context.driver.find_element(By.ID, "login-button").click()

# Preencher com usuário e senha através da decisão (IF)
@when(u'digito os campos de login com usuario {usuario} e senha {senha} com IF')
def step_impl(context, usuario, senha):
    if usuario != '<branco>':
        context.driver.find_element(By.ID, "user-name").send_keys(usuario)
        # se o usuário estiver em <branco> não há ação de preenchimento

    if senha != '<branco>':
        context.driver.find_element(By.NAME, "password").send_keys(senha)
        # se a senha estiver em <branco> não há ação de preenchimento
    
    context.driver.find_element(By.ID, "login-button").click()

@when(u'acesso a página de produtos')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"

@when(u'verifico os dados do produto Sauce Labs Backpack')
def step_impl(context):
    assert context.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack"
    assert context.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == "$29.99"

@when(u'adiciono o produto ao carrinho')
def step_impl(context):
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

@when(u'acesso o carrinho')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Your Cart"

@when(u'removo o produto do carrinho')
def step_impl(context):
    context.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

@when(u'faço logout')
def step_impl(context):
    context.driver.find_element(By.ID, "react-burger-menu-btn").click()
    context.driver.find_element(By.ID, "logout_sidebar_link").click()

@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    # time.sleep(2)

    # teardown / encerramento
    context.driver.quit()

@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"

    context.driver.quit()

# Verifica a mensagem para o Scenario Outline
@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem

    context.driver.quit()

@then(u'o produto "Sauce Labs Backpack" é adicionado ao carrinho com sucesso')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"

    context.driver.quit()

@then(u'os detalhes do produto "Sauce Labs Backpack" são exibidos corretamente no carrinho')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "cart_quantity").text == "1"
    assert context.driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"
    assert context.driver.find_element(By.CLASS_NAME, "inventory_item_price").text == "$29.99"

    context.driver.quit()

@then(u'o usuário é redirecionado para a página de login')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()

    context.driver.quit()

