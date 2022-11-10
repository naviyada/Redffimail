# We will automate the Login page of Rediffmail Account
  # As the number of rows present in EXAMPLE keyword, Feature file will run those number of times

  Feature: login Rediffmail
    Scenario Outline: login data
      Given we navigate to Rediffmail account
      When we validate the username text
      And we type in the "<username>" edit box
      And we validate the password text
      And we type in the "<password>" field
      And we click on the sign in button
      Then type "<searchtext>" in search bar
      And click on search button

      Examples:

        | username | password | searchtext |
      |  selenium.testmay1999| Dilee@123 | welcome |
      | naveennani.2022@ | Dilee@123 |  welcome |
      |  selenium.testmay1999| test@123| welcome |
      | selenium.testmay20171 | test@123431 | welcome |

