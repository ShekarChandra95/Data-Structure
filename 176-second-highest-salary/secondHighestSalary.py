import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Drop the duplicate and get unique salaries in the DF
    unique_salary = employee['salary'].drop_duplicates()

    # Sort salaries in Descending Order and get the 2nd highest salary
    sec_highest = unique_salary.nlargest(2).iloc[-1] if len(unique_salary) >=2 else None

    # If the DF has less than 2 salaries return the value as None
    if sec_highest is None:
        return pd.DataFrame({'SecondHighestSalary':[None]})

    # Return the result as 2nd Highest salary
    result_DF = pd.DataFrame({'SecondHighestSalary': [sec_highest]})

    return result_DF
