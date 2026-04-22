# 📧 Email Spam Detection using Machine Learning

> A machine learning pipeline for classifying emails as **spam or ham** using NLP and multiple ML models — with automated PR evaluation and a live accuracy leaderboard.

🌐 **Live Leaderboard:** [https://omk26.github.io/Email-Spam-Detection/](https://omk26.github.io/Email-Spam-Detection/)

---

## 📌 Problem Statement

This project aims to classify emails as **spam or not spam (ham)** using machine learning and Natural Language Processing (NLP) techniques. Spam detection is a crucial task in cybersecurity to prevent phishing attacks and unwanted messages.

---

## 🧠 Techniques Used

### 🔹 Text Preprocessing
- Lowercasing
- Removal of stopwords
- Tokenization and cleaning

### 🔹 Feature Extraction
- **TF-IDF Vectorization** to convert text data into numerical form

### 🔹 Machine Learning Models
- Logistic Regression
- Random Forest
- Gradient Boosting
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)

---

## 📊 Results

The models were evaluated using **Accuracy, ROC-AUC, and Cross-Validation scores**.

| Model               | Accuracy   | ROC-AUC    | CV Score   |
| ------------------- | ---------- | ---------- | ---------- |
| Logistic Regression | 87.40%     | 0.9524     | 0.8898     |
| Random Forest       | 88.80%     | 0.9604     | 0.9001     |
| Gradient Boosting   | **89.35%** | **0.9672** | **0.9065** |
| SVM                 | 87.55%     | 0.9492     | 0.8914     |
| KNN                 | 84.55%     | 0.9145     | 0.8592     |

### 🏆 Best Model

**Gradient Boosting** performed the best due to its ability to combine multiple weak learners and reduce both bias and variance.

---

## 🤖 Automated Evaluation & Leaderboard

This repository uses **GitHub Actions** to automatically evaluate every pull request and track accuracy over time.

### How it works

1. A contributor opens or updates a Pull Request
2. The workflow automatically runs `evaluate.py` against the test dataset
3. The accuracy score is recorded in `leaderboard.csv` with the commit hash and timestamp
4. A **comment is posted on the PR** with the evaluation result
5. The [live leaderboard](https://omk26.github.io/Email-Spam-Detection/) updates automatically

### Workflow file

The CI/CD pipeline is defined in `.github/workflows/evaluate.yml`. It:
- Sets up **Python 3.11** and installs all dependencies from `requirements.txt`
- Runs `evaluate.py` from the repository root
- Commits the updated `leaderboard.csv` back to the `main` branch
- Copies the leaderboard to `docs/` so GitHub Pages can serve it
- Posts the result as a PR comment

### Submitting your model

1. Fork this repository
2. Implement your model logic inside `evaluate.py` (see the `TODO` comments)
3. Open a Pull Request — the workflow will evaluate it automatically
4. Check the PR comment for your accuracy score and view your rank on the [leaderboard](https://omk26.github.io/Email-Spam-Detection/)

---

## 📁 Project Structure

```
Email-Spam-Detection/
│
├── .github/
│   └── workflows/
│       └── evaluate.yml        # GitHub Actions CI/CD workflow
│
├── data/
│   ├── spam_email_dataset.csv  # Raw dataset
│   ├── train.csv               # Training split
│   └── test.csv                # Test split (used by evaluate.py)
│
├── docs/
│   ├── index.html              # GitHub Pages leaderboard UI
│   └── leaderboard.csv         # Auto-synced copy for GitHub Pages
│
├── notebooks/
│   └── email-spam-detection-5-ml-models.ipynb
│
├── starter_code/
│   └── baseline.py             # Baseline model for reference
│
├── evaluate.py                 # Evaluation script (run on every PR)
├── leaderboard.csv             # Master leaderboard (auto-updated)
├── requirements.txt            # Python dependencies
└── README.md
```

---

## ⚙️ Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/omk26/Email-Spam-Detection.git
cd Email-Spam-Detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the evaluation script locally

```bash
python evaluate.py
```

This will run your model against `data/test.csv` and update `leaderboard.csv` with the result.

### 4. Explore the notebooks

```bash
jupyter notebook notebooks/email-spam-detection-5-ml-models.ipynb
```

---

## 📂 Dataset

The dataset contains labeled email messages:

| Label | Value | Meaning          |
|-------|-------|------------------|
| Ham   | 0     | Legitimate email |
| Spam  | 1     | Spam/junk email  |

Files:
- `data/spam_email_dataset.csv` — full raw dataset
- `data/train.csv` — training split
- `data/test.csv` — test split (used by the evaluator)

---

## 🚀 Key Highlights

- Applied **NLP techniques** for real-world text classification
- Compared **5 ML models** with comprehensive metrics
- Used **TF-IDF vectorization** for feature extraction
- Evaluated using Accuracy, ROC-AUC, and Cross-Validation scores
- **Automated PR evaluation** via GitHub Actions
- **Live leaderboard** hosted on GitHub Pages

---

## 🔮 Future Scope

- Improve performance using **Deep Learning (LSTM / Transformers)**
- Deploy as a **web application**
- Extend to **phishing and scam detection systems**
- Add ROC-AUC and F1 score tracking to the leaderboard

---

## 👨‍💻 Author

**Om Kumbhar**
- GitHub: [@omk26](https://github.com/omk26)
- Project: [Email-Spam-Detection](https://github.com/omk26/Email-Spam-Detection)
