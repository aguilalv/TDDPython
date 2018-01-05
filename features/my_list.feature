Feature: My list

    Scenario: Start a list and retrieve it later

        When I visit "http://localhost:8000/"
        Then I will see the page title mentions "To-Do"
        And I will see the page header mentions "To-Do"
        And I am invited to enter a to-do item straight away

        When I type "Buy peacock feathers" into a text box and press enter
        Then I will see the page updates and now lists "1:Buy peacock feathers"

