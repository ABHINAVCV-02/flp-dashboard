

### 📄 `README.md`
```markdown
# 📊 School Performance Dashboard

A simple Flask web app to visualize student academic performance using uploaded Excel or CSV files. It compares **Pre-Summative** and **Post-Summative** marks using charts, and visually highlights weak students (marks below 50).

---

## 🚀 Features

- Upload Excel (`.xlsx`) or CSV files.
- Automatically parses student performance.
- Displays:
  - 📈 Line chart for each student's Pre vs Post Summative marks.
  - 🥧 Pie chart showing average Pre vs Post Summative performance.
- **Auto-highlights weak students** (marks below 50) in red.
- Fully responsive and print-friendly (A4 landscape).

---

## 📝 Data Format (Excel or CSV)

Your file should include at least the following columns:

| Student Name | Pre_Summative | Post_Summative |
|--------------|---------------|----------------|
| Alice        | 40            | 55             |
| Bob          | 70            | 65             |

> Column headers are case-insensitive and flexible (`Student Name` or `Name` are both accepted).

---

## 📦 Installation

1. Clone or download the repository.
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

4. Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📂 File Structure

```
├── app.py               # Main Flask application
├── uploads/             # Uploaded files are stored here
├── requirements.txt     # Python dependencies
└── README.md            # You're reading it now!
```

---

## 📌 Dependencies

- Flask
- pandas
- openpyxl

---

## 🧠 Future Improvements (Ideas)

- Add table for weak students.
- Export charts to PDF.
- Filter by subject/term.
- Authentication for multi-school use.

---

## 🛠️ Author

Built with ❤️ using Flask and Chart.js.

```

---

### 📄 `requirements.txt`
```txt
Flask>=2.0.0
pandas>=1.3.0
openpyxl>=3.0.0
```

---
