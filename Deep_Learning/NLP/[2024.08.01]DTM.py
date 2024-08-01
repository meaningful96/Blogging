def update_bow_length(bow, vocab_length):
    """Ensure the BoW vector has the correct length."""
    if len(bow) < vocab_length:
        bow += [0] * (vocab_length - len(bow))
    return bow

def DTM(document, vocab=None, dtm=None):
    # 띄어쓰기 기준 토큰화
    doc_tokenized = document.split(' ')
    
    # 기존 단어 집합과 DTM이 없는 경우 새로 생성
    if vocab is None:
        vocab = {}
    if dtm is None:
        dtm = []
        
    # 단어별 인덱스에 단어의 출현빈도를 저장할 BoW 벡터
    bow = [0] * len(vocab)
    
    for word in doc_tokenized:
        # 처음 출현한 단어인 경우(=단어 집합에 미존재)
        if word not in vocab:
            # 단어가 등장한 순서를 정수 인덱스로 부여
            vocab[word] = len(vocab)
            # BoW 벡터를 확장하여 새로운 단어에 대한 공간 추가
            bow.append(1)
        # 출현 이력이 있는 단어의 경우
        else:
            # 해당 단어의 인덱스 찾기
            word_index = vocab.get(word)
            # 등장 횟수 1 증가
            bow[word_index] += 1
    
    # 새로운 단어가 추가된 경우 모든 이전 BoW 벡터의 길이 맞추기
    vocab_length = len(vocab)
    for i in range(len(dtm)):
        dtm[i] = update_bow_length(dtm[i], vocab_length)
    
    # 현재 BoW 벡터의 길이 맞추기
    bow = update_bow_length(bow, vocab_length)
    
    return vocab, bow, dtm

docs = ["The cat chased the mouse under the table",
       "The mouse found a piece of cheese", 
        "The dog barked at the cat loudly"]

# 전체 문서에 대해 단어 집합과 BoW 벡터 초기화
vocab = {}
dtm = []

for doc in docs:
    vocab, bow, dtm = DTM(doc, vocab, dtm)
    dtm.append(bow)

# DTM 출력
print("단어 집합:", vocab)
print("DTM:")
for i, bow in enumerate(dtm):
    print(f"문서 {i+1}: {bow}")
