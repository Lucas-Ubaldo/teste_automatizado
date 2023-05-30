from behave import given, when, then
from selenium import webdriver
import pyautogui
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
    button_locator = (By.XPATH, '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a')
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(button_locator))
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

@when('eu clico no botão de Salvar em "Assistir mais tarde"')
def step_impl(context):
    options_button = context.driver.find_element(By.XPATH, '//*[@id="button-shape"]/button')
    options_button.click()
    sleep(2)
    save_button = context.driver.find_element(By.XPATH, '//*[@id="items"]/ytd-menu-service-item-renderer[2]')
    save_button.click()
    sleep(2)
    save_to = context.driver.find_element(By.ID, 'checkboxContainer')
    save_to.click()
    sleep(2)

@then('eu devo ver o vídeo sendo reproduzido')
def step_impl(context):
    sleep(5)
    search_results = context.driver.find_elements(By.CSS_SELECTOR, '#contents ytd-video-renderer')
    assert len(search_results) >= 1, "Nenhum resultado de pesquisa encontrado"

@then('o vídeo deve ser salvo em "Assistir mais tarde"')
def step_impl(context):
    context.driver.get('https://www.youtube.com/playlist?list=WL')
    sleep(2)
    videos = context.driver.find_elements(By.CSS_SELECTOR, '#contents ytd-playlist-video-renderer')
    assert len(videos) >= 1, "O vídeo não foi salvo em 'Assistir mais tarde'"

@when('eu clico no botão de upload de vídeo')
def step_impl(context):
    upload_button = context.driver.find_element(By.XPATH, '//*[@id="button"]/a')
    upload_button.click()
    sleep(2)
    send_video = context.driver.find_element(By.XPATH, '//*[@id="items"]/ytd-compact-link-renderer[1]')
    send_video.click()
    sleep(2)

@when('eu escolho o vídeo "{caminho_video}" para enviar')
def step_impl(context, caminho_video):
    file_input = context.driver.find_element(By.ID, 'select-files-button')
    file_input.send_keys(caminho_video)
    sleep(2)
    # Uso do pyautogui para interagir com o explorador de arquivos
    pyautogui.write(caminho_video)  
    pyautogui.press('enter')  
    sleep(5)  

@when('eu insiro o título do vídeo "{titulo}"')
def step_impl(context, titulo):
    title_input = context.driver.find_element(By.ID, 'textbox')
    title_input.clear()
    title_input.send_keys(titulo)
    sleep(2)
    public_button = context.driver.find_element(By.ID, 'offRadio')
    public_button.click()
    sleep(2)

@when('eu clico no botão de próximo')
def step_impl(context):
    next_button = context.driver.find_element(By.ID, 'next-button')
    next_button.click()
    sleep(2)
    next_button = context.driver.find_element(By.ID, 'next-button')
    next_button.click()
    sleep(2)
    next_button = context.driver.find_element(By.ID, 'next-button')
    next_button.click()
    sleep(2)
    private_button = context.driver.find_element(By.XPATH, '//*[@id="private-radio-button"]') 
    private_button.click()
    sleep(2)

@when('eu clico no botão de publicar')
def step_impl(context):
    publish_button = context.driver.find_element(By.ID, 'done-button')
    publish_button.click()
    sleep(2)
    
@when('eu sou redirecionado para a página de upload após a publicação')
def step_impl(context):
    expected_url = 'https://studio.youtube.com/channel/UCLY2hOUiEuC-1zRWt5GqiJg/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D'
    assert context.driver.current_url == expected_url, "A página não foi redirecionada corretamente"
    sleep(10)