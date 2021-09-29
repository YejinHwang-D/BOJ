n = int(input())
cnt = 0 #최종 출력할 카운트

# hahppy
for i in range(n):
    check = True
    temp = []
    word = list(input())
    word_len = len(word)
    
    temp.append(word[0]) #맨 처음 문자 등록
    for j in range(1, word_len):
        if word[j]!=word[j-1]:
            if word[j] not in temp:
                temp.append(word[j])
            else:
                check = False
    if check==True:
        cnt += 1
print(cnt)