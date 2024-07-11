import pickle

with open('vector_class.pkl', 'rb') as f:
    vector_class = pickle.load(f)
with open('model_xgboost_class.pkl', 'rb') as f:
    model_xgboost_class = pickle.load(f)
with open('vector_seniority.pkl', 'rb') as f:
    vector_seniority = pickle.load(f)
with open('model_xgboost_seniority.pkl', 'rb') as f:
    model_xgboost_seniority = pickle.load(f)