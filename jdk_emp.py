#develop a python application to calculate an employee's gross salary 
#by considering basic salary as 50000.,HRA(20%) and DA(10%). push the 
#code to GitHub. create a jenkins Freestyle project to pull the codeand execute the python program . verify the execution through the jenkins console output.

# salary_calculator.py

def calculate_salary():
    basic_salary = 50000
    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    gross_salary = basic_salary + hra + da

    print("--- Employee Salary Details ---")
    print(f"Basic Salary : Rs {basic_salary}")
    print(f"HRA (20%)    : Rs {hra}")
    print(f"DA (10%)     : Rs {da}")
    print(f"Gross Salary : Rs {gross_salary}")

if __name__ == "__main__":
    calculate_salary()