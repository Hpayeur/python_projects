import requests

parameters = {
    "amount": 15,
    "type": "boolean",
    "category": 27,
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

# question_data = [
#     {
#         "category": "History",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "There are 13 months in the Ethiopian Calendar.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
# {
#         "category": "History",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "Brazil used to be an empire",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
# {
#         "category": "Science: Gadgets",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "iRobot's revolutionary floor-cleaning vacuum,the Roomba, was first invented in 2002",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
# {
#         "category": "Science: Gadgets",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The Western Electric Model 500 telephone uses tone dialing to dial phone numbers.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
# {
#         "category": "Animals",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The mountain chicken is a chicken.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
# {
#         "category": "Animals",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "Hyenas are more closely related to cats than to dogs",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
# {
#         "category": "Science & Nature",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "If you dip a dry towel into a tub full of water, water will climb up the towel by a "
#                     "phenomenon called Cartillary Action",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
# {
#         "category": "Science & Nature",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The French Scientists Louis Pasteur and Emile Roux developed "
#                     "the first rabies vaccination in 1885.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
# {
#         "category": "Animals",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "Finnish Lapphund dogs were used for herding reindeer",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
# {
#         "category": "Animals",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The Average Lifespan of a wildcat is only around 5-6years.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
# ]
