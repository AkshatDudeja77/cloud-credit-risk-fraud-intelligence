import pandas as pd
from sklearn.ensemble import IsolationForest

# -----------------------------
# Layer 1: Transaction Risk Engine
# -----------------------------

# Load transaction dataset
df = pd.read_csv("creditcard.csv")

# Select key behavioral features
transaction_features = df[['Time', 'Amount']]

# Initialize Isolation Forest
transaction_model = IsolationForest(
    n_estimators=100,
    contamination=0.01,
    random_state=42
)

# Train model and predict anomalies
df['Transaction_Risk_Flag'] = transaction_model.fit_predict(transaction_features)

# Convert model output to readable labels
df['Transaction_Risk_Flag'] = df['Transaction_Risk_Flag'].map({
    -1: 'High Transaction Risk',
     1: 'Normal Transaction'
})

# Save output for downstream layers
df.to_csv("transaction_risk_output.csv", index=False)

print("Transaction Risk Engine complete. Output saved as transaction_risk_output.csv")
