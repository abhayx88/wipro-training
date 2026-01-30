*** Settings ***
Library    BuiltIn

*** Variables ***
${NAME}        Abhay
${COURSE}      Robot Framework
@{SKILLS}      Python    Selenium    Robot

*** Test Cases ***
Log Scalar Variables
    Log    User name is ${NAME}
    Log To Console    Learning ${COURSE}

Log List Variables
    Log    User skills are: ${SKILLS}
    Log To Console    First skill is ${SKILLS}[0]
