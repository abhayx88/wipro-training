*** Settings ***
Resource    ../resources/base.resource

*** Keywords ***
Checkout Page Should Be Visible
    Log Operation    [Assert] Checkout page should be visible
    Wait Until Keyword Succeeds    5x    1s    Location Should Contain    route=checkout
    Page Should Contain    Checkout
    ${location}=                Get Location
    ${has_billing_details}=     Run Keyword And Return Status    Page Should Contain    Billing Details
    ${has_delivery_details}=    Run Keyword And Return Status    Page Should Contain    Delivery Details
    ${has_payment_method}=      Run Keyword And Return Status    Page Should Contain    Payment Method
    ${has_checkout_cart_url}=   Run Keyword And Return Status    Should Contain    ${location}    route=checkout/cart
    Run Keyword If    not (${has_billing_details} or ${has_delivery_details} or ${has_payment_method} or ${has_checkout_cart_url})    Fail    Checkout page loaded but expected checkout sections were not found.
