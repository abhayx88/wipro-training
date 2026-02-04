*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}  chrome

*** Keywords ***
Open OrangeHRM
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//input[@placeholder='Username']    10s

OrangeHRM Login
    [Arguments]    ${username}    ${password}
    Input Text    xpath=//input[@placeholder='Username']    ${username}
    Input Text    xpath=//input[@placeholder='Password']    ${password}
    Capture Page Screenshot    beforelogin.png
    Click Button    xpath=//button[@type='submit']
    Wait Until Page Contains Element    xpath=//span[text()='Dashboard']    10s
    Capture Page Screenshot    afterlogin.png
    Close Browser

*** Test Cases ***
TC005_DD
    Open OrangeHRM
    OrangeHRM Login    Admin    admin123
