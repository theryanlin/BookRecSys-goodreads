# BookRecSys-goodreads
 
# BookRecSys-goodreads

A book recommender system built on Goodreads data (goodbooks-10k), comparing
classical, deep learning, and multimodal recommendation algorithms — and
finding that the "best" model depends on what you measure.

## The problem

Goodreads recommends books based on user ratings, but new users hit a
**cold start**: you have to rate 20+ books before getting any recommendations.
This project tries different algorithms for different situations instead of
betting on a single model.

## Dataset

- **Ratings:** 53,424 users × 10,000 books, ~6.0M ratings (98.88% sparse)
- **Book tags:** 34,252 raw user tags filtered down to 37 genres
  (fiction, fantasy, mystery, romance, sci-fi, …), ~6.5 tags per book

## Methods compared

| Model | Type | Idea |
|-------|------|------|
| Most Popular | Baseline | Recommend globally top-rated books |
| BPR | Classical | Bayesian personalized ranking (K=300) |
| BiVAE | Deep learning | Bilateral variational autoencoder |
| VBPR | Multimodal | Visual BPR — book cover images (ResNet) + genre tags fused into latent factors |
| CTR | Topic model | Collaborative topic regression on book descriptions (K=300) |

User-based / item-based collaborative filtering, WMF, and LIBFM are also
explored in the notebooks.

## Results

Evaluated with Recall@20, NDCG@20, NCRR@20, and their harmonic mean:

| Model | Recall@20 | NDCG@20 | NCRR@20 | Harmonic mean |
|-------|-----------|---------|---------|---------------|
| Most Popular | 0.0544 | **0.1083** | **0.1177** | 0.0831 |
| BPR | 0.1118 | 0.0730 | 0.0876 | 0.0881 |
| VBPR | 0.1353 | 0.0528 | 0.0266 | 0.0469 |
| CTR | **0.2501** | 0.1025 | 0.0553 | 0.0942 |
| BiVAE | 0.2262 | 0.1016 | 0.0598 | **0.0968** |

## Key findings

1. **BiVAE is the best all-rounder** (highest harmonic mean) — but the simple
   Most Popular baseline surprisingly wins on NDCG/NCRR, i.e. ranking-position
   accuracy. Popular books are popular for a reason.
2. **CTR has the highest recall** — book attributes (topics/genres) genuinely
   help surface more relevant items.
3. **VBPR underperforms on ranking** — adding book-cover images as a modality
   did not improve ranking quality here. More data modalities ≠ better results.

Takeaway: for history-based book recommendation, data volume matters more than
model complexity — so the final system combines Most Popular with the deep
learning model, serving different recommendations to different user types.

## Demo

A working demo website (`Demo_Website/`) shows personalized stats — favorite
books, favorite genres, average rating — plus "Picks for you" recommendations.

## Repo structure

```
├── *.ipynb                  # model experiments (BPR, BiVAE, VBPR, CTR, CF baselines)
├── Demo_Website/            # working recommendation demo
├── coding/                  # helper scripts
├── goodbooks-10k-dataset/   # dataset
└── Projecr Report.pdf       # full project report (slides)
```

## Team

Group project with Bai Xinyue, Liang Yingfang, and Wang Jiali.
