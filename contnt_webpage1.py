import pickle
import pandas as pd
import streamlit as st

cosine_sim = pickle.load(open('C:/Users/sures/Downloads/cosine_df.sav', 'rb'))
indices = pickle.load(open('C:/Users/sures/Downloads/indices.sav', 'rb'))
dfnew1 = pickle.load(open('C:/Users/sures/Downloads/dfnew1.sav', 'rb'))

listname=[]

for string in indices.index:
    string=string.strip()
    listname.append(string)

indices.index=listname

def get_recommendations(title):
    # Get the index of the product that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all product with that product
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the product based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 20 most similar product
    sim_scores = sim_scores[1:10]

    # Get the product indices
    product_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar product
    return dfnew1['title'].iloc[product_indices]

st.title('ML Recommender System (Content based)')

search = st.text_input('Search for...')
search1= search.strip()
if(search==''):
    search="IHOP Gift Card Collection"
else:
    flag=0
    for string in dfnew1.title:
        string = string.strip()
        if(search1==string):
            flag=1
    if(flag==0):
        st.error("Match not found")
        search="IHOP Gift Card Collection"

st.write('Your recommendations are ')
st.write(get_recommendations(search))
