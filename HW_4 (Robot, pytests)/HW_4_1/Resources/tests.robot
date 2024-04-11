*** Settings ***
Documentation   Robot variables for all tests

*** Variables ***
${HR_EMP_DUPLICATE}            SELECT employee_id, count(*)
                                 ...  FROM [hr].[employees]
                                 ...  GROUP BY employee_id HAVING count(*) > 1;

${HR_EMP_SALARY_RANGE_CHECK}   SELECT employee_id, employees.job_id, salary, min_salary, max_salary
                               ...  FROM [hr].[employees]
                               ...  LEFT JOIN [hr].[jobs] on jobs.job_id = employees.job_id
                               ...  WHERE salary < min_salary or salary > max_salary

${HR_JOB_NULL_VALUES}            SELECT *
                               ...  FROM [hr].[jobs]
                               ...  WHERE job_id IS NULL OR job_title IS NULL
                               ...       OR min_salary IS NULL OR max_salary IS NULL

${HR_JOB_SALARY_DELTA}         SELECT job_id, job_title, (coalesce(max_salary,0)-coalesce(min_salary,0)) as diff
                               ...  FROM [hr].[jobs]
                               ...  WHERE (coalesce(max_salary,0)-coalesce(min_salary,0))>20000


${HR_DEPART_IN_EACH_EXIST_EMPLOYEE}   SELECT d.department_id, d.department_name
                                      ...  FROM [hr].[departments] as d
                                      ...  LEFT JOIN [hr].[employees] as e ON d.department_id=e.department_id
                                      ...  WHERE e.department_id is null
                                      ...  ORDER BY d.department_id

${HR_DEPART_COMPLITNES_WITH_LOCATION}  SELECT distinct d.location_id
                                       ...  FROM [hr].[departments] as d
                                       ...  LEFT JOIN [hr].[locations] as l ON d.location_id=l.location_id
                                       ...  WHERE l.location_id is null
