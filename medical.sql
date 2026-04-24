CREATE DATABASE clinic_db;
USE clinic_db;

-- PATIENT
CREATE TABLE patient_info (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    phone VARCHAR(15),
    spouse_name VARCHAR(100),
    address VARCHAR(255)
);

-- DOCTOR
CREATE TABLE doctor_info (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    specialization VARCHAR(100),
    available_days VARCHAR(50),
    available_time VARCHAR(50)
);

-- APPOINTMENT
CREATE TABLE appointment_info (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    date DATE,
    time_slot VARCHAR(20),
    FOREIGN KEY (patient_id) REFERENCES patient_info(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctor_info(doctor_id)
);

-- SAMPLE DATA
INSERT INTO doctor_info (name, specialization, available_days, available_time) VALUES
('Dr. Sharma','Cardiologist','Mon,Wed,Fri','10AM-2PM'),
('Dr. Verma','Dermatologist','Tue,Thu','12PM-4PM'),
('Dr. Singh','General Physician','Mon,Tue,Wed,Thu,Fri,Sat','9AM-1PM');

-- VIEW
CREATE VIEW appointment_view AS
SELECT p.name AS patient, d.name AS doctor, a.date, a.time_slot
FROM appointment_info a
JOIN patient_info p ON a.patient_id = p.patient_id
JOIN doctor_info d ON a.doctor_id = d.doctor_id;

-- STORED PROCEDURE
DELIMITER //
CREATE PROCEDURE getDoctorAppointments(IN doc_id INT)
BEGIN
    SELECT * FROM appointment_info WHERE doctor_id = doc_id;
END //
DELIMITER ;

-- TRIGGER
DELIMITER //
CREATE TRIGGER prevent_duplicate
BEFORE INSERT ON appointment_info
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT 1 FROM appointment_info
        WHERE doctor_id = NEW.doctor_id
        AND date = NEW.date
        AND time_slot = NEW.time_slot
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Slot already booked!';
    END IF;
END //
DELIMITER ;