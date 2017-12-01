import jieba
import pandas
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
path = '/ods/analysis/20170907_training/data/'
dic_path = '/ods/analysis/20170907_training/dictionary/'

qat = pandas.read_csv(os.path.join(path, 'QA_Table.tsv'), sep = '\t' )
jieba.load_userdict(os.path.join(dic_path, 'issuance.dict'))

def getQA(question):
    corpus = [' '.join(jieba.cut(question))]
    question = []
    answer   = []
    ret = {}
    for rec in qat.iterrows():
        corpus.append(' '.join(jieba.cut(rec[1]['對應詢問項目'])))
        question.append(rec[1]['對應詢問項目'])
        answer.append(rec[1]['答覆內容(文字)'])
    vectorizer  = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    cs = cosine_similarity(X[0], X[1:])
    question_ary = np.array(question)
    rank = cs.flatten().argsort()[::-1]
    
    answer_ary = []
    for idx in rank[0:20]:
        if cs[0][idx] > 0.2:
            answer_ary.append({'quesiton':question[idx], \
                              'similarity': cs[0][idx], \
                              'answer': answer[idx]})
    return answer_ary