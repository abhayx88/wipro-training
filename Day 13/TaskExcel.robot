*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=login_success_data.xlsx    sheet_name=Sheet1
Test Template    Login With Excel

*** Variables ***
${URL}      https://tutorialsninja.com/demo/
${BROWSER}  chrome

*** Keywords ***
Open TutorialsNinja
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains Element    xpath=//a[text()='My Account']    15s

Open Login Page
    # Click My Account (JS click – FIX)
    Execute Javascript    document.querySelector("a[title='My Account']").click()

    Wait Until Page Contains Element    xpath=//a[text()='Login']    10s

    # Click Login (JS click – FIX)
    Execute Javascript    document.querySelector("a[href*='account/login']").click()

    Wait Until Page Contains Element    id=input-email    15s

Login With Excel
    [Arguments]    ${email}    ${password}

    Open TutorialsNinja
    Open Login Page

    Wait Until Element Is Visible    id=input-email    10s
    Input Text    id=input-email       ${email}
    Input Text    id=input-password    ${password}

    # Click Login button (JS click – SAFE)
    Execute Javascript    document.querySelector("input[value='Login']").click()

    Verify Login Success
    Close Browser

Verify Login Success
    Wait Until Page Contains    My Account    15s
    Capture Page Screenshot

*** Test Cases ***
Login with valid data from Excel
