"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.

b. Can you fix it so that it prints the list of (10) scores per subject with the maximum per subject?

c. When you've done that, also print the minimum and average for each subject.

d. Then print the results in a nicely-formatted table.
"""


# Read and display student scores from scores file.
def main():
    raw_data = load_data_from_file()
    subjects = raw_data[0].strip().split(",")
    score_values = read_scores_from_data(raw_data)
    #sort score values
    print(score_values)


def read_scores_from_data(scores_data):
    score_values = []
    for line in scores_data[1:]:
        score_values += [line.strip().split(",")]
    return score_values


def load_data_from_file():
    file = open("scores.csv")
    data = file.readlines()
    file.close()
    return data


main()
