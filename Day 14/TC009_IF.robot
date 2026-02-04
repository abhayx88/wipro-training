*** Test Cases ***
IF Condition Example
    ${age}=  Set Variable    20
    IF    ${age}>=18
        Log    Eligible to vote
    END
    
IF ELSE Example
    ${num}=  Set Variable    5
    IF    ${num}>10
        Log    Greater than 10
    ELSE
        Log    Less than or equal to 10
    END

IF ELSE IF Example
    ${marks}=   Set Variable    75
    IF    ${marks}>=90
        Log    Grade A
    ELSE IF    ${marks}>=75
        Log    Grade B
    ELSE
        Log    Grade C
    END
    
Inline IF Example
    ${status}=   Set Variable    PASS
    IF    '${status}'=='PASS'  Log    Test Passed
        
FOR Loop Basic
    FOR    ${item}   IN    one two three
        Log    Item:${item}
    END

*** Variables ***
@{COLORS}  Red Green Blue

*** Test Cases ***
FOR Loop With List
    FOR    ${color}   IN    @{COLORS}
        Log    Color:${color}
    END

FOR Loop IN RANGE
    FOR   ${i}   IN RANGE  1    6
        Log    Number:${i}
    END

FOR Loop With Step
    FOR    ${i}   IN RANGE  0  10  2
        Log    Value:${i}
    END

FOR Loop Enumerate
    FOR    ${index}  ${value}  IN ENUMERATE    a  b  c
        Log    ${index}=${value}
    END

*** Variables ***
@{USERS}    admin    user
@{PADS}     admin123    user123

*** Test Cases ***
TC011 ZIP
    ${count}=    Get Length    ${USERS}
    FOR    ${i}    IN RANGE    ${count}
        Log    ${USERS}[${i}] / ${PADS}[${i}]
    END

Nested FOR Loop
    FOR    ${i}    IN RANGE    1    4
        FOR    ${j}    IN RANGE    1    3
            Log    i=${i}, j=${j}
        END
    END

FOR Loop With IF
    FOR    ${n}    IN RANGE    1    6
        IF    ${n} == 3
            Log    Found 3
        END
    END

BREAK Example
    FOR    ${i}    IN RANGE    1    10
        IF    ${i} == 5
            BREAK
        END
        Log    ${i}
    END


CONTINUE Example
    FOR    ${i}    IN RANGE    1    6
        IF    ${i} == 3
            CONTINUE
        END
        Log    ${i}
    END

WHILE Loop Example
    ${i}=    Set Variable    1
    WHILE    ${i} <= 5
        Log    Value: ${i}
        ${i}=    Evaluate    ${i} + 1
    END

WHILE Loop With BREAK
    ${i}=    Set Variable    1
    WHILE    True
        IF    ${i} == 4
            BREAK
        END
        Log    ${i}
        ${i}=    Evaluate    ${i} + 1
    END

Try Except Example
    TRY
        Fail    Something went wrong
    EXCEPT
        Log    Error handled
    FINALLY
        Log    Always executed
    END

Run Keyword If Example
    ${status}=    Set Variable    PASS
    Run Keyword If    '${status}' == 'PASS'    Log    Test Passed

Run Keyword Unless Example
    ${status}=    Set Variable    FAIL
    Run Keyword Unless    '${status}' == 'PASS'    Log    Test Failed


