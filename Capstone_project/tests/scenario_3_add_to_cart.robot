*** Settings ***
Library    DataDriver    file=${CURDIR}/../testdata/e2e_master_data.csv
Resource   ../keywords/account_keywords.robot
Resource   ../keywords/product_keywords.robot
Resource   ../keywords/cart_keywords.robot

Test Setup     Open Application
Test Teardown  Close Application
Suite Teardown    Finalize Suite Screenshot Policy
Test Template  Scenario 3 Add To Cart

*** Test Cases ***
Add To Cart Scenario
    [Tags]    modular    scenario3

*** Keywords ***
Scenario 3 Add To Cart
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${phone}    ${password}    ${product}
    Login User With Shared Registration    ${firstname}    ${lastname}    ${email}    ${phone}    ${password}
    Clear Cart Before Scenario
    Search Product                 ${product}
    Open Product Details           ${product}
    Add Product To Cart
    Open Cart
    Verify Product Present In Cart    ${product}
