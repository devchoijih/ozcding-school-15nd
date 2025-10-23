use testdatabase;

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    product_name VARCHAR(255),
    quantity INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
