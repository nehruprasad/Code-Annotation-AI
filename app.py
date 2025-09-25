import streamlit as st
import ast
from radon.complexity import cc_visit, cc_rank
from radon.metrics import mi_visit, h_visit

st.set_page_config(page_title="Code Annotation AI (NLP)", layout="wide")
st.title("💻 Code Annotation AI (NLP Powered)")

# ----------------- Helper Functions -----------------

def generate_nlp_comments(code):
    """
    NLP-based comment generation:
    - Detect function definitions
    - Describe parameters
    - Insert human-readable explanation above function
    """
    annotated_code = ""
    try:
        tree = ast.parse(code)
        lines = code.split("\n")
        added_lines = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_name = node.name
                params = [arg.arg for arg in node.args.args]
                comment = f"# Function '{func_name}'"
                if params:
                    comment += f" takes parameters {', '.join(params)}"
                comment += " and performs its logic as defined below."

                # Insert comment above function only once
                lineno = node.lineno - 1
                if lineno not in added_lines:
                    annotated_code += comment + "\n"
                    added_lines.add(lineno)
                
                # Add function code
                func_lines = lines[lineno: lineno + len(node.body)+1]
                annotated_code += "\n".join(func_lines) + "\n"

        # If no functions found, return original code
        if annotated_code.strip() == "":
            annotated_code = "# No functions detected\n" + code

    except Exception as e:
        annotated_code = "# Error parsing code for NLP comments: " + str(e)

    return annotated_code

def analyze_complexity(code):
    """
    Use radon to compute cyclomatic complexity for each function
    """
    try:
        cc_results = cc_visit(code)
        complexity_info = []
        for func in cc_results:
            complexity_info.append({
                "Name": func.name,
                "Type": func.type,
                "Complexity": func.complexity,
                "Rank": cc_rank(func.complexity)
            })
        return complexity_info
    except Exception as e:
        return [{"Error": str(e)}]

def generate_documentation(code):
    """
    Generate documentation summary:
    - Number of functions
    - Function names
    - Total lines of code
    - High-level description
    """
    doc_summary = {}
    try:
        tree = ast.parse(code)
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        doc_summary["Number of functions"] = len(functions)
        doc_summary["Functions"] = functions
        doc_summary["Lines of code"] = len(code.split("\n"))
        if functions:
            doc_summary["Description"] = "This code contains " + str(len(functions)) + " function(s) performing defined logic."
        else:
            doc_summary["Description"] = "This code contains no functions."
    except Exception as e:
        doc_summary["Error"] = str(e)
    return doc_summary

# ----------------- Streamlit App -----------------

st.subheader("Paste your Python code below:")
user_code = st.text_area("Code Input", height=250)

if st.button("Annotate Code"):
    if not user_code.strip():
        st.warning("Please paste some Python code first.")
    else:
        # 1️⃣ Generate NLP comments + annotated code
        annotated_code = generate_nlp_comments(user_code)
        st.subheader("📝 Annotated Code (NLP)")
        st.code(annotated_code, language="python")

        # 2️⃣ Complexity analysis
        complexity = analyze_complexity(user_code)
        st.subheader("⚙️ Complexity Analysis")
        if complexity and "Error" not in complexity[0]:
            st.table(complexity)
        else:
            st.write("Error analyzing complexity:", complexity[0]["Error"])

        # 3️⃣ Documentation summary
        documentation = generate_documentation(user_code)
        st.subheader("📄 Documentation Summary (NLP)")
        st.json(documentation)
