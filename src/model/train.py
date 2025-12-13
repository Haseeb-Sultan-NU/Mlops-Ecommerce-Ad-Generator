import pandas as pd
import mlflow
import mlflow.transformers
import os
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import Dataset

# Configuration
MODEL_NAME = "distilgpt2"
DATA_PATH = "data/products.csv"
OUTPUT_DIR = "model_output"
MLFLOW_URI = "http://localhost:5001"  # Connecting to your Docker Container

def train_model():
    # 1. Setup MLflow
    mlflow.set_tracking_uri(MLFLOW_URI)
    mlflow.set_experiment("ad_creative_gen_experiment")

    print(f"Loading data from {DATA_PATH}...")
    try:
        df = pd.read_csv(DATA_PATH)
        # Simple text format for training
        df['text'] = "Title: " + df['title'] + " \n Description: " + df['description']
        dataset = Dataset.from_pandas(df[['text']])
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    print(f"Loading base model: {MODEL_NAME}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

    def tokenize_function(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=64)

    tokenized_datasets = dataset.map(tokenize_function, batched=True)
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    training_args = TrainingArguments(
        output_dir="./results",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        logging_steps=10,
        save_strategy="no",
        report_to="mlflow" # We rely on manual MLflow logging below
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets,
        data_collator=data_collator,
    )

    print("Starting training...")
    with mlflow.start_run():
        mlflow.log_param("base_model", MODEL_NAME)
        
        # Run Training
        trainer.train()
        
        # Log the model to MLflow (Cloud/Container storage)
        mlflow.transformers.log_model(
            transformers_model={"model": model, "tokenizer": tokenizer},
            artifact_path="ad_model"
        )

    # 2. Save Model Locally (For the API Phase)
    print(f"Saving model artifacts locally to {OUTPUT_DIR}...")
    model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print("Model saved successfully.")

if __name__ == "__main__":
    train_model()