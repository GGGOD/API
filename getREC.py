import pymongo

client = pymongo.MongoClient('localhost',27017)
db = client.recommendation
collection = db.ALS
def getREC(question):
    res = [] 
    tmp = collection.find_one({"APPL_ID":question})['recomlist']
    for idx, ele in enumerate(tmp):
        res.append({'number':idx+1, 'name':ele[0]})
    return res
print(getREC('K120751651'))
