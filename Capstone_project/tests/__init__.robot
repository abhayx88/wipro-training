*** Settings ***
Resource       ../keywords/account_keywords.robot
Resource       ../resources/base.resource
Suite Setup    Global Suite Setup

*** Keywords ***
Global Suite Setup
    Prepare Fresh Reports Directory
    Prepare Shared Users For Full Run
