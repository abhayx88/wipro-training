*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=testdata.xlsx    sheet_name=Sheet1
Test Template    OrangeHRM Login With Excel

*** Variables ***
${URL}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}   chrome

*** Keywords ***
Open OrangeHRM
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    name=username    15s

OrangeHRM Login With Excel
    [Arguments]    ${username}    ${password}    ${expected}

    Open OrangeHRM

    Clear Element Text    name=username
    Clear Element Text    name=password

    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Click Button    xpath=//button[@type='submit']

    Run Keyword If    '${expected}' == 'success'
    ...    Verify Successful Login
    ...    ELSE
    ...    Verify Login Failure

    Close Browser

Verify Successful Login
    Wait Until Element Is Visible    xpath=//span[@class='oxd-userdropdown-tab']    15s
    Capture Page Screenshot
    Logout From OrangeHRM

Verify Login Failure
    Wait Until Element Is Visible
    ...    xpath=//p[contains(@class,'oxd-alert-content-text')]    10s
    Capture Page Screenshot

Logout From OrangeHRM
    Click Element    xpath=//span[@class='oxd-userdropdown-tab']
    Wait Until Element Is Visible    xpath=//a[text()='Logout']    10s
    Click Element    xpath=//a[text()='Logout']
    Wait Until Element Is Visible    name=username    15s

*** Test Cases ***
Login with users from Excel
    ${username}    ${password}    ${expected}
