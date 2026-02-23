*** Settings ***
Resource   ../resources/base.resource
Resource   ../keywords/account_keywords.robot
Resource   ../keywords/common_keywords.robot

Test Setup     Open Application
Test Teardown  Close Application
Suite Teardown    Finalize Suite Screenshot Policy

*** Test Cases ***
Customer Role Validation
    [Tags]    roles    customer
    Login User With Fresh Registration
    Logout User
    Verify Logout Successful
    Verify Session Is Terminated
