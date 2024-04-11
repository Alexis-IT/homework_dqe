*** Settings ***
Library           ../Resources/CustomFunctions.py
Library           OperatingSystem
Library           DatabaseLibrary
Resource          ../Resources/tests.robot
Resource          ../Resources/credentials.robot

Suite Setup       Create Connection And Set As Variable

*** Keywords ***
Create Connection And Set As Variable
    ${cursor}=    Connect To Database Full Way    ${DBHost}    ${DBName}    ${DBUser}    ${DBPass}    ${DBDriver}
    Set Global Variable    ${cursor}

*** Test Cases ***
No key duplicates in [hr].[employees]
    [Tags]  Uniqueness; Employees
    [Documentation]
    ...   *Description:*
    ...        Verify that keys in the table [hr].[employees] are unique
    [Setup]
        ${result}=   Execute SQL Query   ${cursor}   ${HR_EMP_DUPLICATE}
        Should Be Empty   ${result}

Check salary range [hr].[employees]
    [Tags]  Salary  Validity
    [Documentation]
    ...   *Description:*
    ...       Verify that salary for each emploees are in range [min_salary; max_salary]
    ...       which mentioned in table [hr].[jobs].
    [Setup]
        ${result}=   Execute SQL Query   ${cursor}    ${HR_EMP_SALARY_RANGE_CHECK}
        Should Be Empty   ${result}

Check NULL values in all columns in [hr].[jobs]
    [Tags]  Compleatnes   NULL values   Jobs
    [Documentation]
    ...   *Description:*
    ...       Verify that all columns in [hr].[jobs] do not contain NULL values.
    [Setup]
        ${result}=   Execute SQL Query   ${cursor}    ${HR_JOB_NULL_VALUES}
        Should Be Empty   ${result}

Check difference between min and max salary in [hr].[jobs]
    [Tags]  Validity checks   Jobs   Salary
    [Documentation]
    ...   *Description:*
    ...       Verify that difference between min and max salary in [hr].[jobs] not more then 20000.
    [Setup]
        ${result}=   Execute SQL Query   ${cursor}    ${HR_JOB_SALARY_DELTA}
        Should Be Empty   ${result}

Check that each depatrment has emploee in [hr].[departments]
    [Tags]  Completeness checks   Departments
    [Documentation]
    ...   *Description:*
    ...       Verify that each depatrment has emploee.
    [Setup]
        ${result}=   Execute SQL Query   ${cursor}    ${HR_DEPART_IN_EACH_EXIST_EMPLOYEE}
        Should Be Empty   ${result}

Check that all location id from dim [hr].[departments] present in location dimension
    [Tags]  Completeness checks   Departments   Location
    [Documentation]
    ...   *Description:*
    ...      Verify that all location id from [hr].[departments] present in [hr].[locations].
    [Setup]
        ${result}=   Execute SQL Query   ${cursor}    ${HR_DEPART_COMPLITNES_WITH_LOCATION}
        Should Be Empty   ${result}