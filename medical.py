from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Mohit2006",
    database="clinic_db"
)
cursor = db.cursor()

# -------- HOME -------- #
@app.route('/')
def home():
    cursor.execute("SELECT * FROM doctor_info")
    doctors = cursor.fetchall()

    # Doctor count
    cursor.execute("""
        SELECT d.name, COUNT(a.appointment_id)
        FROM doctor_info d
        LEFT JOIN appointment_info a
        ON d.doctor_id = a.doctor_id
        GROUP BY d.name
    """)
    counts = cursor.fetchall()

    return render_template('index.html', doctors=doctors, counts=counts)

# -------- BOOK -------- #
@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    phone = request.form['phone']
    spouse = request.form['spouse']
    address = request.form['address']
    doctor_id = request.form['doctor']
    date = request.form['date']
    slot = request.form['slot']

    # Check duplicate slot
    cursor.execute("""
        SELECT * FROM appointment_info
        WHERE doctor_id=%s AND date=%s AND time_slot=%s
    """,(doctor_id, date, slot))

    if cursor.fetchone():
        return "❌ Slot already booked!"

    # Insert patient
    cursor.execute("""
        INSERT INTO patient_info (name, age, gender, phone, spouse_name, address)
        VALUES (%s,%s,%s,%s,%s,%s)
    """,(name, age, gender, phone, spouse, address))
    db.commit()

    cursor.execute("SELECT LAST_INSERT_ID()")
    pid = cursor.fetchone()[0]

    # Insert appointment
    cursor.execute("""
        INSERT INTO appointment_info (patient_id, doctor_id, date, time_slot)
        VALUES (%s,%s,%s,%s)
    """,(pid, doctor_id, date, slot))
    db.commit()

    return "✅ Appointment Booked!"

# -------- DELETE -------- #
@app.route('/delete', methods=['POST'])
def delete():
    appointment_id = request.form['appointment_id']

    cursor.execute("DELETE FROM appointment_info WHERE appointment_id=%s",(appointment_id,))
    db.commit()

    return "🗑️ Appointment Deleted!"

# -------- VIEW ALL -------- #
@app.route('/view')
def view():
    cursor.execute("""
        SELECT a.appointment_id, p.name, d.name, a.date, a.time_slot
        FROM appointment_info a
        JOIN patient_info p ON a.patient_id = p.patient_id
        JOIN doctor_info d ON a.doctor_id = d.doctor_id
    """)
    data = cursor.fetchall()

    return render_template('index.html', data=data)

app.run(debug=True)