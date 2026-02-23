*** Settings ***
Resource    ../resources/base.resource

*** Variables ***
${SHOPPING_CART_LINK}      xpath=//span[text()='Shopping Cart']
${QUANTITY_FIELD}          xpath=//input[contains(@name,'quantity')]
${UPDATE_BUTTON}           xpath=//button[@data-original-title='Update']
${REMOVE_BUTTON}           xpath=//button[@data-original-title='Remove']
${CHECKOUT_LINK}           xpath=//a[contains(@href,'route=checkout/checkout')]
${CART_CONTENT}            xpath=//div[@id='content']
${CHECKOUT_URL}            ${URL}index.php?route=checkout/checkout
${CART_URL}                ${URL}index.php?route=checkout/cart
${REMOVE_FIRST_BUTTON}     xpath=(//button[@data-original-title='Remove'])[1]

*** Keywords ***
Open Cart Page
    Wait And Click    ${SHOPPING_CART_LINK}
    Log Operation    [Assert] Shopping cart page should be visible
    Assert Shopping Cart Page Is Visible

Cart Should Contain Product
    [Arguments]    ${product_name}
    Log Operation    [Assert] Product should be present in cart: ${product_name}
    Wait Until Element Is Visible    ${CART_CONTENT}
    Wait Until Page Contains         Shopping Cart
    ${cart_text}=    Get Text    ${CART_CONTENT}
    Should Contain    ${cart_text}    ${product_name}    msg=Item not found in cart: '${product_name}'.

Update Cart Quantity To
    [Arguments]    ${quantity}
    Wait Until Keyword Succeeds    5x    1s    Set Cart Quantity And Update    ${quantity}

Set Cart Quantity And Update
    [Arguments]    ${quantity}
    Wait Until Element Is Visible    ${QUANTITY_FIELD}
    Clear Element Text    ${QUANTITY_FIELD}
    Input Text            ${QUANTITY_FIELD}    ${quantity}
    Click Button          ${UPDATE_BUTTON}

Cart Quantity Should Be
    [Arguments]    ${expected_quantity}
    Log Operation    [Assert] Cart quantity should be ${expected_quantity}
    Wait Until Keyword Succeeds    5x    1s    Textfield Value Should Be    ${QUANTITY_FIELD}    ${expected_quantity}    msg=Cart quantity update failed. Expected '${expected_quantity}'.

Remove Product From Cart
    [Arguments]    ${product_name}=${EMPTY}
    IF    '${product_name}' == ''
        Wait Until Element Is Visible    ${REMOVE_BUTTON}
        Click Element    ${REMOVE_BUTTON}
    ELSE
        ${product_remove_button}=    Set Variable    xpath=//div[@id='content']//tr[.//a[contains(normalize-space(),'${product_name}')]]//button[@data-original-title='Remove']
        Wait Until Element Is Visible    ${product_remove_button}    10s
        Click Element    ${product_remove_button}
    END

Clear Cart Completely
    Go To    ${CART_URL}
    FOR    ${index}    IN RANGE    30
        ${has_item}=    Run Keyword And Return Status    Element Should Be Visible    ${REMOVE_FIRST_BUTTON}
        IF    not ${has_item}
            Exit For Loop
        END
        Click Element    ${REMOVE_FIRST_BUTTON}
        Sleep    0.5s
    END

Cart Should Not Contain Product
    [Arguments]    ${product_name}
    Log Operation    [Assert] Product should not be present in cart: ${product_name}
    Wait Until Keyword Succeeds    5x    1s    Assert Cart Does Not Contain Product    ${product_name}

Assert Cart Does Not Contain Product
    [Arguments]    ${product_name}
    Wait Until Element Is Visible    ${CART_CONTENT}
    ${cart_text}=    Get Text    ${CART_CONTENT}
    Should Not Contain    ${cart_text}    ${product_name}    msg=Item still present in cart: '${product_name}'.

Proceed To Checkout
    Wait Until Element Is Visible    ${CHECKOUT_LINK}
    Scroll Element Into View         ${CHECKOUT_LINK}
    Wait Until Keyword Succeeds    3x    1s    Click Element    ${CHECKOUT_LINK}
    ${location}=    Get Location
    IF    'route=checkout' not in $location
        Go To    ${CHECKOUT_URL}
    END
    Wait Until Keyword Succeeds    5x    1s    Location Should Contain    route=checkout

Assert Shopping Cart Page Is Visible
    Wait Until Page Contains    Shopping Cart    10s    Shopping cart page did not open.
