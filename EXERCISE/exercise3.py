#KBC GAME CODE:-
kbc =[
    {
        "question" : "what is my name?",
        "option" : ["a> rishi", "b> akiii","c> ankit","d> rishideo"],
        "answer" : "c"
    },
    {
        "question" : "what is my insta id?",
        "option" : ["a> rishi", "b> akiii","c> akiiiyarrrr","d> rishideo"],
        "answer" : "c"
    },
    {
        "question" : "what is your name?",
        "option" : ["a> rishi", "b> akiii","c> ankit","d> rishideo"],
        "answer" : "d"
    },
    {
        "question" : "what is your id?",
        "option" : ["a> rishi", "b> akiii","c> ankit","d> rishideo"],
        "answer" : "d"
    },
    {
        "question" : "what is your stream?",
        "option" : ["a> it", "b> ds","c> aiml","d> cse"],
        "answer" : "b"
    },
    {
        "question" : "what is your dream?",
        "option" : ["a> gen ai dev", "b> video editor","c> data scientist","d> data analyst"],
        "answer" : "c"
    },
]
amount = [1000,5000,10000,25000,50000,100000]
total_amount = 0
def play_kbc():
    global total_amount
    for i in range(len(kbc)):
        print(f"question {i+1}:{kbc[i]["question"]}")
        for option in kbc[i]["option"]:
            print(option)
        user_answer = input("enter your answer(a/b/c/d):").lower()
        if user_answer == kbc[i]["answer"]:
            print(f"correct! you have own {amount[i]}\n")
            total_amount += amount[i]
        else:
            print("wrong answer! better luck. game over.\n")
            break
    print(f"congratualtion! you are taking home :{total_amount}")
if __name__ == "__main__":
    play_kbc() 