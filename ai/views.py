from django.shortcuts import render
from .utils import extract_pdf_text
from .llm import ask_ollama
import os

# Path to your PDF in the project
PDF_PATH = os.path.join(os.path.dirname(__file__), "../../your_pdf_folder/gym_info.pdf")

def recommend_gyms(request):
    user_input = request.GET.get("input", "").strip()
    answer = ""

    if user_input:
        # Extract text from PDF
        pdf_text = extract_pdf_text(PDF_PATH)[:5000]  # limit to first 5000 chars for context
        prompt = f"User wants: {user_input}\nGym info: {pdf_text}\nRecommend three best gyms with reasons."
        
        try:
            answer = ask_ollama(prompt, model="llama3")
        except Exception as e:
            answer = f"Error generating recommendation: {e}"

    return render(request, "ai/recommend.html", {"answer": answer, "user_input": user_input})
