*** Settings ***
Resource    ../resources/base.resource

*** Variables ***
${MY_ACCOUNT_MENU}         xpath=//span[text()='My Account']
${LOGOUT_LINK}             xpath=//ul[@class='dropdown-menu dropdown-menu-right']//a[text()='Logout']
${FIRSTNAME_FIELD}         id=input-firstname
${LASTNAME_FIELD}          id=input-lastname
${EMAIL_FIELD}             id=input-email
${PHONE_FIELD}             id=input-telephone
${PASSWORD_FIELD}          id=input-password
${CONFIRM_FIELD}           id=input-confirm
${PRIVACY_POLICY_CHECKBOX}    name=agree
${CONTINUE_BUTTON}         xpath=//input[@value='Continue']
${LOGIN_BUTTON}            xpath=//input[@value='Login']
${ACCOUNT_PAGE_URL}        ${URL}index.php?route=account/account
${REGISTER_PAGE_URL}       ${URL}index.php?route=account/register
${LOGIN_PAGE_URL}          ${URL}index.php?route=account/login
${LOGOUT_PAGE_URL}         ${URL}index.php?route=account/logout

*** Keywords ***
Open Register Page
    Go To    ${REGISTER_PAGE_URL}
    Log Operation    [Assert] Register page should be visible
    Assert Register Page Is Visible

Open Login Page
    Go To    ${LOGIN_PAGE_URL}
    Log Operation    [Assert] Login page should be visible
    Assert Login Page Is Visible

Submit Registration Form
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${phone}    ${password}
    Input Text Safe    ${FIRSTNAME_FIELD}    ${firstname}
    Input Text Safe    ${LASTNAME_FIELD}     ${lastname}
    Input Text Safe    ${EMAIL_FIELD}        ${email}
    Input Text Safe    ${PHONE_FIELD}        ${phone}
    Input Text Safe    ${PASSWORD_FIELD}     ${password}
    Input Text Safe    ${CONFIRM_FIELD}      ${password}
    Select Checkbox    ${PRIVACY_POLICY_CHECKBOX}
    Click With Wait    ${CONTINUE_BUTTON}
    ${reached_success}=      Run Keyword And Return Status    Wait Until Location Contains    route=account/success    3s
    IF    not ${reached_success}
        ${register_form_still_visible}=    Run Keyword And Return Status    Wait Until Element Is Visible    ${PRIVACY_POLICY_CHECKBOX}    2s
        IF    ${register_form_still_visible}
            Log Operation    [Registration] First submit stayed on register page, retrying once
            Select Checkbox    ${PRIVACY_POLICY_CHECKBOX}
            Click With Wait    ${CONTINUE_BUTTON}
        END
    END

Submit Login Form
    [Arguments]    ${email}    ${password}
    Input Text Safe   ${EMAIL_FIELD}       ${email}
    Input Text Safe   ${PASSWORD_FIELD}    ${password}
    Click Button      ${LOGIN_BUTTON}

Logout From Account
    Silence Failure Screenshots
    ${menu_visible}=    Run Keyword And Return Status    Wait Until Element Is Visible    ${MY_ACCOUNT_MENU}    3s
    Enable Failure Screenshots
    IF    ${menu_visible}
        Silence Failure Screenshots
        ${logout_visible}=    Run Keyword And Return Status    Ensure Account Option Is Visible    ${LOGOUT_LINK}
        Enable Failure Screenshots
        IF    ${logout_visible}
            ${clicked_logout}=    Run Keyword And Return Status    Click With Wait    ${LOGOUT_LINK}
            IF    not ${clicked_logout}
                Go To    ${LOGOUT_PAGE_URL}
            END
        ELSE
            Go To    ${LOGOUT_PAGE_URL}
        END
    ELSE
        Go To    ${LOGOUT_PAGE_URL}
    END

