# Review Theme Finder

Upload a CSV of short written reviews and group similar comments. TF-IDF turns review text into word and phrase counts; K-means groups similar vectors. The app shows top phrases and real example reviews for each group, then lets you export the assignments.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Start with the bundled `sample_reviews.csv`, then upload your own CSV. Select the text column and adjust the number of themes. Clusters are suggestions, not automatically correct topic names. Very short or mixed-topic reviews may group poorly. No reviews are sent to an AI service.

## Learn the code

See [How it works](HOW_IT_WORKS.md) for the data flow, hands-on checks, limitations, and ideas for your own changes.
