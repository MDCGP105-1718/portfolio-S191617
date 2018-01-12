x = 0
y = 0

#get input from the user
total_cost = float(input("Enter the total cost of the house: "))
portion_saved = float(input("The portion of salary to be saved: "))
annual_salary = float(input("Enter your annual salary: "))


portion_deposit = 0.2 * total_cost # deposit = 20% of 
current_savings = 0 #
r = 0.04
monthly_salary = annual_salary / 12
monthly_savings = monthly_salary * portion_saved

number_of_months = 0

# find the number of months needed to save for
while current_savings < portion_deposit:
    current_savings = current_savings + current_savings * r / 12 # add the return from investments
    current_savings = current_savings + monthly_savings # add the savings from the monthly salary
    number_of_months += 1

