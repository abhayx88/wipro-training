
*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Variables  ../variables/config.py

*** Keywords ***
Open Application
    [Arguments]    ${browser}=${BROWSER}
    Create Directory    ${EXECDIR}${/}reports
    Set Screenshot Directory    ${EXECDIR}${/}reports
    ${resolved_browser}=    Resolve Browser Name    ${browser}
    Log Operation    [Browser] Launching tests on ${resolved_browser}
    Open Browser    ${URL}    ${resolved_browser}
    Maximize Browser Window
    Set Selenium Timeout    ${TIMEOUT}
    Register Keyword To Run On Failure    NONE

Close Application
    IF    '${TEST STATUS}' == 'FAIL'
        Run Keyword And Ignore Error    Capture Page Screenshot
        Set Suite Variable    ${SUITE_HAS_FAILURE}    ${True}
    ELSE
        Capture First Pass Screenshot Once
    END
    Close All Browsers

Wait And Click
    [Arguments]    ${locator}
    Wait Until Element Is Visible    ${locator}
    Click Element    ${locator}

Input Text Safe
    [Arguments]    ${locator}    ${text}
    Wait Until Element Is Visible    ${locator}
    Input Text    ${locator}    ${text}

Click With Wait
    [Arguments]    ${locator}
    Wait Until Element Is Visible    ${locator}
    Wait Until Element Is Enabled    ${locator}
    Click Element    ${locator}

Silence Failure Screenshots
    Register Keyword To Run On Failure    NONE

Enable Failure Screenshots
    Register Keyword To Run On Failure    NONE

Log Operation
    [Arguments]    ${message}
    Log    ${message}

Capture First Pass Screenshot Once
    ${already_captured}=    Run Keyword And Return Status    Variable Should Exist    ${SUITE_PASS_SCREENSHOT_PATH}
    IF    not ${already_captured}
        ${path}=    Capture Page Screenshot
        Set Suite Variable    ${SUITE_PASS_SCREENSHOT_PATH}    ${path}
    END

Finalize Suite Screenshot Policy
    IF    '${SUITE STATUS}' == 'FAIL'
        ${has_pass_screenshot}=    Run Keyword And Return Status    Variable Should Exist    ${SUITE_PASS_SCREENSHOT_PATH}
        IF    ${has_pass_screenshot}
            Run Keyword And Ignore Error    Remove File    ${SUITE_PASS_SCREENSHOT_PATH}
        END
    END

Prepare Fresh Reports Directory
    ${reports_dir}=    Set Variable    ${EXECDIR}${/}reports
    Run Keyword And Ignore Error    Remove Directory    ${reports_dir}    recursive=True
    Create Directory    ${reports_dir}

Resolve Browser Name
    [Arguments]    ${browser}
    ${name}=    Evaluate    str("${browser}").strip().lower()
    IF    '${name}' == 'msedge' or '${name}' == 'microsoftedge'
        ${name}=    Set Variable    edge
    END
    ${supported}=    Run Keyword And Return Status    Should Match Regexp    ${name}    ^(chrome|firefox|edge)$
    IF    not ${supported}
        Fail    Unsupported browser '${browser}'. Use chrome, firefox, or edge.
    END
    RETURN    ${name}
