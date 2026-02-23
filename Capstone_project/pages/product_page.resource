*** Settings ***
Resource    ../resources/base.resource

*** Variables ***
${SEARCH_FIELD}            name=search
${SEARCH_BUTTON}           xpath=//button[@class='btn btn-default btn-lg']
${PRODUCT_TITLE_HEADER}    css=div#content h1
${ADD_TO_CART_BUTTON}      id=button-cart
${SUCCESS_ALERT}           css=.alert-success

*** Keywords ***
Search For Product
    [Arguments]    ${product_name}
    Log Operation    [Assert] Search controls should be visible
    Assert Search Controls Are Visible
    Input Text Safe    ${SEARCH_FIELD}    ${product_name}
    Click Button       ${SEARCH_BUTTON}
    Product Search Should Return Result    ${product_name}

Open Product Details Page
    [Arguments]    ${product_name}
    ${product_link}=    Set Variable    xpath=//div[contains(@class,'product-thumb')]//a[contains(normalize-space(),'${product_name}')]
    Wait Until Element Is Visible    ${product_link}
    Scroll Element Into View         ${product_link}
    Click Element                    ${product_link}

Add Current Product To Cart
    Click Button    ${ADD_TO_CART_BUTTON}

Product Page Should Match
    [Arguments]    ${product_name}
    Log Operation    [Assert] Product details page should match searched product
    Element Text Should Be    ${PRODUCT_TITLE_HEADER}    ${product_name}

Add To Cart Should Be Successful
    Log Operation    [Assert] Add to cart should succeed
    Wait Until Element Is Visible    ${SUCCESS_ALERT}
    Element Should Contain    ${SUCCESS_ALERT}    Success

Product Search Should Return Result
    [Arguments]    ${product_name}
    Log Operation    [Assert] Product should exist in search results
    ${no_match}=    Run Keyword And Return Status    Page Should Contain    There is no product that matches the search criteria.
    Run Keyword If    ${no_match}    Fail    Product not found: '${product_name}'.
    ${product_link}=    Set Variable    xpath=//div[contains(@class,'product-thumb')]//a[contains(normalize-space(),'${product_name}')]
    Wait Until Element Is Visible    ${product_link}    10s    Product not found in search results: '${product_name}'.

Assert Search Controls Are Visible
    Wait Until Element Is Visible    ${SEARCH_FIELD}    10s    Search field is not visible.
    Wait Until Element Is Visible    ${SEARCH_BUTTON}    10s    Search button is not visible.
