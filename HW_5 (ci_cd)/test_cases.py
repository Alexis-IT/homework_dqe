from connect import *

# TestCases to table [hr].[employees]


class TestEmployees:
    TABLE = "[hr].[employees]"

    def test_tc1_key_unique_employees(self, db):
        """ TC1 Verify that keys in the table [hr].[employees] are unique """

        print('TC1 Verify that keys in the table [hr].[employees] are unique')
        query = f"SELECT count(*) FROM {self.TABLE} GROUP BY employee_id HAVING count(*) > 1;"
        exp_result = None
        result = db.execute_sql_query(query)
        # logging.getLogger().info('Your log message')
        assert result is exp_result

    def test_tc2_salary_in_range(self, db):
        """ TC2 Verify that keys in the table [hr].[employees] are unique"""

        print('TC2 Verify that keys in the table [hr].[employees] are unique')
        query = (f"SELECT employee_id, employees.job_id, salary, min_salary, max_salary "
                 f"FROM {self.TABLE} LEFT JOIN [hr].[jobs] on jobs.job_id = employees.job_id "
                 f"WHERE salary < min_salary or salary > max_salary;"
                 )
        exp_result = None
        result = db.execute_sql_query(query)
        assert result is exp_result

# # TestCases to table [hr].[jobs]


class TestJobs:
    TABLE = "[hr].[jobs]"

    def test_tc3_nulls_in_jobs(self, db):
        """ TC3 Verify that all columns in [hr].[jobs] do not contain NULL values"""

        print('TC3 Verify that all columns in [hr].[jobs] do not contain NULL values')
        query = (f"SELECT * FROM {self.TABLE} WHERE job_id IS NULL OR job_title IS NULL "
                 f"OR min_salary IS NULL OR max_salary IS NULL;"
                 )
        exp_result = None
        result = db.execute_sql_query(query)
        assert result is exp_result

    def test_tc4_min_max_salary_diff(self, db):
        """ TC4 Verify that difference between min and max salary in [hr].[jobs] not more then 20000"""

        print('TC4 Verify that difference between min and max salary in [hr].[jobs] not more then 20000')
        query = (f"SELECT job_id, job_title, (coalesce(max_salary,0)-coalesce(min_salary,0)) as diff "
                 f"FROM {self.TABLE}; "
                 )
        exp_result = 20000
        result = db.execute_sql_query(query)
        assert float(result[2]) <= exp_result


# TestCases to table [hr].[departments]


class TestDepartments:
    TABLE = "[hr].[departments]"

    def test_tc5_department_vs_employee(self, db):
        """ TC5 Check that each department has employee in [hr].[departments]"""

        print('TC5 Check that each department has employee in [hr].[departments]')
        query = (f"SELECT d.department_id, d.department_name FROM {self.TABLE} as d "
                 f"LEFT JOIN [hr].[employees] as e ON d.department_id=e.department_id "
                 f"WHERE e.department_id is null "
                 f"ORDER BY d.department_id"
                 )
        exp_result = None
        result = db.execute_sql_query(query)
        assert result is exp_result

    def test_tc6_department_vs_location(self, db):
        """ TC6 Check that all location id from dim [hr].[departments] present in location dimension"""

        print('TC6 Check that all location id from dim [hr].[departments] present in location dimension')
        query = (f"SELECT distinct d.location_id FROM {self.TABLE} as d "
                 f"LEFT JOIN [hr].[locations] as l ON d.location_id=l.location_id "
                 f"WHERE l.location_id is null"
                 )
        exp_result = None
        result = db.execute_sql_query(query)
        assert result is exp_result
