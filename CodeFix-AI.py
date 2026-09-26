# Step 1: Install advanced dependencies for MLOps and quantization
!pip install -q transformers torch accelerate bitsandbytes gradio

# Step 2: Import libraries
import ast
import torch
import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

# Step 3: Configure 4-bit quantization for efficient GPU memory usage
print("Initializing quantization config...")
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True
)

# Step 4: Load a specialized Code LLM (Qwen2.5-Coder-7B-Instruct)
MODEL_ID = "Qwen/Qwen2.5-Coder-7B-Instruct"

print(f"Loading elite coding model ({MODEL_ID})... This may take a minute.")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    quantization_config=bnb_config,
    device_map="auto"
)
print("Model loaded successfully with 4-bit optimization!")

# Step 5: Deterministic Code Validation using Python AST
def static_syntax_check(code_string):
    """Performs a fast, deterministic check for syntax errors before hitting the LLM."""
    try:
        ast.parse(code_string)
        return None  # No syntax error found by Python parser
    except SyntaxError as e:
        return f"Python SyntaxError Detected (Pre-AI Check):\nLine {e.lineno}: {e.text}\n{e.msg}"

# Step 6: Core AI Diagnosis Pipeline
def advanced_code_doctor(buggy_code, error_traceback):
    if not buggy_code.strip():
        return "⚠️ Please provide a snippet of code to diagnose."
    
    # Run deterministic check first
    syntax_alert = static_syntax_check(buggy_code)
    
    # Construct professional prompt template
    system_prompt = (
        "You are an elite Principal Software Engineer and Code Reviewer. "
        "Analyze the provided code and error traceback. Provide:\n"
        "1. **Root Cause Analysis**: Exactly why the bug occurs.\n"
        "2. **Corrected Code**: Clean, production-ready, PEP 8 compliant code block.\n"
        "3. **Prevention Tip**: How to avoid this issue in the future."
    )
    
    user_prompt = f"### Buggy Code:\n```python\n{buggy_code}\n```\n\n### Error Traceback:\n{error_traceback if error_traceback else 'None provided'}"
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    
    model_inputs = tokenizer([text], return_tensors="pt").to("cuda")
    
    # Generate response
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=512,
        temperature=0.2, # Low temperature for precise code fixes
        do_sample=True
    )
    
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    # Prepend deterministic alert if syntax is fundamentally broken
    if syntax_alert:
        return f"🚨 **Static Analysis Alert:**\n{syntax_alert}\n\n---\n\n🧠 **AI Deep Dive & Fix:**\n{response}"
    
    return response

# Step 7: Build Professional Gradio Interface
with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
    gr.Markdown("# 🩺 Enterprise AI Code Doctor & Refactoring Assistant")
    gr.Markdown("Powered by **Qwen2.5-Coder-7B** with **4-bit MLOps Quantization** and **AST Static Analysis**.")
    
    with gr.Row():
        with gr.Column(scale=1):
            code_input = gr.Textbox(
                label="Source Code", 
                placeholder="Paste buggy Python code here...", 
                lines=10
            )
            error_input = gr.Textbox(
                label="Error Traceback / Log (Optional)", 
                placeholder="Paste traceback if available...", 
                lines=4
            )
            submit_btn = gr.Button("Run Diagnostics 🔬", variant="primary")
            
        with gr.Column(scale=1):
            output_box = gr.Textbox(
                label="Diagnostic Report & Refactored Solution", 
                lines=16
            )
            
    submit_btn.click(
        fn=advanced_code_doctor, 
        inputs=[code_input, error_input], 
        outputs=output_box
    )

# Step 8: Launch app with public link
demo.launch(share=True, debug=True)
