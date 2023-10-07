def main():
    user_answer = input("Какой ответ на главный вопрос жизни, вселенной и всего такого? ")

    if user_answer.lower() == "42" or user_answer.lower() == "сорок два":
        print("Да")
    else:
        print("Нет")

if __name__ == "__main__":
    main()