# 🔐 Password Analysis and Digital Security Project
This is a Password Analysis and Security Tool built with Streamlit that provides:

<img width="1365" height="618" alt="Screenshot From 2025-07-31 21-35-40" src="https://github.com/user-attachments/assets/cab23e50-4317-4f26-86ef-5b7961ed50b8" />

<div align="center">

![Eyes Logo](assets/eyes.png)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**A comprehensive password analysis and digital security auditing tool using artificial intelligence**

[Arabic](#Arabic) | [English](#english)

</div>

---
## Arabic

### 📋 Overview

The Password Analysis and Digital Security Project is a comprehensive tool developed in Python that aims to:

- **Password strength analysis** using artificial intelligence algorithms
- **Data leak scanning** for email and passwords
- **Search social media accounts** associated with users
- **Password clustering** using the K-Means algorithm
- **Automatically generate strong passwords**
- **Interactive user interface** using Streamlit

### ✨ Key Features

#### 🔍 Password Analysis
- Comprehensive analysis of password characteristics (length, uppercase/lowercase letters, numbers, symbols)
- Detection of common and weak patterns
- Evaluation of password strength (strong/average/weak)
- Recommendations for password improvement

#### 🛡️ Leak Scanning
- Scanning passwords against leak databases Known
- Email Scanning for Data Leaks
- View Leak Details (Date, Source, Type of Leaked Data)

#### 👁️ Eyes Email Scanning Tool
- Comprehensive Email Scanning Across Multiple Platforms
- Support for the following platforms:
- Duolingo
- GitHub
- Gravatar
- Imgur
- Mail.ru
- Pastebin
- Protonmail
- Bitmoji
- Instagram
- X (Twitter)

#### 🤖 Artificial Intelligence
- Password Clustering Using the K-Means Algorithm
- Text Analysis Using TF-IDF
- Automatically Generate Strong Passwords
- Graphical Visualizations for Analytics

#### 🌐 User Interface
- Interactive Web Interface Using Streamlit
- Arabic Language Support
- Upload CSV Files to Analyze Password Clusters
- Display Results Visually and Interactively

### 🚀 Installation and Setup

#### Prerequisites
- Python 3.8 or higher Latest
- pip (Python Package Manager)

#### Installation Steps

1. **Clone the Project**
```bash
git clone https://github.com/yourusername/password_analysis_project.git
cd password_analysis_project
```

2. **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate # on Linux/Mac
# or
venv\Scripts\activate # on Windows
```

3. **Install Requirements**
```bash
pip install -r requirements.txt
```

4. **Set Up API Keys (Optional)**
- For full functionality, set up API keys in the appropriate files:
- RapidAPI key in `social_media.py`
- HaveIBeenPwned API key in `data_breach.py`

### 📖 How to Use

#### 1. Run the Streamlit interface

```bash
streamlit run main.py
```

#### 2. Use the Eyes tool from the command line

```bash
python eyes.py example@email.com
```

Or to view all available modules:

```bash
python eyes.py -m
```

#### 3. Programmatic usage

```python
from password_analysis import analyze_password, evaluate_password_strength
from password_breach import check_password_breach

# Analyze password
password = "MyPassword123!"
analysis = analyze_password(password)
strength = evaluate_password_strength(password)
breach_count = check_password_breach(password)

print(f"Password Analysis: {analysis}")
print(f"Password Strength: {strength}")
print(f"Leak Count: {breach_count}")
```

### 📁 Project Structure

```
password_analysis_project/
├── main.py # Streamlit interface main file
├── eyes.py # Eyes email scanner
├── password_analysis.py # Password analysis module
├── password_breach.py # Password leak detection module
├── data_breach.py # Data leak detection module
├── social_media.py # Social Media Accounts Scanning Module
├── output.py # Results Display Module
├── requirements.txt # Project Requirements
├── assets/ # Images and Auxiliary Files
├── lib/ # Helper Libraries
│ ├── cli.py # Command Line Interface
│ ├── banner.py # Application Banner
│ ├── agents.py # User Agents
│ └── ...
├── modules/ # Email Scanning Modules
│ └── email_modules/
│ ├── github.py
│ ├── instagram.py
│ ├── gravatar.py
│ └── ...
└── facial_recognition/ # Facial Recognition Module (Under Development)
```

### 🔧 Modules and Components

#### Password Analysis Module (`password_analysis.py`)
- `analyze_password()`: Comprehensive analysis of password characteristics
- `detect_common_patterns()`: Detect common and weak patterns
- `evaluate_password_strength()`: Evaluate password strength

#### Leak Scanning Module (`password_breach.py`, `data_breach.py`)
- Scan passwords against leak databases
- Scan emails against known data leaks
- View details of leaks and leaked information

#### Eyes Tool (`eyes.py`, `lib/`, `modules/`)
- Comprehensive email scanning across multiple platforms
- Specialized modules for each platform
- Easy-to-use command-line interface

### 📊 Usage Examples

#### Example 1: Analyzing a Simple Password

```python
from password_analysis import analyze_password, evaluate_password_strength
