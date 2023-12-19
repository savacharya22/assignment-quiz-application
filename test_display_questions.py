import pytest
from main_menu import display_question

def test_display_question(capsys):
    # Arrange
    question_number = 1
    question = {
        'que': 'What is the capital of Japan?',
        'a': 'Beijing',
        'b': 'Seoul',
        'c': 'Tokyo',
        'd': 'Bangkok',
    }

    # Act
    display_question(question_number, question)

    # Assert
    captured_stdout = capsys.readouterr().out
    expected_output = f"""
{'-'*30}

Question {question_number} ): {question['que']}

\ta. {question['a']}
\tb. {question['b']}
\tc. {question['c']}
\td. {question['d']}

"""
    assert captured_stdout.strip() == expected_output.strip()