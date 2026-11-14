# U.S. Phone Number Normalizer 📞

A lightweight Python utility that cleans and formats messy U.S. phone numbers into a standard (XXX) XXX-XXXX layout. Using core string methods like strip and replace, it removes dashes, spaces, and brackets. It validates the 10-digit length and outputs clean data. Perfect for backend validation.

## ✨ Features
* **Symbol Stripping:** Automatically removes common separators like dashes `-`, periods `.`, and parentheses `()`.
* **Whitespace Cleaning:** Strips accidental leading or trailing spaces.
* **Length Validation:** Checks to ensure the final processed input contains exactly 10 digits.

## 🚀 Quick Start

### Installation
Clone this repository to your local machine:
```bash
git clone https://github.com
cd U.S.-phone-normalizer-py-
```

### Usage
Run the script directly in your terminal to try it interactively:
```bash
python main.py
```

You can also import the core function into your own Python projects:
```python
from main import normalize_us_phone

print(normalize_us_phone("123-456-7890"))    # Output: (123) 456-7890
print(normalize_us_phone("(123)456.7890"))   # Output: (123) 456-7890
print(normalize_us_phone("12345"))           # Output: Error: Please enter exactly 10 digits.
```

## 🛠️ Built With
* **Python 3** - Built completely using native string operations (`strip`, `replace`, `split`, `join`).

## 📄 License
This project is licensed under the MIT License.
