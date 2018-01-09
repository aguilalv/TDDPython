Feature: My list

    Scenario: Start a list and retrieve it later

        When I visit "http://localhost:8000/"
        Then I will see the page title mentions "To-Do"
        And I will see the page header mentions "To-Do"
        And I will see a  text box and will be prompted to input "Enter a to-do item"

        When I type "Buy peacock feathers" into a text box and press enter
        Then I will see the row lists "1: Buy peacock feathers" item in a table
        And I will see a  text box and will be prompted to input "Enter a to-do item"
 
        Given I have typed "Buy peacock feathers" into a text box and press enter
        When I type "Use peacock feathers to make a fly" into a text box and press enter
        Then I will see the row lists "1:Buy peacock feathers" item in a table
        And I will see the row lists "2:Use peacock feathers to make a fly" item in a table
        
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there

        # Satisfied, she goes back to sleep
