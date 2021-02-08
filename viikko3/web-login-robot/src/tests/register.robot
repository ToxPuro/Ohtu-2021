*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page


***Test Cases***
Register With Valid Username And Password
    Reset Application
    Set Username  kalle
    Set Password  kalle123
    Set Password_confirmation  kalle123
    Click Button  Register
    Title Should Be  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Reset Application
    Set Username  et
    Set Password  kalle123
    Set Password_confirmation  kalle123
    Click Button  Register
    Registering Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Reset Application
    Set Username  kalle
    Set Password  ab12
    Set Password_confirmation  ab12
    Click Button  Register
    Registering Should Fail With Message  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation 
    Reset Application
    Set username  kalle
    Set Password  kalle123
    Set Password_confirmation  kalle321
    Click Button  Register
    Registering Should Fail With Message  Password and password confirmation differ

Login After Successful Registration
    Reset Application
    Set Username  kalle
    Set Password  kalle123
    Set Password_confirmation  kalle123
    Click Button  Register
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Reset Application
    Set Username  kalle
    Set Password  kalle123
    Set Password_confirmation  kalle321
    Click Button  Register
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password


***Keywords***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Password_confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Registering Should Fail With Message
    [Arguments]  ${message}
    Title Should Be  Register
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}