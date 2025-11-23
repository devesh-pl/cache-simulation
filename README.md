# Cache Simulation

A Python-based cache simulation project using Redis. This project demonstrates how caching works by storing and retrieving data efficiently using an in-memory data store.

## 🚀 Features
- Simulates cache behavior using Redis
- Stores and retrieves task data
- Uses CSV input for loading data
- Displays cached data efficiently

## 🛠️ Tech Stack
- Python
- Redis
- CSV for data storage
- Git for version control

## 📂 Project Structure
cache-simulation/
│
├── load_tasks.py # Loads tasks from CSV to Redis
├── view_tasks.py # Displays cached tasks
├── tasks.csv # CSV input file
├── requirements.txt # Python dependencies
└── README.md # Project documentation
## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Start Redis Server
redis-server

4️⃣ Load Data from CSV to Redis
python3 load_tasks.py

5️⃣ View Cached Data
python3 view_tasks.py

redis==5.0.7
matplotlib==3.9.2
pandas==2.2.2
