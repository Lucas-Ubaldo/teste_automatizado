from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#OK
@given('que estou na página de login do YouTube')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.youtube.com')

    # Aguarde até que o elemento seja visível
    button_locator = (By.XPATH, '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a')
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(button_locator))

    # Clique no botão de login
    login_button = context.driver.find_element(*button_locator)
    login_button.click()

@when('eu insiro meu email "{email}"')
def step_impl(context, email):
    email_input = context.driver.find_element(By.ID, 'identifierId')
    email_input.send_keys(email)

    next_button = context.driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
    next_button.click()

    sleep(2)

@when('eu insiro minha senha "{senha}"')
def step_impl(context, senha):
    wait = WebDriverWait(context.driver, 10)
    senha_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
    
    if senha_input.is_displayed() and senha_input.is_enabled():
        senha_input.clear()
        senha_input.send_keys(senha)
    else:
        raise Exception("Campo de senha não está visível ou habilitado.")

    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button')))
    next_button.click()

    sleep(2)

@when('eu pesquiso por "{termo_pesquisa}"')
def step_impl(context, termo_pesquisa):
    search_input = context.driver.find_element(By.NAME, 'search_query')
    search_input.clear()
    search_input.send_keys(termo_pesquisa)
    search_input.send_keys(Keys.RETURN)

    sleep(2)

@when('eu clico e reproduzo o primeiro vídeo')
def step_impl(context):
    video_link = context.driver.find_element(By.CSS_SELECTOR, '#contents ytd-video-renderer a#thumbnail')
    video_link.click()

    # Aguarda o vídeo carregar e reproduzir
    sleep(5)

@when('eu clico no botão de Inscrever-se')
def step_impl(context):
    subscribe_button = context.driver.find_element(By.CSS_SELECTOR, '#subscribe-button')
    subscribe_button.click()
    sleep(2)

@when('eu clico no botão de Gostei')
def step_impl(context):
    like_button = context.driver.find_element(By.ID, 'segmented-like-button')
    like_button.click()
    sleep(2)

@then('eu devo ver o vídeo sendo reproduzido')
def step_impl(context):
    sleep(5)
    search_results = context.driver.find_elements(By.CSS_SELECTOR, '#contents ytd-video-renderer')
    assert len(search_results) >= 1, "Nenhum resultado de pesquisa encontrado"
