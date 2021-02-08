*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  touko  touko123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  et  kalle123
    Output Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  touko  sala12
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password That Contains Only Letters
    Input Credentials  touko  salasana
    Output Should Contain  Password must contain numbers

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
