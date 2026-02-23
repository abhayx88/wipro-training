*** Settings ***
Library    DataDriver    file=${CURDIR}/../testdata/e2e_master_data.csv
Resource   ../keywords/account_keywords.robot
Resource   ../keywords/product_keywords.robot
Resource   ../keywords/cart_keywords.robot

Test Setup     Open Application
Test Teardown  Close Application
Suite Teardown    Finalize Suite Screenshot Policy
Test Template  Scenario 4 Update Remove Cart

*** Test Cases ***
Update Remove Cart Scenario
    [Tags]    modular    scenario4

*** Keywords ***
Scenario 4 Update Remove Cart
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${phone}    ${password}    ${product}    ${quantity}
    Login User With Shared Registration    ${firstname}    ${lastname}    ${email}    ${phone}    ${password}
    Clear Cart Before Scenario
    Search Product                 ${product}
    Open Product Details           ${product}
    Add Product To Cart
    Open Cart
    Verify Product Present In Cart    ${product}
    Update Quantity                   ${quantity}
    Remove Product                    ${product}
    Verify Product Not Present In Cart    ${product}
