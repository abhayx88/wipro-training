
*** Settings ***
Resource    ../pages/account_page.resource

*** Keywords ***
Logout User
    Log Operation    [Account] Logging out current user
    Logout From Account

Verify Logout Successful
    Log Operation    [Account] Validating logout success
    Logout Should Be Successful

Verify Session Is Terminated
    Log Operation    [Account] Validating session termination
    Account Access Should Require Login
