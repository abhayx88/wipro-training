*** Settings ***
Library    RequestsLibrary

*** Variables ***
${baseurl}    http://127.0.0.1:5000

*** Test Cases ***
Verify Get All Users
    Create Session    mysession    ${baseurl}
    ${response}=    GET On Session    mysession    /users
    Status Should Be    200    ${response}
    ${res_json}=    To Json    ${response.content}
    Log    ${res_json}    console=True

Verify Get Single User
    Create Session    mysession    ${baseurl}
    ${response}=    GET On Session    mysession    /users/1
    Status Should Be    200    ${response}
    ${res_json}=    To Json    ${response.content}
    Log    ${res_json}    console=True

Verify Get Single User Not Found
    Create Session    mysession    ${baseurl}
    ${response}=    GET On Session    mysession    /users/99    expected_status=404
    Status Should Be    404    ${response}
    Log    ${response.json()}    console=True

Create New User
    Create Session    mysession    ${baseurl}
    ${body}=    Create Dictionary    name=Shyam
    ${response}=    POST On Session    mysession    /users   json=${body}    expected_status=405
    Status Should Be    405    ${response}

Update User Using PUT
    Create Session    mysession    ${baseurl}
    ${body}=    Create Dictionary    name=Shyam
    ${response}=    PUT On Session    mysession    /users/1    json=${body}    expected_status=405
    Status Should Be    405    ${response}


Update User Using PATCH
    Create Session    mysession    ${baseurl}
    ${body}=    Create Dictionary    name=Ravi
    ${response}=    PATCH On Session    mysession    /users/1    json=${body}    expected_status=405
    Status Should Be    405    ${response}




