import jieba
import pandas
import os, re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
path = '/home/odshadoop/api/data/'
#dic_path = '/ods/analysis/20170907_training/dictionary/'
dic_path = '/ods/analysis/20170907_training/data/智能理賠/'

medical_rpt = pandas.read_csv(os.path.join(path, 'MEDICAL_DOC.csv') )
jieba.load_userdict(os.path.join(dic_path, 'MedTerm_Dict.txt'))

def returnstoplist(path):
    with open(path) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
    stopwordlist = [x.strip() for x in content] 
    return stopwordlist

stopwordlist= returnstoplist('/ods/analysis/20170907_training/data/智能理賠/md_stop.txt')

def getMedical(question):
    corpus = [' '.join([w for w in jieba.cut(question) if re.match('^[\u4e00-\u9fa5]+$', w) and w not in stopwordlist]) ]
    question = []
    answer   = []
    opers   = []
    codes   = []
    ret = {}
    for rpt in medical_rpt.iterrows():
        corpus.append(' '.join([w for w in jieba.cut(str(rpt[1]['CASE_INFO'])) if re.match('^[\u4e00-\u9fa5]+$', w) and w not in stopwordlist]))
        opers.append(rpt[1]['OPER_NAME'])
        codes.append(rpt[1]['OPER_CODE'])
    vectorizer  = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    cs = cosine_similarity(X[0], X[1:])
    rank = cs.flatten().argsort()[::-1]
    
    answer_ary = []
    for idx in rank[0:20]:
        if cs[0][idx] > 0.5:
            answer_ary.append({'codes':codes[idx], \
                              'similarity': cs[0][idx], \
                              'opers': opers[idx]})
    return answer_ary
