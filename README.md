# Review Theme Finder

Upload a CSV of written reviews to find recurring topics. The app groups similar comments, shows representative reviews and important phrases, and exports the assignments.

**Purpose:** When feedback is scattered across many comments, grouping it helps someone inspect common complaints and praise. The groups are suggestions for a human to review.

## Features

- Uses the included sample immediately or accepts a CSV upload.
- Lets you choose the text column and number of themes.
- Displays each group's size, top phrases, and example comments.
- Downloads a CSV with every usable review and its assigned group.

## Run locally

```bash
git clone https://github.com/Ayanshxkeel/review-theme-finder.git
cd review-theme-finder
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit. On Windows, activate with `.venv\Scripts\activate`.

## Try it

The 12 bundled comments should form three groups of four at the default setting: delivery, setup, and price. Change the slider to two themes and notice that topics must merge. For your own data, upload a CSV with a review column, select it, and inspect comments before naming the groups.

## How it works

The app removes blank and very short comments. **TF-IDF** converts words and two-word phrases to numerical features. **K-means** groups the review vectors into the number of themes you select. Top phrases in each group are shown as hints. See [How it works](HOW_IT_WORKS.md) for a code walkthrough.

## Files

| File | Purpose |
| --- | --- |
| `app.py` | CSV handling, clustering, and interface |
| `sample_reviews.csv` | Small, inspectable example |
| `requirements.txt` | Python dependencies |
| `HOW_IT_WORKS.md` | Explanation and hands-on changes |

## Limits and privacy

K-means needs a chosen theme count and can place mixed-topic comments in an imperfect group. Top phrases are not verified labels or sentiment scores. Uploaded reviews are processed by the running app, not sent to a separate AI API; avoid uploading confidential reviews to a public host you do not control.
