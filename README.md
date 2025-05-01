# Listfy - Fast RockYou-Style Wordlist Generator

> 🚀 A high-performance, optimized password wordlist generator inspired by RockYou — perfect for CTFs, pentesting, and password audits.

---

Listfy is a Python-based tool that quickly creates custom password wordlists based on personal information, common patterns, and password mutation techniques — all tuned for speed and efficiency. Ideal for generating targeted wordlists for ethical hacking and security assessments.

## ✨ Features

- **Fast generation** using optimized mutations and combinations
- Supports:
  - Leet speak substitutions
  - Suffix symbols (e.g., `123`, `!`, `2024`)
  - Common password words (e.g., `password`, `admin`)
- Smart handling of:
  - Names
  - Surnames
  - Birthdates (with multiple formats)
  - Phone numbers
  - Additional custom inputs
- Cleans output based on password length (default 8–20 chars)
- Provides wordlist statistics (count, avg length, size)

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Listfy.git
cd Listfy
(Optional) Create a virtual environment:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install requirements:

pip install -r requirements.txt
⚙️ Usage
Run Listfy with:

python listfy.py
You’ll be prompted to input:

Name

Surname

Birthdate (DDMMYYYY)

Phone number
```


Any additional information

Example run:
```bash
Enter your name (Press Enter to skip): john
Enter your surname (Press Enter to skip): doe
Enter your birth date (DDMMYYYY) (Press Enter to skip): 01011990
Enter your phone number (Press Enter to skip): 1234567890
Enter additional info (Press Enter to skip): company
Enter additional info (Press Enter to skip):
When finished, Listfy will generate and save your custom wordlist.

📊 Example Output
📝 Raw input words count: 4
🔄 Variants before cleaning: 1442
💡 Total passwords after cleaning (8-20 chars): 1127
✅ Done! Saved 1127 passwords to 'custom_rockyou.txt'
📊 Stats for custom_rockyou.txt:
  Total passwords: 1127
  Avg length: 11.82
  Shortest length: 8
  Longest length: 20
  File size: 19 KB
```
---

📂 Output
The final wordlist (default filename: custom_rockyou.txt) contains:

All mutations and combinations of your inputs

Passwords between 8 and 20 characters

Cleaned, deduplicated, and sorted

---
🛠️ Requirements
Python 3.7+
---
📄 License
This project is licensed under the MIT License.
Feel free to contribute, fork, or submit issues!
---
⚠️ Disclaimer
Listfy is intended for ethical use only. Do not use this tool for unauthorized access or illegal activities. The developer is not responsible for misuse.

