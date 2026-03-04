# 🏀 Aris Thessaloniki Basketball Analytics

A data engineering project that automatically collects, processes and visualizes 
basketball statistics for Aris Thessaloniki (Basket League 2024-2025).

---

## 📌 What This Project Does

- Fetches real game data from the API-Basketball for Aris Thessaloniki
- Processes and enriches the raw data (wins/losses, points, opponents)
- Displays an interactive dashboard with charts and statistics

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas | Data processing and transformation |
| Streamlit | Interactive dashboard |
| Plotly | Data visualization |
| API-Basketball | Data source |

---

## 📁 Project Structure
```
AbcAnalytics/
├── data/
│   ├── raw/                  # Raw data from API
│   └── processed/            # Transformed data
├── src/
│   ├── scraper.py            # Fetches data from API
│   ├── transformer.py        # Processes raw data
│   └── dashboard.py          # Streamlit dashboard
├── .env                      # API credentials (not included)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ How To Run

**1. Clone the repository**
```bash
git clone https://github.com/your-username/AbcAnalytics.git
cd AbcAnalytics
```

**2. Create a virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up your API key**

Create a `.env` file in the root folder:
```
API_BASKETBALL_KEY=your_api_key_here
```
Get your free API key at [api-basketball.com](https://www.api-basketball.com)

**5. Run the pipeline**
```bash
# Step 1: Fetch data
python src/scraper.py

# Step 2: Process data
python src/transformer.py

# Step 3: Launch dashboard
streamlit run src/dashboard.py
```

---

## 📊 Dashboard Preview

The dashboard includes:
- Season overview (total games, wins, losses, average points)
- Points per game bar chart (Aris vs opponent)
- Win/Loss pie chart
- Points distribution by league (Basket League vs Eurocup)
- Full game log table

---

## 👤 Author

**Nikolaos Chalatsis** — Junior Data Engineer  
[GitHub](https://github.com/NChalatsis) · [LinkedIn](https://www.linkedin.com/in/nchalatsis/)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).