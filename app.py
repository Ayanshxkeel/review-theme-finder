"""Group short reviews into themes with TF-IDF and K-means."""
import pandas as pd
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

@st.cache_data
def example_data():
    return pd.read_csv('sample_reviews.csv')

def group_reviews(reviews, groups):
    model = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), max_features=2000)
    matrix = model.fit_transform(reviews)
    clusters = KMeans(n_clusters=groups, random_state=42, n_init=10).fit(matrix)
    words = model.get_feature_names_out()
    themes = {}
    for group in range(groups):
        top = clusters.cluster_centers_[group].argsort()[-5:][::-1]
        themes[group] = ', '.join(words[top])
    return clusters.labels_, themes

st.set_page_config(page_title='Review Theme Finder', page_icon='💬', layout='wide')
st.title('Review Theme Finder')
st.caption('Upload reviews and discover recurring topics with simple text clustering.')
upload = st.file_uploader('Upload a CSV of reviews', type='csv')
try:
    data = pd.read_csv(upload) if upload else example_data()
    column = st.selectbox('Which column contains reviews?', data.columns, index=list(data.columns).index('review') if 'review' in data else 0)
    clean = data[column].dropna().astype(str).str.strip()
    clean = clean[clean.str.len() >= 10].reset_index(drop=True)
    st.write(f'{len(clean)} usable reviews')
    if len(clean) >= 4:
        count = st.slider('Number of themes', 2, min(8, len(clean) - 1), min(3, len(clean) - 1))
        labels, themes = group_reviews(clean.tolist(), count)
        results = pd.DataFrame({'review': clean, 'theme': [f'Theme {x+1}' for x in labels]})
        for number in range(count):
            subset = results[results.theme == f'Theme {number+1}']
            with st.expander(f'Theme {number+1} · {len(subset)} reviews · {themes[number]}', expanded=True):
                for review in subset.review.head(5):
                    st.write('•', review)
        st.download_button('Download grouped reviews', results.to_csv(index=False), 'grouped_reviews.csv', 'text/csv')
    else:
        st.info('Provide at least four reviews with ten or more characters each.')
except (ValueError, KeyError) as error:
    st.error(f'Could not group these reviews: {error}')
st.caption('Themes are unlabeled clusters, not sentiment scores. Read example reviews before naming a theme.')
