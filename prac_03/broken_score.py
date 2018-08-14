"""
Program to determine grade from score
"""


def main():
    score = float(input("Enter score: "))
    print(check_score(score))


def check_score(score):
    if score < 0 or score > 100:
        str_output = "Invalid score"
    elif score >= 90:
        str_output = "Excellent"
    elif score >= 50:
        str_output = "Pass"
    else:
        str_output = "Fail"
    return str_output


main()
