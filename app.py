import os
import pandas as pd
from flask import Flask, request, jsonify, render_template_string, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = 'your_secret_key'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

data_json = []

# HTML for Upload Page
upload_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Upload School Report</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 40px; }
        form { margin-top: 20px; }
    </style>
</head>
<body>
    <h2>Upload Student Performance Excel/CSV</h2>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept=".csv,.xlsx" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
'''

# HTML for Dashboard Page
dashboard_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>School Performance Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        @media print {
            @page {
                size: A4 landscape;
                margin: 1cm;
            }
        }
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            max-width: 100%;
        }
        h2 {
            text-align: center;
        }
        .charts-container {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        .chart-box {
            width: 45%;
            height: 300px;
            margin-bottom: 30px;
        }
        canvas {
            width: 100% !important;
            height: 100% !important;
        }
    </style>
</head>
<body>
    <h2>School Performance Dashboard</h2>
    <div class="charts-container">
        <div class="chart-box">
            <canvas id="pieChart"></canvas>
        </div>
        <div class="chart-box">
            <canvas id="lineChart"></canvas>
        </div>
    </div>

    <script>
        fetch('/data')
        .then(response => response.json())
        .then(data => {
            if (!data.length) {
                document.body.innerHTML += "<p>No data found. Please upload a valid file.</p>";
                return;
            }

            const names = data.map(item => item.Name);
            const preMarks = data.map(item => item.Pre_Summative);
            const postMarks = data.map(item => item.Post_Summative);

            const avgPre = preMarks.reduce((a, b) => a + b, 0) / preMarks.length;
            const avgPost = postMarks.reduce((a, b) => a + b, 0) / postMarks.length;

            // Pie Chart
            new Chart(document.getElementById('pieChart').getContext('2d'), {
                type: 'pie',
                data: {
                    labels: ['Avg Pre-Summative', 'Avg Post-Summative'],
                    datasets: [{
                        data: [avgPre, avgPost],
                        backgroundColor: ['#3498db', '#2ecc71']
                    }]
                },
                options: {
                    plugins: {
                        legend: { position: 'bottom' }
                    }
                }
            });

            // Weak student names will be colored red on x-axis
            const weakIndexes = [];
            preMarks.forEach((mark, i) => {
                if (mark < 50 || postMarks[i] < 50) weakIndexes.push(i);
            });

            const labelColors = names.map((_, i) =>
                weakIndexes.includes(i) ? 'red' : 'black'
            );

            // Line Chart
            new Chart(document.getElementById('lineChart').getContext('2d'), {
                type: 'line',
                data: {
                    labels: names,
                    datasets: [
                        {
                            label: 'Pre-Summative',
                            data: preMarks,
                            borderColor: '#e67e22',
                            fill: false
                        },
                        {
                            label: 'Post-Summative',
                            data: postMarks,
                            borderColor: '#27ae60',
                            fill: false
                        }
                    ]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { position: 'bottom' }
                    },
                    scales: {
                        x: {
                            ticks: {
                                callback: function(value, index) {
                                    return this.getLabelForValue(index);
                                },
                                color: function(context) {
                                    return labelColors[context.index];
                                }
                            }
                        },
                        y: {
                            beginAtZero: true,
                            max: 100
                        }
                    }
                }
            });
        })
        .catch(err => {
            document.body.innerHTML += "<p>Error loading data: " + err.message + "</p>";
            console.error("Detailed Error:", err);
        });
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(upload_html)

@app.route('/upload', methods=['POST'])
def upload_file():
    global data_json

    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    try:
        if filename.endswith('.csv'):
            df = pd.read_csv(filepath)
        elif filename.endswith('.xlsx'):
            df = pd.read_excel(filepath, engine='openpyxl')
        else:
            return "Unsupported file format", 400
    except Exception as e:
        return f"Error processing file: {e}", 500

    # Normalize column names
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

    # Rename columns
    col_map = {
        'student_name': 'Name',
        'name': 'Name',
        'pre_summative': 'Pre_Summative',
        'post_summative': 'Post_Summative'
    }
    df.rename(columns=col_map, inplace=True)

    required_columns = {'Name', 'Pre_Summative', 'Post_Summative'}
    if not required_columns.issubset(df.columns):
        return f"Missing required columns: {required_columns - set(df.columns)}", 400

    # Clean data
    df['Pre_Summative'] = pd.to_numeric(df['Pre_Summative'], errors='coerce')
    df['Post_Summative'] = pd.to_numeric(df['Post_Summative'], errors='coerce')
    df.dropna(subset=['Name', 'Pre_Summative', 'Post_Summative'], inplace=True)

    data_json = df.to_dict(orient='records')
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template_string(dashboard_html)

@app.route('/data')
def data():
    return jsonify(data_json)

if __name__ == '__main__':
    app.run(debug=True)
