def main():
    question = 'What is the capital of California?'
    answer = 'Sacramento'

    question = 'What is the capital of Nevada?'
    answer = 'Carson City'



    if correct_answer:
        print('You got the answer correct.')
    else:
        print('You did not get the answer correct.')

    user_answer = input('')


def quiz_question(question, answer):
    # ask one question, check the answer
    # call this function many times

    user_answer = input(question + ':')

    if user_answer == answer:  # TODO ignore case?
        print('Correct')
    else:
        print('Sorry the answer is ' + answer)


main()


def check_answer(user_answer):
    # Return True if user answer is correct. Return false if user answer is incorrect
    if user_answer == 'Sacramento':
        print('Your answer is correct.')
        return True
    else:
        if user_answer != 'Sacramento':
            print('Your answer is wrong. The correct answer is Sacramento.')
    return False