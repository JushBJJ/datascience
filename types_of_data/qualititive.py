# Nominal Data
eyepieces = ["9mm", "12.5mm", "25mm"]

print("Nominal Data of Telescope: ")
for eyepiece in eyepieces:
    print(eyepiece)

# Ordinal
rocket_statuses = {
    "First Stage: ": "Go",
    "Second Stage: ": "Anomoly"
}

print("Ordinal Data of Rocket Statuses: ")
for stage in rocket_statuses:
    print(rocket_statuses[stage])