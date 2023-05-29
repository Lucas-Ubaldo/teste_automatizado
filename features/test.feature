Feature: Pesquisa no youtube
  Scenario: Search for a corinthians
    Given I am on the youtube homepage
    When I search for "corinthians"
    Then I should see search results
    When I click on the first video
    Then I should be on the video page


  
