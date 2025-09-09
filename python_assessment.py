import pandas as pd

def get_employees_df():
    return pd.read_csv("https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv")

def get_departments_df():
    dep_df = pd.read_csv("https://gist.githubusercontent.com/kevin336/5ea0e96813aa88871c20d315b5bf445c/raw/d8fcf5c2630ba12dd8802a2cdd5480621b6a0ea6/departments.csv")
    dep_df = dep_df.rename(columns={"DEPARTMENT_ID": "DEPARTMENT_IDENTIFIER"})
    return dep_df

def compare_salary_to_average(df):
    if df['SALARY'] >= df['AVG SALARY']:
        return 'high'
    else:
        return 'low'

def compare_salary_to_average_per_dep(df):
    if df['SALARY'] >= df['DEP AVG SALARY']:
        return 'high'
    else:
        return 'low'

employees = get_employees_df()
departments = get_departments_df()

# Task 1
Task1 = employees[['SALARY']].agg({'SALARY':['mean','median','min', 'max']})
Task1.rename(columns={'SALARY':'AVG SALARY'}, inplace=True)
#print(Task1)
Task1.to_csv('Task1.csv')

# Task 2
df2 = employees.merge(departments, left_on='DEPARTMENT_ID', right_on='DEPARTMENT_IDENTIFIER', how='left')
Task2 = df2[['DEPARTMENT_NAME','SALARY']].groupby('DEPARTMENT_NAME').agg({'SALARY':'mean'})
Task2.rename(columns={'SALARY' : 'DEP AVG SALARY'}, inplace=True)
#print(Task2)
Task2.to_csv('Task2.csv')

# Task 3
df3 = employees
df3['AVG SALARY'] = Task1['AVG SALARY']['mean']
df3['SALARY_CATEGORY']  = df3[['SALARY', 'AVG SALARY']].apply(compare_salary_to_average, axis=1)
Task3 = df3[['EMPLOYEE_ID', 'SALARY', 'AVG SALARY', 'SALARY_CATEGORY']]
#print(Task3)
Task3.to_csv('Task3.csv')

# Task 4
df4 = df2.merge(Task2, left_on='DEPARTMENT_NAME', right_on='DEPARTMENT_NAME', how='left')
df4['SALARY_CATEGORY_AMONG_DEPARTMENT']  = df4[['SALARY', 'DEP AVG SALARY']].apply(compare_salary_to_average_per_dep, axis=1)
Task4 =  df4[['EMPLOYEE_ID', 'SALARY', 'DEP AVG SALARY', 'SALARY_CATEGORY_AMONG_DEPARTMENT']]
#print(Task4)
Task4.to_csv('Task4.csv')

# Task 5
df5 = employees
Task5 = df5[df5['DEPARTMENT_ID'] == 20]
#print(Task5)
Task5.to_csv('Task5.csv')

# Task 6
df6 = Task5
df6['NEW SALARY'] = df6['SALARY'].apply(lambda x: x*1.1)
Task6 = df6[['EMPLOYEE_ID','FIRST_NAME','LAST_NAME', 'DEPARTMENT_ID', 'SALARY', 'NEW SALARY']]
#print(Task6)
Task6.to_csv('Task6.csv')

# Task 7 
df7 = employees
Task7 = len(df7[df7['PHONE_NUMBER'].isna()])
#print(f'Number of entries with empty PHONE_NUMBER: {Task7}')
with open('Task7.txt','w') as task7:
    task7.write(f'Number of entries with empty PHONE_NUMBER: {Task7}')

# Task 8
df8 = employees
df8['Dep Total Salary'] = df8[['SALARY','DEPARTMENT_ID']].groupby('DEPARTMENT_ID').transform(sum)
df8['Percentage Salary'] = 100 * df8['SALARY'] / df8['Dep Total Salary']
for dep_id, dep_df in df8.groupby('DEPARTMENT_ID'):
    print(f'dep id : {dep_id}')
    print(dep_df[['EMPLOYEE_ID','SALARY', 'Dep Total Salary', 'Percentage Salary']])