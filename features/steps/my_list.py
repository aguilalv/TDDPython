@when(u'I visit "{url}"')
def visit(context,url):
    context.browser.get(url)

@then(u'I will see the page title mentions "{expected_title}"')
def see_title_mentions(context,expected_title):
    title = context.browser.title
    context.test.assertIn(expected_title,title)

@then(u'I will see the page header mentions "To-Do"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I will see the page header mentions "To-Do"')

@then(u'I am invited to enter a to-do item straight away')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am invited to enter a to-do item straight away')

@when(u'I type "Buy peacock feathers" into a text box and press enter')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type "Buy peacock feathers" into a text box and press enter')

@then(u'I will see the page updates and now lists "1:Buy peacock feathers"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I will see the page updates and now lists "1:Buy peacock feathers"')
