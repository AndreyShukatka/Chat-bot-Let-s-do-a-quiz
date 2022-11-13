import random


def get_random_question(quiz_bank):
    question, _ = random.choice(list(quiz_bank.items()))
    return question


def get_answer(question, quiz_bank):
    answer = quiz_bank.get(question)
    simple_answer = answer.partition('.')[0].partition('(')[0]
    return simple_answer
