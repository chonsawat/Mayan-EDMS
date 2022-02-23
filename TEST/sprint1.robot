*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${STUFF_ID}     staff
${STUFF_PASS}   pizzahud1150

*** Test Case ***
Open Login
    Open Browser    http://localhost/   edge

Login as Stuff
    Login as Stuff Username
    Location Should Be  http://localhost/#/home/
    [Teardown]  Close Browser


Login as Fail
    Open Browser    http://localhost/   edge
    Wait Until Element Is Visible  id:id_username
    Input Text  id:id_username      fail
    Input Text  id:id_password      fail
    Click Button    class:btn-primary
    Location Should Be      http://localhost/authentication/login/
    Element Text Should Be    xpath://div[@class="alert alert-danger"]  Please enter a correct Username and password. Note that both fields may be case-sensitive.
    [Teardown]  Close Browser


Click Document
    Open Browser    http://localhost/   edge
    Login as Stuff Username
    Wait Until Element Is Visible  xpath://a[@aria-controls="collapse-documents"]
    Double Click Element    xpath://a[@aria-controls="collapse-documents"]
    Wait Until Element Is Visible    xpath://a[@href="/documents/documents/"]
    Double Click Element    xpath://a[@href="/documents/documents/"]
    Element Should Be Visible   content-title
    [Teardown]  Close Browser

All Document Page
    Open Browser    http://localhost/#/documents/documents/   edge
    Login as Stuff Username
    Wait Until Element Is Visible  content-title
    Element Text Should Be  content-title   All documents
    [Teardown]  Close Browser


# All Document Page Complete Tag
#     Open Browser    http://localhost/#/tags/documents/2/tags/   edge
#     Login as Stuff Username
#     Wait Until Element Is Visible  class:label-tag
#     Element Text Should Be  class:label-tag   เอกสารครบ
#     [Teardown]  Close Browser


# All Document Page Inomplete Tag
#     Open Browser    http://localhost/#/tags/documents/1/tags/   edge
#     Login as Stuff Username
#     Wait Until Element Is Visible  class:label-tag
#     Element Text Should Be  class:label-tag   เอกสารไม่ครบ
#     [Teardown]  Close Browser


*** Keywords ***
Login as Stuff Username
    Wait Until Element Is Visible  id:id_username
    Input Text  id_username     ${STUFF_ID}
    Input Text  id_password     ${STUFF_PASS}
    Click Button    class:btn-primary