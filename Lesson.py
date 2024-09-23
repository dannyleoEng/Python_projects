def calculate_finances(monthly_salary: float, tax_rate: float, expenses: str, currency: str):
    yearly_salary: float = monthly_salary * 12
    monthly_tax: float = monthly_salary * (tax_rate/100)
    yearly_tax: float = monthly_tax * 12
 
    expense_list: list = expenses.split(", ")
    total_expenses: float = 0
    for words in expense_list:
        total_expenses += int(input(f"cost of {words}: "))
    
    yearly_expenses: float = total_expenses * 12
    monthly_net_income: float = monthly_salary - monthly_tax
    yearly_net_income: float = yearly_salary - yearly_tax
    yearly_net_savings: float = yearly_net_income - yearly_expenses
    monthly_net_saving: float = monthly_net_income - total_expenses



    print("--------------------------")
    print(f"yearly salary: {yearly_salary:,.2f}")
    print(f"monthly salary: {monthly_salary:,.2f}")
    print(f"monthly tax: {monthly_tax}")
    print(f"Yearly tax: {yearly_tax}")
    print(f"Monthly Expenses: {total_expenses}")
    print(f"monthly_net_income: {monthly_net_income:,.2f}")
    print(f"Yearly net income: {yearly_net_income:,.2f}")
    print(f"Monthly net savings: {monthly_net_saving}")
    print(f"Yearly net savings: #{yearly_net_savings}")
    print("--------------------------------")
    
def main():
    try:
        monthly_salary = int(input("Enter your monthly salary: "))
        tax_rate = int(input("Enter your tax rate (%): "))
        expenses = input("Enter all expense you made: ")
        calculate_finances(monthly_salary, tax_rate, expenses=expenses, currency="#")
    except ValueError:
        print("monthly salary and tax rate can only be a number")

if __name__ == "__main__":
    main()

