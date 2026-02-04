*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser To Login Page
Suite Teardown    Close Browser
Test Template    Login Test Template

*** Test Cases ***
Login Test 1    tomsmith     SuperSecretPassword!
Login Test 2    wronguser    wrongpass
Login Test 3    tomsmith     wrongpass

*** Keywords ***
Open Browser To Login Page
    Open Browser    https://the-internet.herokuapp.com/login    chrome
    Maximize Browser Window
    Wait Until Element Is Visible    id=username    10s

Enter Username
    [Arguments]    ${username}
    Input Text    id=username    ${username}

Enter Password
    [Arguments]    ${password}
    Input Text    id=password    ${password}

Click Login Button
    Click Button    css=button[type="submit"]

Verify Login Result
    Run Keyword And Ignore Error    Page Should Contain    You logged into a secure area

Close Browser
    Close Browser

Login Test Template
    [Arguments]    ${username}    ${password}
    Enter Username    ${username}
    Enter Password    ${password}
    Click Login Button
    Verify Login Result
