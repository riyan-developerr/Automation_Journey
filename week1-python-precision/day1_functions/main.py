from utils import(greet,Price_af_discount,profile,repeat_action,summarize)

print(greet("Riyan"))
print(greet("Riyan", greeting="Assalam o Alaikum"))

print(Price_af_discount(5000, 20))
print(Price_af_discount(5000, 150))  # should return invalid message

print(summarize([10, 20, 30, 40, 50]))
print(summarize([]))

print(profile("Riyan", 19, city="Faisalabad", degree="BS AI"))

print(repeat_action(greet, 3, "Riyan"))