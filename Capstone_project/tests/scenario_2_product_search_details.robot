*** Settings ***
Library    DataDriver    file=${CURDIR}/../testdata/e2e_master_data.csv
Resource   ../keywords/account_keywords.robot
Resource   ../keywords/product_keywords.robot

Test Setup     Open Application
Test Teardown  Close Application
Suite Teardown    Finalize Suite Screenshot Policy
Test Template  Scenario 2 Product Search Details

*** Test Cases ***
Product Search Details Scenario
    [Tags]    modular    scenario2

*** Keywords ***
Scenario 2 Product Search Details
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${phone}    ${password}    ${product}
    Login User With Shared Registration    ${firstname}    ${lastname}    ${email}    ${phone}    ${password}
    Search Product        ${product}
    Open Product Details  ${product}
