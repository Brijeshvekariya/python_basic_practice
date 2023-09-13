
quiz = {
    1:{
        'que' : 'Who is the Prime Minister Of India',
        'ans' : 'Narendra modi'
    },
    2:{
        'que' : 'Most Popular Programing Language',
        'ans' : 'Python'
    },
    3:{
        'que' : 'Most Popular Cricketer of World',
        'ans' : 'Mahendra sinh dhoni'
    }
}
# print(quiz)
score = 0
for i in range(1,len(quiz)+1):
    print(f"({i}) Que. {quiz[i]['que']}")
    ans = input("Enter your Answer : ").title()
    if ans == quiz[i]['ans']:
        print('Correct Answer .')
        score += 50
    else:
        print('Wrong Answer.')
        score -= 20
    input()
print("Your Score is : ",score)