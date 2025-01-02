from transformers import AutoModelForCausalLM, AutoTokenizer
 
# Load your model and tokenizer
model = AutoModelForCausalLM.from_pretrained("your-local-model-path") # Update the path
tokenizer = AutoTokenizer.from_pretrained("your-local-model-path") # Update the path
 
# Push the model to the hub
model.push_to_hub("your-model-name", use_temp_dir=False) # Update the model name. Ex: "RicardoGarces/faq-taylor-swift"
tokenizer.push_to_hub("your-model-name", use_temp_dir=False) # Update the model name. Ex: "RicardoGarces/faq-taylor-swift"