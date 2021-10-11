import pickle

# ¸ü¤JModel
with open('./model/xgboost-iris.pickle', 'rb') as f:
    xgboostModel = pickle.load(f)

def predict(input):
    pred=xgboostModel.predict(input)[0]
    print(pred)
    return pred