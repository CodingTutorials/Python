# Grade Converter
# http://cs.smith.edu/~jorourke/Grading.html
Choice = input("Fraction/Percent [F/P]:")

if Choice == "F":
  Numerator = float(input("Points: "))
  Denominator = float(input("Total: "))
  Score = Numerator/Denominator * 100

if Choice == "P":
  Score = float(input("Percent: "))


if Score >= 97.5:
  print("A+")

elif Score >= 92.5:
  print("A")

elif Score >= 90.0:
  print("A-")

elif Score >= 87.5:
  print("B+")

elif Score >= 82.5:
  print("B")

elif Score >= 80.0:
  print("B-")

elif Score >= 77.5:
  print("C+")

elif Score >= 72.5:
  print("C")

elif Score >= 70.0:
  print("C-")

elif Score >= 67.5:
  print("D+")

elif Score >= 62.5:
  print("D")
  
elif Score >= 60.0:
  print("D-")
  
elif Score < 60.0:
  print("F")
