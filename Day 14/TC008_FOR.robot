*** Test Cases ***
Print Names using for loop
    FOR    ${name}    IN    Ram    Ravi    Taj
        Log To Console    ${name}
    END

Print Numbers using while loop
    ${count}=    Set Variable    1
    WHILE    ${count} <= 5
        Log To Console    ${count}
        ${count}=    Evaluate    ${count} + 1
    END
