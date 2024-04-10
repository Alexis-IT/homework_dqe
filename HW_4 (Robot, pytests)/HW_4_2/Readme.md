## Project pytest with automated test cases from 'TNR' database

### Requirements: 
1. Python 3.11
2. PyTest: pip install pytest
3. PyTest html reporting: pip install pytest-html
4. pyodbc: pip install pyodbc
5. TRN database


### Project:
1. Go to `HW_4_2` directory in a terminal
2. Update credentials `HW_4_2/credentials.py` if needed
3. Run test suite with the following command:
>  pytest test_cases.py
4. Generate report with command :
> pytest --html=report.html 

Report will be available in 'report.html' file

### Test description

#### Test cases for 'employees' table
1. Verify that keys in the table [hr].[employees] are unique
    > Expected result: Execution result show 0 rows
                       (All key values unique). 
2. Verify that salary for each employee are
    in range [min_salary; max_salary] which mentioned in table [hr].[jobs].
    > Expected result: Execution result show 0 rows

#### Test cases for 'jobs' table
3.Check if there are any null values in columns:
     - job_id
     - job_title
     - min_salary
     - max_salary
    > Expected result: Execution result show 0 rows

4. Verify that difference between min and max salary in [hr].[jobs] not more than 20000
    > Expected result: Execution result show 0 rows

#### Test cases for 'jobs' table
5. Verify that each department has employees.
    > Expected result: Execution result show 0 rows

6. Verify that all location id from [hr].[departments] present in dimension [hr].[locations]
    > Expected result: Execution result show 0 rows