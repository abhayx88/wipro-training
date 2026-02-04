*** Settings ***
Library           SeleniumLibrary

Suite Setup       Suite Setup Keyword
Suite Teardown    Suite Teardown Keyword
Test Setup        Test Setup Keyword
Test Teardown     Test Teardown Keyword

*** Variables ***
${URL}    https://example.com
${BROWSER}    Chrome

*** Test Cases ***
Verify Page Title
    [Tags]    smoke    regression
    Open Browser    ${URL}    ${BROWSER}
    Title Should Be    Example Domain
    Close Browser

Verify Page Contains Text
    [Tags]    sanity
    Open Browser    ${URL}    ${BROWSER}
    Page Should Contain    Example Domain
    Close Browser

*** Keywords ***
Suite Setup Keyword
    Log    ===== SUITE SETUP STARTED =====

Suite Teardown Keyword
    Log    ===== SUITE TEARDOWN COMPLETED =====

Test Setup Keyword
    Log    --- TEST SETUP STARTED ---

Test Teardown Keyword
    Log    --- TEST TEARDOWN COMPLETED ---
