from difflib import SequenceMatcher

# Define the two strings

def compare(data1, data2):
    # Create a SequenceMatcher object
    matcher = SequenceMatcher(None, data1, data2)

    # Calculate the similarity ratio
    similarity_ratio = matcher.ratio()

    # Calculate the percentage difference
    percentage_difference = round((1 - similarity_ratio) * 100, 2)
    return percentage_difference

# print(f"Percentage difference between the two strings: {percentage_difference:.2f}%")
