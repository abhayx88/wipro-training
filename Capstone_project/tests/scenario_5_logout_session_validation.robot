*** Settings ***
Library    DataDriver    file=${CURDIR}/../testdata/e2e_master_data.csv
Resource   ../keywords/account_keywords.robot
Resource   ../keywords/common_keywords.robot

Test Setup     Open Application
Test Teardown  Close Application
Suite Teardown    Finalize Suite Screenshot Policy
Test Template  Scenario 5 Logout Session Validation

*** Test Cases ***
Logout Session Validation Scenario
    [Tags]    modular    scenario5

*** Keywords ***
Scenario 5 Logout Session Validation
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${phone}    ${password}
    Login User With Shared Registration    ${firstname}    ${lastname}    ${email}    ${phone}    ${password}
    Logout User
    Verify Logout Successful
    Verify Session Is Terminated
