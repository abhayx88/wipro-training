
*** Settings ***
Resource    ../pages/product_page.resource

*** Variables ***
${DEFAULT_SEARCH_PRODUCT}    iPhone

*** Keywords ***
Search Product
    [Arguments]    ${product_name}=${DEFAULT_SEARCH_PRODUCT}
    Log Operation    [Product] Searching for product: ${product_name}
    Search For Product    ${product_name}
    Page Should Contain   ${product_name}

Open Product Details
    [Arguments]    ${product_name}=${DEFAULT_SEARCH_PRODUCT}
    Log Operation    [Product] Opening product details: ${product_name}
    Open Product Details Page    ${product_name}
    Product Page Should Match    ${product_name}
