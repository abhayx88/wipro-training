*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://www.seleniumeasy.com/test/input-form-demo.html
${BROWSER}    Chrome

*** Test Cases ***
Validate Form Submission Using Built-in Keywords
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window


    Input Text    name=first_name    Abhay
    Input Text    name=last_name     Gupta
    Input Text    name=email         abhay@gmail.com
    Input Text    name=phone         9876543210
    Input Text    name=address       Bhopal
    Input Text    name=city          Bhopal


    Select From List By Value    name=state    MP

    Click Element    xpath=//input[@value='yes']

    Click Element    name=hosting

    ${title}=    Get Title
    Run Keyword If    '${title}' != ''    Log    Page loaded successfully

    Click Button    xpath=//button[@type='submit']

    Sleep    3s

    ${current_url}=    Get Location
    Should Be Equal    ${current_url}    ${URL}

    Close Browser
