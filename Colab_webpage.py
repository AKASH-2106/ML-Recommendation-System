import pickle
import pandas as pd
import streamlit as st

#loading the saved model
item_similarity_df = pickle.load(open('C:/Users/sures/Downloads/similarity_df.sav', 'rb'))

def get_similar_products(product_name, user_rating):
  similar_score=item_similarity_df[product_name]*(user_rating-2.5)
  similar_score=similar_score.sort_values(ascending=False)
  return similar_score

# giving a title
st.title('ML Recommender System')

st.write('Enter ratings of the products that you have used')

# getting the input data from the user
product_name1 = st.text_input('Enter the ID of the 1st product')
user_rating1 = st.number_input('Enter rating of the 1st product')
if(product_name1==''):
    product_name1="B00001P4ZH"
else:
    if(product_name1 not in list(item_similarity_df.columns)):
        st.error("Error, invalid product ID given")
        product_name1="B00001P4ZH"

product_name2 = st.text_input('Enter the ID of the 2nd product')
user_rating2 = st.number_input('Enter rating of the 2nd product')
if(product_name2==''):
    product_name2="B00001P4ZH"
else:
    if(product_name2 not in list(item_similarity_df.columns)):
        st.error("Error, invalid product ID given")
        product_name1="B00001P4ZH"
    
product_name3 = st.text_input('Enter the ID of the 3rd product')
user_rating3 = st.number_input('Enter rating of the 3rd product')
if(product_name3==''):
    product_name3="B00001P4ZH"    
else:
    if(product_name3 not in list(item_similarity_df.columns)):
        st.error("Error, invalid product ID given")
        product_name1="B00001P4ZH"
        
product_name4 = st.text_input('Enter the ID of the 4th product')
user_rating4 = st.number_input('Enter rating of the 4th product')
if(product_name4==''):
    product_name4="B00001P4ZH"
else:
    if(product_name4 not in list(item_similarity_df.columns)):
        st.error("Error, invalid product ID given")
        product_name1="B00001P4ZH"
    
product_name5 = st.text_input('Enter the ID of the 5th product')
user_rating5 = st.number_input('Enter rating of the 5th product')
if(product_name5==''):
    product_name5="B00001P4ZH"
else:
    if(product_name5 not in list(item_similarity_df.columns)):
        st.error("Error, invalid product ID given")
        product_name1="B00001P4ZH"
    
# code for Prediction
example=[(product_name1, user_rating1),(product_name2, user_rating2),(product_name3, user_rating3),(product_name4, user_rating4),(product_name5, user_rating5)]
similar_products=pd.DataFrame()
for product, rating in example:
  similar_products=similar_products.append(get_similar_products(product, rating),ignore_index=True)
st.write("Your most recommended products are ")
st.dataframe(similar_products.sum().sort_values(ascending=False).head())