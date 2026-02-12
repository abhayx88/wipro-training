*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE}    http://127.0.0.1:5000/api

*** Test Cases ***
Get Restaurants
    Create Session    foodie    ${BASE}
    ${response}=    GET On Session    foodie    /restaurants
    Status Should Be    200    ${response}
