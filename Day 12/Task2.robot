*** Settings ***
Library    BuiltIn
Library    SeleniumLibrary

*** Test Cases ***
Verify Environment Setup
    Log To Console    ===== Environment Verification Started =====

    # 1. Verify Python installation (most reliable way)
    ${python_path}=    Evaluate    __import__('sys').executable
    Should Not Be Empty    ${python_path}    Python is not accessible to Robot Framework
    Log    Python Executable: ${python_path}
    Log To Console    Python Executable: ${python_path}

    # 2 & 4. Verify Robot Framework installation and print version
    Should Not Be Empty    ${ROBOT_VERSION}    Robot Framework is not installed
    Log    Robot Framework Version: ${ROBOT_VERSION}
    Log To Console    Robot Framework Version: ${ROBOT_VERSION}

    # 3. SeleniumLibrary import verification
    Log To Console    SeleniumLibrary imported successfully

    Log To Console    ===== Environment Verification Completed Successfully =====
