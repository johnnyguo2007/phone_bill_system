minutesIncluded = 300

costMonthlyPlan = 29.95

costPerMinute = 0.45

taxes = 12.5

minutesUsed = int(input("How many minutes did you use this month?: "))

if minutesUsed < minutesIncluded:
    taxes = costMonthlyPlan * 12.5 / 100
    monthlyBill = costMonthlyPlan + taxes

else:
    difference = minutesUsed - minutesIncluded
    extraCost = difference * costPerMinute
    taxes = (costMonthlyPlan + extraCost) * 12.5 / 100
    monthlyBill = costMonthlyPlan + extraCost + taxes

print("Your monthly bill is: ", monthlyBill)
