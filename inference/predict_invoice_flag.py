import joblib
import pandas as pd

MODEL_PATH = "models/predict_flag_invoice.pkl"

def load_model(model_path: str = MODEL_PATH):
    """
    Load trained classifier model.
    """
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    return model

def predict_invoice_flag(input_data):
    """
    Predict invoice flag for new vendor invoices.

    Parameters
    ----------
    input_data : dict

    Returns
    -------
    pd.DataFrame with predicted flag
    """
    model = load_model()
    input_df = pd.DataFrame(input_data)
    input_df['Predicted_Flag'] = model.predict(input_df).round()
    return input_df

if __name__ == "__main__":
   # Test data - exactly 5 features
    sample_data = {
        "invoice_quantity": [50],
        "invoice_dollars": [1200.0],
        "Freight": [45.0],
        "total_item_quantity": [50],
        "total_item_dollars": [1195.0]
    }

    print("\n--- Running Local Terminal Test ---")
    result = predict_invoice_flag(sample_data)
    
    if result is not None:
        print("SUCCESS!")
        print(result[['invoice_dollars', 'total_item_dollars', 'Predicted_Flag']])
        
        flag_val = result['Predicted_Flag'].iloc[0]
        status = "HIGH RISK" if flag_val == 1 else " LOW RISK"
        print(f"\nResult: {status}")
    else:
        print("Test failed. See errors above.")
    