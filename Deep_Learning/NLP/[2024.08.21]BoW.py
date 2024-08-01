def bag_of_words(document):
    # 띄어쓰기 기준 토큰화
    doc_tokenized = document.split(' ')
    
    # 단어별 고유의 정수 인덱스를 할당할 단어 집합(Vocabulary)
    vocab = {}
    # 단어별 인덱스에 단어의 출현빈도를 저장할 BoW 벡터
    bow = []
    
    for word in doc_tokenized:
        # 처음 출현한 단어인 경우(=단어 집합에 미존재)
        if word not in vocab.keys():
            # 단어가 등장한 순서를 정수 인덱스로 부여
            vocab[word] = len(vocab)
            # 처음 등장한 단어이므로 BoW에 1 부여
            bow.append(1)
            
        # 출현 이력이 있는 단어의 경우
        else:
            # 해당 단어의 인덱스 찾기
            word_index = vocab.get(word)
            # 등장 횟수 1 증가
            bow[word_index]+=1
            
    return vocab, bow

docs = ["오렌지 먹은지 얼마나 오렌지",
       "바나나 먹으면 나한테 바나나"]

for doc in docs:
    vocab, bow = bag_of_words(doc)
    print(f"- 문서: {doc}")
    print(f"- 단어 집합: {vocab}")
    print(f"- BoW 벡터: {bow}")
    print("===================")
