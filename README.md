# habitacion-compatibility-app
🏘️ Streamlit app for Habitacion.com simulating a real-world recommendation system to match compatible co-owners based on psychographic data. Uses Python, Pandas, NumPy, and cosine similarity to reduce a pool of 12,000 candidates into a curated shortlist. Built for scalable decision-making in shared property ownership.

<# Roommate Compatibility App 🏠

**Streamlit app** that suggests compatible roommates based on habits and preferences.  
Developed by **Carlos Onrubia Rodríguez** · *Data Scientist & Analytics*.

![Demo](assets/captura_home.png)

---

## ✨ Features
- Top-N roommate recommendations based on similarity.
- Interactive charts and comparison tables.
- Clean modular architecture: logic, helpers, and UI separated.
- Lightweight: uses `pandas.get_dummies` instead of scikit-learn.

---

## 🧰 Tech Stack
- **Python 3.11**
- **Streamlit**
- **pandas**, **numpy**
- **matplotlib**, **seaborn**
- **plotly**

---

## 📂 Project Structure
.
├─ app/
│ ├─ main.py # Streamlit UI
│ ├─ logica.py # Compatibility calculation & encoding
│ ├─ ayudantes.py # Charts & tables
│ ├─ dataset_inquilinos.csv
│ └─ Media/
│ └─ portada.png
├─ requirements.txt
└─ README.md


---

## 🚀 Run Locally
```powershell
# 1. Clone the repository
git clone https://github.com/Carlos23-oss/habitacion-compatibility-app.git
cd habitacion-compatibility-app

# 2. Create a virtual environment (Windows, Python 3.11)
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the app
streamlit run app/main.py
Go to 👉 http://localhost:8501

🐳 Run with Docker (optional)
docker build -t roommate-app .
docker run --rm -p 8501:8501 roommate-app

👤 Author

Carlos Onrubia Rodríguez
📌 Data Scientist & Analytics
📧 [https://www.notion.so/Turning-Psychographic-Data-into-Smart-Real-Estate-Decisions-A-Scalable-Recommendation-System-for-Ha-270f57ca73ee80549dd3fdb2ad5eec11]
