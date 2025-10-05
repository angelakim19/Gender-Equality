import os
import re

# Path to your project folder — current folder
PROJECT_DIR = "./"

# Patterns to remove (Lovable scripts, meta tags, badges)
patterns = [
    r'<script[^>]*src=["\'].*lovable.*["\'][^>]*></script>',  # Remove Lovable scripts
    r'<meta[^>]*name=["\']lovable["\'][^>]*>',               # Remove Lovable meta tags
    r'<img[^>]*src=["\'].*lovable.*["\'][^>]*>',             # Remove Lovable badge images
]

# Function to clean a single file
def clean_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return  # Skip unreadable files

    original_content = content
    for pattern in patterns:
        content = re.sub(pattern, '', content, flags=re.IGNORECASE)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Cleaned: {filepath}")

# Walk through all files in the project directory
for root, dirs, files in os.walk(PROJECT_DIR):
    for file in files:
        if file.endswith((".html", ".htm", ".js", ".jsx", ".ts", ".tsx")):  # Scan HTML/JS/TS files
            clean_file(os.path.join(root, file))

print("🎉 Done! Lovable references removed.")
