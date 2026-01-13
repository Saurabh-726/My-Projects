# 🔐 Secure Password Generator (Python)

A streamlined Python utility that generates high-entropy, random passwords using a combination of alphanumeric characters and special symbols.



## 📖 Overview
This project provides a quick and efficient way to generate 8-character passwords. It utilizes Python's built-in `string` and `random` modules to ensure a diverse character set, making passwords resistant to common dictionary attacks.

## 🛠️ Tech Stack
* **Language**: Python 3.x
* **Core Modules**: `random`, `string`

## ⚙️ How It Works

The script follows a 3-step logic to ensure complexity:
1.  **Pool Creation**: It aggregates uppercase letters, lowercase letters, digits, and punctuation symbols into a single character set.
2.  **Random Selection**: It uses a generator expression to pick 8 characters at random from this pool.
3.  **String Assembly**: It joins these characters into a single string for output.

### Character Breakdown
The generator pulls from the following sets:
* **Letters**: `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`
* **Digits**: `0123456789`
* **Punctuation**: `!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`

## 🚀 Installation & Usage

### 1. Prerequisites
Ensure you have Python installed on your system.

### 2. Run the Script
Clone the repository and run the file directly:
```bash
python password_gen.py
🔐 Security Note: Random vs. Secrets
This version uses the random module, which is suitable for general use. However, for high-security environments (like banking or server root passwords), it is recommended to use the secrets module, as it is cryptographically secure.

To upgrade to the secure version, change the code to:

Python

import secrets
# ...
password = "".join(secrets.choice(characters) for i in range(12))
🛠️ Planned Enhancements
[ ] Custom Length: Allow users to specify password length via command-line arguments.

[ ] Strength Meter: Analyze the generated password and provide a "Strength Score."

[ ] Clipboard Support: Automatically copy the password to the clipboard after generation.

[ ] GUI Version: A simple windowed interface using Tkinter.
