# Code-Annotation-AI
# Code Annotation AI (NLP Powered)

A Streamlit-based Python application that **automatically annotates Python code**, analyzes complexity, and generates documentation summaries using **NLP techniques** and static code analysis.

---

## **Features**

1. **NLP-based Code Annotation**  
   - Detects function definitions  
   - Describes function parameters  
   - Inserts human-readable comments above functions

2. **Cyclomatic Complexity Analysis**  
   - Uses `radon` to compute complexity for each function  
   - Provides complexity rank (A–F)

3. **Documentation Generation**  
   - Summarizes number of functions  
   - Lists function names  
   - Total lines of code  
   - Provides high-level description of the code  

4. **Interactive Web Interface**  
   - Paste Python code directly  
   - View annotated code, complexity, and documentation instantly

---

## **Requirements**

- Python 3.8+  
- Streamlit  
- Radon  
- NLTK  
- SpaCy (optional for advanced NLP features)  

---

## **Setup Instructions**

1. **Clone the repository** or download the code:

```bash
git clone <repository-url>
cd code_annotation_ai

Create a virtual environment (recommended):

python -m venv venv


Activate the virtual environment:

Windows

venv\Scripts\activate


Linux / Mac

source venv/bin/activate


Install dependencies:

pip install streamlit radon nltk spacy


Download NLTK punkt tokenizer:

import nltk
nltk.download('punkt')


(Optional) Download spaCy English model:

python -m spacy download en_core_web_sm

Running the App

Make sure your virtual environment is active.

Run Streamlit:

streamlit run app.py


Open the URL displayed in your terminal (usually http://localhost:8501).

Paste your Python code into the text area.

Click "Annotate Code" to view:

Annotated code with NLP comments

Complexity analysis table

Documentation summary

Sample Input
def calculate_sum(a, b):
    return a + b

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

Output

Annotated Code: Comments above each function explaining parameters and purpose

Complexity Analysis: Cyclomatic complexity for each function with rank

Documentation Summary: Number of functions, their names, total lines of code, and description

Notes

Works best with valid Python code.

Cyclomatic complexity analysis uses radon.

NLP comments are generated statically and do not execute the code.


