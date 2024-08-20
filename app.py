import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
import nltk

# Define the download directory explicitly
nltk_data_dir = r'C:\Users\Testbook\Downloads\spam detection\nltk_data'
nltk.data.path.append(nltk_data_dir)

# Download 'punkt' to the specified directory
nltk.download('punkt', download_dir=nltk_data_dir)


nltk.download('stopwords')
nltk.data.path.append(r'C:\Users\Testbook\Downloads\spam detection\nltk_data')

# Download the 'punkt' data


ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    text = [word for word in text if word.isalnum()]

    text = [word for word in text if word not in stopwords.words('english') and word not in string.punctuation]

    text = [ps.stem(word) for word in text]
    return " ".join(text)

st.title("Email Spam Classifier")
input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    transformed_sms = transform_text(input_sms)

    vector_input = tfidf.transform([transformed_sms])

    result = model.predict(vector_input)[0]

    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
