answers = {
    "hello":"Hi!",
    "hi": "Hi!",
    "how are you":"Fine,as you?",
    "how are u":"Fine,as you?",
    "good":"I'm glad to hear it!",
    "nice":"I'm glad to hear it!",
    "fine":"I'm glad to hear it!",
    "cool":"I'm glad to hear it!",
    "bad":"Oh, don't be sad!",
    "exit":"Bye!"
}


def get_answers(question, answers):
    return answers.get(question)


def ask_users(answers):
    try:
        while True:
            user_input = input("Say something:").lower()
            user_input = user_input.replace('?','').replace('!','')
            answers = get_answers(user_input, answers)
            if (answers == None):
                print("Ask another question")
            elif (user_input == "exit"): 
                break
            else:
                print(answers)
    except KeyboardInterrupt:
        print("I'll see you around!")
    except AttributeError:
        print("Ask another question")
        


ask_users(answers)
