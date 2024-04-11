### Test cases for 'employees' table
1. (HR_EMP_DUPLICATE) Verify that keys in the table [hr].[employees] are unique
    > Expected result: Execution result show 0 rows
                       (All key values unique). 
2. (HR_EMP_SALARY_RANGE_CHECK) Verify that salary for each employee are
    in range [min_salary; max_salary] which mentioned in table [hr].[jobs].
    > Expected result: Execution result show 0 rows

### Test cases for 'jobs' table
3. (HR_JOB_NULL_VALUES) Check if there are any null values in columns:
     - job_id
     - job_title
     - min_salary
     - max_salary
    > Expected result: Execution result show 0 rows

4. (HR_JOB_SALARY_DELTA) Verify that difference between min and max salary in [hr].[jobs] not more then 20000
    > Expected result: Execution result show 0 rows

#### Test cases for 'jobs' table
5. (HR_DEPART_IN_EACH_EXIST_EMPLOYEE) Verify that each department has employees.
    > Expected result: Execution result show 0 rows

6. (HR_DEPART_COMPLITNES_WITH_LOCATION) Verify that all location id from [hr].[departments] present in dimension [hr].[locations]
    > Expected result: Execution result show 0 rows