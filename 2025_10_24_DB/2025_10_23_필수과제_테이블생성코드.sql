CREATE TABLE Customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(30),
    email VARCHAR(100)
);

CREATE TABLE Pet (
    pet_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    pet_name VARCHAR(100),
    species VARCHAR(50),
    breed VARCHAR(100),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Room (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_name VARCHAR(50),
    room_type VARCHAR(50),
    price_per_night DECIMAL(10,2)
);

CREATE TABLE Reservation (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    pet_id INT,
    room_id INT,
    checkin_date DATE,
    checkout_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (pet_id) REFERENCES Pet(pet_id),
    FOREIGN KEY (room_id) REFERENCES Room(room_id)
);

CREATE TABLE Service (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    reservation_id INT,
    service_name VARCHAR(100),
    price DECIMAL(10,2),
    FOREIGN KEY (reservation_id) REFERENCES Reservation(reservation_id)
);