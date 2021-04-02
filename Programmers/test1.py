def solution(new_id):

    answer = ''

    #1단계
    new_id=new_id.lower()

    #2단계
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c


    #3단계
    while '..' in answer:
        answer=answer.replace('..','.')

    #4단계
    if answer[0] == '.' or answer[-1] == '.':
        if answer[0]=='.':
            answer=list(answer)
            answer[0]=''
        if answer[-1]=='.':
            answer=list(answer)
            answer[-1]=''
        answer="".join(answer)

    #5단계
    if answer=='':
        answer='a'


    #6단계
    if len(answer)>=16:
        new_id=""
        for i in range(15):
            new_id+=answer[i]
        if new_id[-1]=='.':
            new_id = list(new_id)
            new_id[-1] = ''
        answer=new_id
        answer = "".join(answer)

    #7단계
    while len(answer)<=2:
        answer+=answer[-1]


    return answer