from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import time
import os
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Ad Creative Generator API", version="1.0")
Instrumentator().instrument(app).expose(app)
# Load Model from local artifacts
MODEL_DIR = "model_output"
print(f"Loading model from {MODEL_DIR}...")

try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = AutoModelForCausalLM.from_pretrained(MODEL_DIR)
    print("Model loaded successfully.")
except Exception as e:
    print(f"CRITICAL ERROR: Could not load model. {e}")
    # Crash if model is missing (Docker should fail to start)
    raise e

class AdRequest(BaseModel):
    product_title: str

@app.get("/")
def health_check():
    return {"status": "healthy", "service": "ad-creative-generator"}

@app.post("/generate")
def generate_ad(request: AdRequest):
    start_time = time.time()
    
    # Prompt Engineering
    input_text = f"Title: {request.product_title} \n Description:"
    
    # Inference
    inputs = tokenizer(input_text, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            inputs.input_ids, 
            max_length=100, 
            num_return_sequences=1,
            do_sample=True,
            top_k=50,
            top_p=0.95
        )
    
    # Decode Output
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Post-processing (Remove the prompt part)
    try:
        ad_copy = generated_text.split("Description:")[1].strip()
    except IndexError:
        ad_copy = generated_text

    duration = time.time() - start_time
    
    return {
        "input": request.product_title,
        "ad_creative": ad_copy,
        "inference_time": round(duration, 4)
    }
