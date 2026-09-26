# Step 1: Install required libraries
!pip install -q transformers torch gradio accelerate

# Step 2: Import dependencies
import gradio as gr
from transformers import pipeline

# Step 3: Load a fast and efficient model for code/text explanation
print("Loading AI Code Doctor model... Please wait.")
# Using FLAN-T5, which is lightweight, instruction-tuned, and fast on Colab
code_doctor_pipeline = pipeline("text-generation", model="google/flan-t5-base", max_length=512)
print("Model loaded successfully!")

# Step 4: Define the core logic for the Code Doctor
def diagnose_code(buggy_code, error_traceback):
    if not buggy_code.strip():
        return "Please provide some buggy code to diagnose."
    
    # Construct a structured prompt for the model
    prompt = (
        f"Analyze this Python code and error. "
        f"1. Explain why it failed. "
        f"2. Provide the corrected code.\n\n"
        f"Code:\n{buggy_code}\n\n"
        f"Error Traceback:\n{error_traceback}"
    )
    
    # Generate the response
    response = code_doctor_pipeline(prompt, max_new_tokens=256)[0]['generated_text']
    return response

# Step 5: Build the Gradio UI
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🩺 AI Python Code Doctor & Explainer")
    gr.Markdown("Paste your broken code or error traceback below. The AI will diagnose the bug, explain the root cause, and provide a fix.")
    
    with gr.Row():
        with gr.Column():
            code_input = gr.Textbox(
                label="Buggy Python Code", 
                placeholder="def add(a, b):\n    return a + c", 
                lines=8
            )
            error_input = gr.Textbox(
                label="Error Traceback (Optional)", 
                placeholder="NameError: name 'c' is not defined", 
                lines=4
            )
            submit_btn = gr.Button("Diagnose Code 🔬", variant="primary")
            
        with gr.Column():
            output_box = gr.Textbox(
                label="Doctor's Diagnosis & Solution", 
                lines=14
            )
            
    submit_btn.click(
        fn=diagnose_code, 
        inputs=[code_input, error_input], 
        outputs=output_box
    )

# Step 6: Launch the app (sets share=True to give you a public link)
demo.launch(share=True, debug=True)
