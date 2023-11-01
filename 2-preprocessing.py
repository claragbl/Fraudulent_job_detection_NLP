import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

path = 'Data/Fake_Real_Job_Posting.csv'
data_full = pd.read_csv(path)

data_reduced = data_full[data_full['requirements'] != "Not Mentioned"]

class PreprocessingClass:
    def remove_URL(self, text):
        url_pattern = r'#URL_[a-f0-9]+#'
        return re.sub(url_pattern, '', text)

    def preprocessing(self, text):
        lemmatizer = WordNetLemmatizer()
        stop_words = set(stopwords.words('english'))

        # URLs removal
        cleaned_text = self.remove_URL(text)
        # Tokenization
        tokens = word_tokenize(cleaned_text)
        # Lowercasing + remove non number and letter character (ponctuation removal)
        words = [word.lower() for word in tokens if word.isalnum()]
        # Stopwords removal
        words = [word for word in words if word not in stop_words]
        # Lemmatization
        words = [lemmatizer.lemmatize(word) for word in words]

        return ' '.join(words)

# instantiate the class
preprocessor = PreprocessingClass()

# apply the preprocessing function to the "requirements" field
data_reduced['requirements'] = data_reduced['requirements'].astype(str).apply(preprocessor.preprocessing)

