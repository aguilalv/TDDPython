from selenium.webdriver.common.keys import Keys
import time

@when(u'I visit "{url}"')
def visit(context,url):
    context.browser.get(url)

@then(u'I will see the page title mentions "{expected_title}"')
def see_title_mentions(context,expected_title):
    title = context.browser.title
    context.test.assertIn(expected_title,title)

@then(u'I will see the page header mentions "{expected_header}"')
def see_header_mentions(context,expected_header):
    header = context.browser.find_element_by_tag_name('h1').text
    context.test.assertIn(expected_header,header)

@then(u'I will see a  text box and will be prompted to input "{expected_prompt}"')
def see_text_box_with_ptompt(context,expected_prompt):
    inputbox = context.browser.find_element_by_id('id_new_item')
    placeholder = inputbox.get_attribute('placeholder')
    context.test.assertEqual(placeholder,expected_prompt)

@when(u'I type "{text_input}" into a text box and press enter')
def type_text_and_press_enter(context,text_input):
    inputbox = context.browser.find_element_by_id('id_new_item')
    inputbox.send_keys(text_input)
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

@then(u'I will see the row lists "{expected_item}" item in a table')
def see_item_in_table(context,expected_item):
    table = context.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    context.test.assertIn(expected_item,[row.text for row in rows])

@given(u'I have typed "{text_input}" into a text box and press enter')
def typed_text_input(context,text_input):
    inputbox = context.browser.find_element_by_id('id_new_item')
    inputbox.send_keys(text_input)
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

