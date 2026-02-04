from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

patients = []

# -------------------------------------------------
# HOME ROUTE – HTML PAGE (for Robot Framework)
# -------------------------------------------------
@app.route('/')
def home():
    return render_template("index.html")

# -------------------------------------------------
# FORM SUBMISSION ROUTE (HTML → Backend)
# -------------------------------------------------
@app.route('/register', methods=['POST'])
def register_patient_form():
    data = {
        "name": request.form.get("name"),
        "age": request.form.get("age"),
        "gender": request.form.get("gender"),
        "disease": request.form.get("disease"),
        "doctor": request.form.get("doctor")
    }
    patients.append(data)
    return "Patient Registered Successfully"

# -------------------------------------------------
# API ROUTES (for Pytest / API Automation)
# -------------------------------------------------

# GET all patients
@app.route('/api/patients', methods=['GET'])
def get_patients():
    return jsonify(patients), 200

# POST patient (JSON)
@app.route('/api/patients', methods=['POST'])
def add_patient():
    data = request.json
    patients.append(data)
    return jsonify({"message": "Patient added"}), 201

# GET single patient
@app.route('/api/patients/<int:pid>', methods=['GET'])
def get_patient(pid):
    if pid < len(patients):
        return jsonify(patients[pid]), 200
    return jsonify({"error": "Patient not found"}), 404

# UPDATE patient
@app.route('/api/patients/<int:pid>', methods=['PUT'])
def update_patient(pid):
    if pid < len(patients):
        patients[pid].update(request.json)
        return jsonify({"message": "Patient updated"}), 200
    return jsonify({"error": "Patient not found"}), 404

# -------------------------------------------------
# WEB PAGE – PATIENT LIST (for Web Scraping)
# -------------------------------------------------
@app.route('/patients')
def patient_list_page():
    html = """
    <html>
    <head><title>Patient List</title></head>
    <body>
    <h2>Registered Patients</h2>
    <table border="1">
        <tr>
            <th>Name</th>
            <th>Age</th>
            <th>Gender</th>
            <th>Disease</th>
            <th>Doctor</th>
        </tr>
    """

    for p in patients:
        html += f"""
        <tr>
            <td>{p.get('name')}</td>
            <td>{p.get('age')}</td>
            <td>{p.get('gender')}</td>
            <td>{p.get('disease')}</td>
            <td>{p.get('doctor')}</td>
        </tr>
        """

    html += """
    </table>
    </body>
    </html>
    """
    return html

# -------------------------------------------------
# RUN SERVER
# -------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
