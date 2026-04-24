# 🏥 Medical Appointment System (DBMS Project)

## 📌 Project Overview

This project is a **Web-Based Medical Appointment System** developed using **Flask (Python) and MySQL**.
It allows users to book, view, and delete appointments while ensuring proper database management and avoiding conflicts.

---

## 🚀 Features

* 📝 Book Appointment
* ❌ Prevent Duplicate Time Slot Booking
* 🗑️ Delete Appointment
* 📊 Doctor-wise Appointment Count (GROUP BY)
* 📋 View All Appointments (JOIN)
* 🧠 Strong DBMS Concepts Implementation

---

## 🛠️ Technologies Used

* **Backend:** Flask (Python)
* **Database:** MySQL
* **Frontend:** HTML
* **Connector:** mysql-connector-python

---

## 🗄️ Database Structure

### Tables:

* `patient_info`
* `doctor_info`
* `appointment_info`

### Relationships:

* One patient → multiple appointments
* One doctor → multiple appointments

---

## 🔥 Advanced SQL Used

* **JOIN** → Combine multiple tables
* **GROUP BY** → Doctor-wise appointment count
* **VIEW** → Simplified data access
* **TRIGGER** → Prevent duplicate booking
* **STORED PROCEDURE** → Fetch doctor appointments

---

## ▶️ How to Run the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Setup Database

* Open MySQL
* Run the SQL script provided in the project

### 3. Run Application

```bash
python app.py
```

### 4. Open in Browser

```
http://127.0.0.1:5000
```

---

## 📊 Key Functionalities

* Users can book appointments by selecting doctor, date, and time slot
* System prevents duplicate slot booking
* Admin can delete appointments using appointment ID
* System shows doctor-wise appointment statistics

---

## 🎯 Learning Outcomes

* Practical implementation of DBMS concepts
* Real-world database design
* Integration of backend with database
* CRUD operations with validation

---

## ⚠️ Limitations

* No authentication system
* Basic UI (no styling)
* SMS/OTP system not implemented

---

## 🔮 Future Enhancements

* 🔐 Login/Signup system
* 📱 SMS/OTP integration
* 🎨 Advanced UI (Bootstrap)
* 🌐 Deployment on cloud

---

## 👨‍💻 Author

Developed as a **DBMS Project** for academic purpose.
