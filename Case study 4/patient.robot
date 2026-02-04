*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Hospital Application
Suite Teardown    Close Browser

*** Variables ***
${URL}    http://127.0.0.1:5000
${BROWSER}    chrome

*** Test Cases ***
Register Single Patient
    Enter Patient Details    Rahul    30    Male    Fever    Dr. Sharma

Register Multiple Patients
    [Template]    Enter Patient Details
    Amit    25    Male    Cold    Dr. Verma
    Neha    28    Female    Fever    Dr. Sharma

*** Keywords ***
Open Hospital Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Enter Patient Details
    [Arguments]    ${name}    ${age}    ${gender}    ${disease}    ${doctor}
    Input Text    name=name    ${name}
    Input Text    name=age     ${age}
    Click Element    xpath=//input[@value='${gender}']
    Input Text    name=disease    ${disease}
    Select From List By Label    name=doctor    ${doctor}
