total_cost = int(input("Enter the Total cost of your  Dream house"))
portion_down_payment = 0.25 * total_cost
current_savings = 0 
annual_salary = int(input("Enter Your Annual Salaly"))
portion_saved =  annual_salary/12 * 0.1

r = 0.04
number_of_months = 0
while current_savings >= 0 :
    current_savings = current_savings*r/12 + portion_saved + current_savings
    number_of_months += 1
    if current_savings >= portion_down_payment:  
        break
print(f"Number of months needed {number_of_months}")
