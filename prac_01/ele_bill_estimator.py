TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = float(input("Enter tariff: "))
if tariff != 11 or tariff != 31:
    print("Invaid Input")
    tariff = float(input("Enter tariff: "))
kWh_daily_use = float(input("Enter daily use in kWh: "))
billing_period = float(input("Enter number of billing days: "))

if tariff == 11:
    bill_estimate = TARIFF_11 * kWh_daily_use * billing_period
else:
    bill_estimate = TARIFF_31 * kWh_daily_use * billing_period

print("Estimated bill: ${:.2f}".format(bill_estimate))