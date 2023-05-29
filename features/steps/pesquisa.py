from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@given('I am on the youtube homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()  # Use o driver correto para o navegador que você está usando
    context.driver.get("https://www.youtube.com/")

@when('I search for "{keyword}"')
def step_impl(context, keyword):
    search_box = context.driver.find_element(By.NAME, "search_query")
    search_box.send_keys(keyword)
    search_box.submit()

@then('I should see search results')
def step_impl(context):
    search_results = context.driver.find_elements(By.ID, "container")
    assert len(search_results) >= 1

@then('I should see no search results')
def step_impl(context):
    assert "No results found" in context.driver.page_source

@when('I click on the first video')
def step_impl(context):
    first_video = context.driver.find_element(By.CSS_SELECTOR, "ytd-video-renderer #thumbnail")
    first_video.click()

@then('I should be on the video page')
def step_impl(context):
    assert "youtube.com/watch" in context.driver.current_url
    sleep(10)

def after_scenario(context, scenario):
    context.driver.quit()
