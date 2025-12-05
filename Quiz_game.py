print("Welcome to a finance Quiz Game hosted by Solker!")

playing = input("Do you want to play this game? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
answer = input("What is WACC in full? ")
if answer.lower() == "weighted average cost of capital":
    print("Correct!")
    score += 2
else:
    print("Incorrect! The correct answer is Weighted Average Cost of Capital.")

answer = input("What is DCF in full? ")
if answer.lower() == "discounted cash flow":
    print("Correct!")
    score += 2
else:
    print("Incorrect! The correct answer is Discounted Cash Flow.")

answer = input("What does EBITDA stand for? ")
if answer.lower() == "earnings before interest, taxes, depreciation and amortization":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Earnings Before Interest, Taxes, Depreciation and Amortization.")

answer = input("What is the formula for NPV? ")
if answer.lower() == "npv = ∑ (cash inflow / (1 + r)^t) - initial investment":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is NPV = ∑ (cash inflow / (1 + r)^t) - initial investment.")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")
