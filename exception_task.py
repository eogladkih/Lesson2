
answers = {
    "привет": "Привет!",
    "как дела": "Отлично, а у тебя?",
    "пока": "Еще увидимся!"
}



def get_answer(question, answers):
    return answers.get(question)
    

def ask_user(answers):
    try:
        while True:
            question = input('Скажи что-нибудь: \n')
            answer = get_answer(question, answers)    
            print(answer)
            if question == 'Пока':
                break
    except KeyboardInterrupt:
        print("Пока!")
        


ask_user(answers)