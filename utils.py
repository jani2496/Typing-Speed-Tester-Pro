import time


def calculate_wpm(text, time_taken):
    words = len(text.split())
    wpm = (words / time_taken) * 60
    return round(wpm, 2)


def calculate_accuracy(original, typed):
    correct_characters = 0

    for i, char in enumerate(typed):
        if i < len(original) and char == original[i]:
            correct_characters += 1

    accuracy = (correct_characters / len(original)) * 100

    return round(accuracy, 2)


def calculate_errors(original, typed):
    errors = 0

    for i, char in enumerate(typed):
        if i < len(original) and char != original[i]:
            errors += 1

    errors += abs(len(original) - len(typed))

    return errors