Registration Should Be Successful
    Log Operation    [Assert] Registration should be successful
    ${location}=                 Get Location
    ${has_success_text}=         Run Keyword And Return Status    Page Should Contain    Your Account Has Been Created!
    ${at_success_url}=           Run Keyword And Return Status    Should Contain    ${location}    route=account/success
    ${email_exists_warning}=     Run Keyword And Return Status    Page Should Contain    Warning: E-Mail Address is already registered!
    ${privacy_warning}=          Run Keyword And Return Status    Page Should Contain    Warning: You must agree to the Privacy Policy!
    ${has_form_error}=           Run Keyword And Return Status    Element Should Be Visible    css=.text-danger
    Run Keyword If    ${email_exists_warning}    Fail    User not registered: e-mail already exists.
    Run Keyword If    ${privacy_warning}    Fail    User not registered: privacy policy agreement was not accepted.
    IF    ${has_form_error}
        ${error_text}=    Get Text    css=.text-danger
        Fail    User not registered: form validation error - ${error_text}
    END
    Run Keyword If    not (${has_success_text} or ${at_success_url})    Fail    User not registered: registration success was not confirmed.

Login Should Be Successful
    Log Operation    [Assert] Login should be successful
    Wait Until Keyword Succeeds    5x    1s    Validate Logged In State

Logout Should Be Successful
    Log Operation    [Assert] Logout should terminate session
    Wait Until Keyword Succeeds    5x    1s    Account Access Should Require Login

Account Access Should Require Login
    Go To    ${ACCOUNT_PAGE_URL}
    Wait Until Keyword Succeeds    5x    1s    Validate Access Redirected To Login

Validate Access Redirected To Login
    ${location}=            Get Location
    ${at_login_url}=        Run Keyword And Return Status    Should Contain    ${location}    route=account/login
    ${has_login_prompt}=    Run Keyword And Return Status    Page Should Contain    Returning Customer
    ${still_account}=       Run Keyword And Return Status    Should Contain    ${location}    route=account/account
    Run Keyword If    ${still_account}    Fail    Session is still active.
    Run Keyword If    not (${at_login_url} or ${has_login_prompt})    Fail    Login redirection was not confirmed.

Validate Logged In State
    ${location}=            Get Location
    Silence Failure Screenshots
    ${has_account_url}=     Run Keyword And Return Status    Should Contain    ${location}    route=account/account
    ${has_edit_account}=    Run Keyword And Return Status    Page Should Contain    Edit your account information
    ${has_login_error}=     Run Keyword And Return Status    Page Should Contain    Warning: No match for E-Mail Address and/or Password.
    Enable Failure Screenshots
    Run Keyword If    ${has_login_error}    Fail    Login failed: user not found or password is invalid.
    Run Keyword If    not (${has_account_url} or ${has_edit_account})    Fail    Login failed: account page was not reached.

Ensure Account Option Is Visible
    [Arguments]    ${option_locator}
    Silence Failure Screenshots
    ${option_visible}=    Run Keyword And Return Status    Element Should Be Visible    ${option_locator}
    Enable Failure Screenshots
    IF    not ${option_visible}
        Click With Wait    ${MY_ACCOUNT_MENU}
        Wait Until Element Is Visible    css=ul.dropdown-menu.dropdown-menu-right
        Wait Until Element Is Visible    ${option_locator}
        Wait Until Element Is Enabled    ${option_locator}
    END

Assert Register Page Is Visible
    Wait Until Location Contains    route=account/register    10s    Register page did not open.
    Wait Until Element Is Visible    ${FIRSTNAME_FIELD}    10s    First name field is not visible on Register page.
    Wait Until Element Is Visible    ${EMAIL_FIELD}    10s    E-mail field is not visible on Register page.

Assert Login Page Is Visible
    Wait Until Location Contains    route=account/login    10s    Login page did not open.
    Wait Until Element Is Visible    ${EMAIL_FIELD}    10s    E-mail field is not visible on Login page.
    Wait Until Element Is Visible    ${PASSWORD_FIELD}    10s    Password field is not visible on Login page.
