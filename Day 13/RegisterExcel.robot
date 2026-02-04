*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=register_3inputs.xlsx    sheet_name=Sheet1
Test Template    Register With Excel (3 Inputs)

*** Variables ***
${URL}      https://tutorialsninja.com/demo/
${BROWSER}  chrome

*** Keywords ***
Open TutorialsNinja
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains Element    xpath=//a[@title='My Account']    15s

Open Register Page
    Execute Javascript    document.querySelector("a[title='My Account']").click()
    Wait Until Page Contains Element    xpath=//a[text()='Register']    10s
    Execute Javascript    document.querySelector("a[href*='account/register']").click()
    Wait Until Page Contains Element    id=input-firstname    15s

Register With Excel (3 Inputs)
    [Arguments]    ${firstname}    ${email}    ${password}

    Open TutorialsNinja
    Open Register Page

    # 3 INPUTS FROM EXCEL
    Input Text    id=input-firstname    ${firstname}
    Input Text    id=input-lastname     User
    Input Text    id=input-email        ${email}
    Input Text    id=input-telephone    9999999999
    Input Text    id=input-password     ${password}
    Input Text    id=input-confirm      ${password}

    # Newsletter = No
    Execute Javascript    document.querySelector("input[name='newsletter'][value='0']").click()

    # Accept Privacy Policy
    Execute Javascript    document.querySelector("input[name='agree']").click()

    # Submit
    Execute Javascript    document.querySelector("input[value='Continue']").click()

    Verify Registration Success
    Close Browser

Verify Registration Success
    Wait Until Page Contains    Your Account Has Been Created!    15s
    Capture Page Screenshot

*** Test Cases ***
Register users from Excel
