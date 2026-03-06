from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
# utils/preprocess.py

# This function encodes the columns based on their respective encoders
def safe_encode(input_df, encoders):  # Take encoders as an argument
    for col, encoder in encoders.items():
        if col not in input_df.columns:
            continue
        if isinstance(encoder, OrdinalEncoder):
            input_df[[col]] = encoder.transform(input_df[[col]])
        elif isinstance(encoder, LabelEncoder):
            input_df[col] = encoder.transform(input_df[col].astype(str))
    return input_df
# utils/preprocess.py
from utils.load_assets import load_encoders  # Import encoders

# Load encoders globally if needed
encoders = load_encoders()

def get_choices(col):
    enc = encoders.get(col)  # Access the encoder for the column
    if isinstance(enc, LabelEncoder):
        return list(enc.classes_)  # Return the possible choices for LabelEncoder
    if isinstance(enc, OrdinalEncoder):
        return list(enc.categories_[0])  # Return the possible choices for OrdinalEncoder
    return None

def safe_scale(input_df, scalers):
    scaler = scalers.get("StandardScaler")
    if scaler is None:
        return input_df
    scaler_cols = list(getattr(scaler, "feature_names_in_", []))
    if scaler_cols:
        input_df[scaler_cols] = scaler.transform(input_df[scaler_cols])
    return input_df