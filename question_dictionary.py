import json
import os
import argparse

def input_parsing_command_line():
    parser = argparse.ArgumentParser(
        description='Программа переводит txt файлы в json'
    )
    parser.add_argument(
        '--folder',
        help='укажите папку с которой брать файлы для перевода',
        default='questions',
        type=str
    )
    parser.add_argument(
        '--path',
        help='укажите путь json файла в формате:"*.json"',
        default='questions_bank.json',
        type=str
    )
    args = parser.parse_args()
    return args

def get_question_and_answer(quiz_question):
    quiz_question = quiz_question.split('\n\n')
    beautiful_question, answer = '', ''
    for question_section in quiz_question:
        if question_section.startswith('Вопрос'):
            question = question_section.partition('\n')[2]
            beautiful_question = question.replace('\n', ' ')
        if question_section.startswith('Ответ:'):
            answer = question_section.partition('\n')[2]
    return beautiful_question, answer


def get_quiz_bank(folder):
    files = os.listdir(folder)
    quiz_bank = {}
    for file in files:
        with open(os.path.join(folder, file), 'r', encoding='KOI8-R') as file:
            file_contents = file.read()
            quiz_questions = file_contents.split('\n\n\n')
            for quiz_question in quiz_questions:
                question, answer = get_question_and_answer(quiz_question)
                quiz_bank[question] = answer
    return quiz_bank


def save_quiz_bank(quiz_bank, path):
    quiz_bank = json.dumps(quiz_bank, ensure_ascii=False)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(quiz_bank)


def main():
    args = input_parsing_command_line()
    folder = args.folder
    path = args.path
    quiz_bank = get_quiz_bank(folder)
    save_quiz_bank(quiz_bank, path)


if __name__ == '__main__':
    main()