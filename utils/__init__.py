from .load_assets import load_model, load_encoders, load_scalers
from  .preprocess import safe_encode, safe_scale
model = load_model()
encoders = load_encoders()  
scalers = load_scalers()
