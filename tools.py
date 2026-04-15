import os

OUTPUT_DIR = "output"

def create_file(filename):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write("")
    return f"File created: {path}"

def write_code(filename, code):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write(code)
    return f"Code written to {path}"

def summarize_text(text):
    return text[:100] + "..."  # simple MVP