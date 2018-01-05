@when(u'I visit "{url}"')
def visit(context,url):
    context.browser.get(url)

@then(u'I will see the page title mentions "{expected_title}"')
def see_title_mentions(context,expected_title):
    title = context.browser.title
    context.test.assertIn(expected_title,title)

@then(u'I will see the page header mentions "{expected_header}"')
def see_header_mentions(context,expected_header):
    header = context.browser.find_element_by_tag_name('h1')
    context.text.assertIn(expected_header,header)

