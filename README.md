

---

### ✅ `README.md`

```markdown
# 📊 School Performance Dashboard Web App

This Flask web app allows you to upload student performance data (CSV or Excel format) and visualize it using interactive charts. It helps educators compare **Pre-Summative** and **Post-Summative** marks and understand student progress easily.

## 🚀 Features

- 📁 Upload student data via CSV or Excel
- 📊 Interactive Pie Chart: Average Pre vs Post Summative
- 📈 Line Chart: Individual student performance comparison
- 🖨️ Print-optimized dashboard (A4 Landscape)
- 🔐 Secure file upload handling

## 🛠️ Tech Stack

- **Backend**: Python, Flask, Pandas
- **Frontend**: HTML, CSS, Chart.js
- **File Support**: `.csv`, `.xlsx`

## 📂 File Upload Format

The uploaded file **must** contain these columns:

| Column Name     | Description                     |
|-----------------|---------------------------------|
| `Name`          | Name of the student             |
| `Pre_Summative` | Marks before the summative exam |
| `Post_Summative`| Marks after the summative exam  |

**Example:**
```csv
Name,Pre_Summative,Post_Summative
Alice,75,88
Bob,60,72
Charlie,90,85
```

## 🧑‍💻 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/school-performance-dashboard.git
   cd school-performance-dashboard
   ```

2. **Create a Virtual Environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**
   ```bash
   python app.py
   ```

5. **Visit the App in Browser**
   ```
   http://127.0.0.1:5000/
   ```

## 📁 Project Structure

```
school-performance-dashboard/
│
├── app.py                # Main Flask application
├── uploads/              # Directory to store uploaded files
├── requirements.txt      # Required Python libraries
└── README.md             # Project documentation
```

## 📌 Notes

- Make sure your uploaded file follows the correct column format.
- Dashboard is optimized for A4 landscape printing.

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

**Developed with ❤️ using Flask & Chart.js**
```

---

### ✅ `requirements.txt`

```txt
Flask
pandas
openpyxl
```

---


