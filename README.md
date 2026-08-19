# IMDB Reviews Sentiment Analysis

A Deep Learning NLP project that uses an **LSTM neural network** to classify IMDB movie reviews as **Positive** or **Negative**.

## 📌 Project Overview

This project performs sentiment analysis on movie reviews using **Natural Language Processing (NLP)** and **Long Short-Term Memory (LSTM)** networks.

The model takes a movie review as input and predicts whether the review expresses a positive or negative sentiment.

## 🧠 How It Works

```text
Movie Review
     ↓
Text Preprocessing
     ↓
Tokenization
     ↓
Padding
     ↓
Embedding Layer
     ↓
LSTM
     ↓
Dense + Sigmoid
     ↓
Positive / Negative
```

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- Pandas
- NumPy
- Scikit-learn
- NLP
- LSTM
- Streamlit

## 📊 Dataset

**IMDB Dataset of 50K Movie Reviews**

- 50,000 movie reviews
- Positive and negative sentiment labels
- 25,000 training reviews
- 25,000 test reviews

## 🏗️ Model Architecture

```text
Input: 200 tokens
        ↓
Embedding
5000 vocabulary × 128 dimensions
        ↓
LSTM
128 units
        ↓
Dense
1 neuron
        ↓
Sigmoid
        ↓
Positive / Negative
```

## ⚙️ Preprocessing

The reviews are processed using:

1. Tokenization
2. Vocabulary limited to 5,000 words
3. Conversion of text into integer sequences
4. Padding sequences to 200 tokens

## 🚀 Installation

```bash
git clone https://github.com/Fahadqureshi0/IMBD-Reviews-Sentiment-Analysis.git

cd IMBD-Reviews-Sentiment-Analysis

pip install -r requirements.txt
```

## ▶️ Run the Project

```bash
streamlit run app.py
```

## 🔮 Example

**Input:**

```text
"This movie was absolutely amazing. I really enjoyed it!"
```

**Prediction:**

```text
Sentiment: Positive
```

## 📈 Future Improvements

- Add Bidirectional LSTM
- Add Attention mechanism
- Improve model accuracy
- Deploy the model
- Add real-time sentiment analysis
- Upgrade to Transformer/BERT-based NLP

## 👨‍💻 Author

**Fahad Qureshi**

GitHub: [Fahadqureshi0](https://github.com/Fahadqureshi0)

## 📄 License

This project is licensed under the MIT License.
