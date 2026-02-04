*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}             https://www.google.com
${BROWSER}         chrome
${EXPECTED_TITLE}  Google

*** Test Cases ***
Verify Page Title and Capture Screenshot
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    ${EXPECTED_TITLE}
    Capture Page Screenshot
    Close Browser
