
import json
from score import save_score


def test_save_score():

    name = "John Doe"
    score = 10

    # Set up a temporary file to store scores
    scores_file = "tests/test.json"
    with open(scores_file, "w") as test_file:
        json.dump([{'name': name, 'score': score}], test_file)

    # Define some sample data

    # Call the function to save the score
    save_score(name, score)

    # Read the content of the file
    with open(scores_file, 'r') as f:
        saved_scores = json.load(f)

    # Check if the score is correctly saved

    assert saved_scores[0]['name'] == name
    assert saved_scores[0]['score'] == score
