
*** Settings ***
Resource    ../pages/cart_page.resource
Resource    ../pages/product_page.resource
Resource    ../pages/checkout_page.resource

*** Keywords ***
Add Product To Cart
    Log Operation    [Cart] Adding current product to cart
    Add Current Product To Cart
    Add To Cart Should Be Successful

Open Cart
    Log Operation    [Cart] Opening shopping cart
    Open Cart Page

Clear Cart Before Scenario
    Log Operation    [Cart] Clearing cart before scenario
    Clear Cart Completely

Update Quantity
    [Arguments]    ${quantity}=2
    Log Operation    [Cart] Updating quantity to ${quantity}
    Update Cart Quantity To    ${quantity}
    Cart Quantity Should Be    ${quantity}

Remove Product
    [Arguments]    ${product_name}=${EMPTY}
    Log Operation    [Cart] Removing product from cart: ${product_name}
    Remove Product From Cart    ${product_name}

Verify Product Not Present In Cart
    [Arguments]    ${product_name}
    Log Operation    [Cart] Verifying product removed: ${product_name}
    Cart Should Not Contain Product    ${product_name}

Verify Product Present In Cart
    [Arguments]    ${product_name}
    Log Operation    [Cart] Verifying product present: ${product_name}
    Cart Should Contain Product    ${product_name}

Proceed Through Checkout
    Proceed To Checkout
    Checkout Page Should Be Visible
