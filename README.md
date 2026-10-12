# Customer Churn Predictor

## 🚀 Live Demo

**Try the application:** [Customer Churn Predictor] https://customer-churn-predictor-sushanthcd.streamlit.app/

An end-to-end Machine Learning project that predicts whether a
telecom customer is likely to leave the service.

The project includes exploratory data analysis, data preprocessing,
model comparison, threshold optimization, model evaluation, and a
Streamlit web application for making predictions.

## Features

- Predicts customer churn using a trained Machine Learning model.
- Displays the estimated probability of churn.
- Uses a customizable customer input form.
- Provides a binary prediction: Yes or No.
- Includes a trained model that can be loaded without retraining.

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

## Machine Learning Workflow

1. Exploratory Data Analysis (EDA)
2. Data cleaning and preprocessing
3. Numerical feature scaling and categorical encoding
4. Logistic Regression and Random Forest comparison
5. Cross-validation and hyperparameter tuning
6. Decision-threshold optimization
7. Model evaluation and error analysis
8. Model serialization using Joblib
9. Deployment using Streamlit

## Model Selection

Logistic Regression was selected as the final model based on its
cross-validation performance, simplicity, and suitability for
the chosen classification threshold.

The decision threshold was selected using out-of-fold predictions
on the training data.

A threshold of 0.35 was chosen to prioritize identifying customers
who are likely to churn, accepting that this produces more false
positives than a threshold of 0.50.

## Test Set Performance

Results on the 20% test split at a decision threshold of 0.35:

| Metric | Result |
|---|---:|
| Accuracy | 84.7% |
| Churn Precision | 68% |
| Churn Recall | 81% |
| Churn F1-Score | 74% |
| ROC-AUC | 92.75% |

The lower decision threshold increases churn recall, helping the
model identify more customers who actually churn. The trade-off is
that more customers who do not churn may be flagged.

## Project Structure

```text
Customer Churn Predictor/
├── customer-churn-predictor/    # Nested folder shown in VS Code
├── notebooks/
│   └── churn_analysis.ipynb
├── .gitignore
├── app.py
├── Customer_Churn_Dataset.xlsx  # Local dataset; excluded from GitHub
├── customer_churn_model.pkl
├── README.md
└── requirements.txt
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Sushanth-CD/customer-churn-predictor.git```

### 2. Enter the project directory

```bash
cd customer-churn-predictor```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Launch the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

http://localhost:8501

Enter customer information and click the prediction button to
view the estimated churn probability and prediction.

## Dataset

The dataset used for training and analysis is not included in this
repository. The trained model is included, so the Streamlit
application does not require the original dataset to make predictions.

## Limitations

- Predictions depend on the quality and representativeness of the
  training dataset.
- The predicted probability is a model estimate, not a guarantee
  that a customer will churn.
- The 0.35 threshold reflects a particular preference for churn
  recall and may not be optimal for every business.
- Further evaluation on a new, untouched dataset would provide a
  stronger assessment of generalization.

## Future Improvements

- Deploy the application publicly.
- Add model monitoring and prediction logging.
- Evaluate performance on new customer data.
- Improve the interface and provide customer-level explanations.