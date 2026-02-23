
*** Settings ***
Resource    ../pages/account_page.resource
Library     Collections

*** Variables ***
${DEFAULT_FIRSTNAME}     Test
${DEFAULT_LASTNAME}      User
${DEFAULT_REG_PHONE}     9999999999
${DEFAULT_REG_PASSWORD}  Password123

*** Keywords ***
Navigate To Register Page
    Open Register Page

Fill Registration Form
    [Arguments]    ${firstname}=${DEFAULT_FIRSTNAME}    ${lastname}=${DEFAULT_LASTNAME}    ${email}=${NONE}    ${phone}=${DEFAULT_REG_PHONE}    ${password}=${DEFAULT_REG_PASSWORD}
    IF    $email is None
        ${email}=    Evaluate    f"qa_{int(time.time()*1000)}@example.com"    modules=time
    END
    Log Operation    [Registration] Registering user ${firstname} ${lastname} with email ${email}
    Submit Registration Form    ${firstname}    ${lastname}    ${email}    ${phone}    ${password}
    Registration Should Be Successful

Login User
    Login User With Shared Registration

Login User With Fresh Registration
    [Arguments]    ${firstname}=${DEFAULT_FIRSTNAME}    ${lastname}=${DEFAULT_LASTNAME}    ${phone}=${DEFAULT_REG_PHONE}    ${password}=${DEFAULT_REG_PASSWORD}
    ${email}    ${password}=    Register New User And Return Credentials    ${firstname}    ${lastname}    ${phone}    ${password}
    Logout From Account
    Logout Should Be Successful
    Login User With Credentials    ${email}    ${password}

Login User With Shared Registration
    [Arguments]    ${firstname}=${DEFAULT_FIRSTNAME}    ${lastname}=${DEFAULT_LASTNAME}    ${email}=${NONE}    ${phone}=${DEFAULT_REG_PHONE}    ${password}=${DEFAULT_REG_PASSWORD}
    IF    $email is None
        Fail    Manual email is required. Pass email from test data.
    END
    Log Operation    [Account] Trying login first with manual email ${email}
    ${login_ok}=    Run Keyword And Return Status    Login User With Credentials    ${email}    ${password}
    IF    not ${login_ok}
        Log Operation    [Account] Login failed for ${email}; registering user and retrying login
        ${registered_email}    ${registered_password}=    Register New User And Return Credentials    ${firstname}    ${lastname}    ${phone}    ${password}    ${email}
        Logout From Account
        Logout Should Be Successful
        Login User With Credentials    ${registered_email}    ${registered_password}
    END

Login User With Credentials
    [Arguments]    ${email}    ${password}
    Log Operation    [Login] Logging in with ${email}
    Open Login Page
    Submit Login Form    ${email}    ${password}
    Login Should Be Successful

Register New User And Return Credentials
    [Arguments]    ${firstname}=${DEFAULT_FIRSTNAME}    ${lastname}=${DEFAULT_LASTNAME}    ${phone}=${DEFAULT_REG_PHONE}    ${password}=${DEFAULT_REG_PASSWORD}    ${email}=${NONE}
    IF    $email is None
        ${email}=    Evaluate    f"qa_{int(time.time()*1000)}@example.com"    modules=time
    END
    Log Operation    [Registration] Creating user ${firstname} ${lastname} with ${email}
    Open Register Page
    Submit Registration Form    ${firstname}    ${lastname}    ${email}    ${phone}    ${password}
    Registration Should Be Successful
    RETURN    ${email}    ${password}

Ensure Shared User Pool Exists
    ${has_shared_emails}=       Run Keyword And Return Status    Variable Should Exist    ${SHARED_USER_EMAILS}
    ${has_shared_passwords}=    Run Keyword And Return Status    Variable Should Exist    ${SHARED_USER_PASSWORDS}
    IF    ${has_shared_emails} and ${has_shared_passwords}
        RETURN
    END
    Prepare Shared Users For Full Run

Prepare Shared Users For Full Run
    [Arguments]    ${firstname}=${DEFAULT_FIRSTNAME}    ${lastname}=${DEFAULT_LASTNAME}    ${phone}=${DEFAULT_REG_PHONE}    ${password}=${DEFAULT_REG_PASSWORD}
    ${run_id}=        Evaluate    datetime.datetime.now().strftime("%Y%m%d%H%M%S")    modules=datetime
    Log Operation     [Setup] Initializing dynamic shared user pool for run ${run_id}
    ${emails}=        Create List
    ${passwords}=     Create List
    Set Global Variable    ${SHARED_USER_EMAILS}       ${emails}
    Set Global Variable    ${SHARED_USER_PASSWORDS}    ${passwords}
    Set Global Variable    ${SHARED_RUN_ID}            ${run_id}

Ensure Shared User Pool Has Index
    [Arguments]    ${target_index}    ${firstname}    ${lastname}    ${phone}    ${password}
    ${current_count}=    Get Length    ${SHARED_USER_EMAILS}
    ${needed_count}=     Evaluate    ${target_index} + 1
    IF    ${current_count} >= ${needed_count}
        RETURN
    END
    ${next_needed}=    Evaluate    ${current_count} + 1
    IF    ${needed_count} != ${next_needed}
        Fail    Shared user creation must follow CSV order. Expected user index ${next_needed - 1}, got ${target_index}.
    END
    ${user_number}=    Evaluate    ${target_index} + 1
    ${email}=    Set Variable    qa_user${user_number}_${SHARED_RUN_ID}@example.com
    ${email}    ${pwd}=    Register New User And Return Credentials    ${firstname}    ${lastname}    ${phone}    ${password}    ${email}
    Append To List    ${SHARED_USER_EMAILS}        ${email}
    Append To List    ${SHARED_USER_PASSWORDS}     ${pwd}
    Logout From Account
    Logout Should Be Successful

Get Current Scenario User Index
    ${index}=    Evaluate    int(re.search(r'(\\d+)$', """${TEST NAME}""").group(1)) - 1    modules=re
    RETURN    ${index}
