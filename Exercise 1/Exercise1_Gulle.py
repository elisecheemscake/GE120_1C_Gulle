"""
GE 120: A cool programming subject
The first time I've ever tried to code!
"""

# Converting DMS to DD

print("----- DMS to DD -----")
dms = "267-58-99.99" #input your dms value here!
print("DMS value:", dms)
values = dms.split("-")

degrees = int(values[0])
minutes = int(values[1])
seconds = float(values[2])

dd = degrees + (minutes/60) + (seconds/3600)
print("DD value:", round(dd,6))

# Converting DD to DMS

print("----- DD to DMS -----")
DD = "359.98298347"
print("DD value:",DD)

DEGREES = int(float(DD))
print("*degrees:", DEGREES)

MINUTES = (((float(DD))-DEGREES)*60)
print("*minutes:", MINUTES)

MINUTES_INT = int(((float(DD))-DEGREES)*60)
print("*minutes_int:",MINUTES_INT)

SECONDS = float((MINUTES_INT - MINUTES)*60)
print("*seconds:",round(SECONDS,2))
print("DMS value:",DEGREES, MINUTES_INT, round(SECONDS,2))