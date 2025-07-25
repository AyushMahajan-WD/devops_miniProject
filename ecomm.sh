#!/bin/bash

start_package() {
    sudo systemctl start $1
    sudo systemctl enable $1
}

sudo yum install httpd -y
start_package httpd

sudo yum install mariadb-server -y
start_package mariadb

sudo yum install php php-mysqlnd -y

sudo yum install git -y

sudo git clone https://github.com/kodekloudhub/learning-app-ecommerce

sudo cp -r learning-app-ecommerce/* /var/www/html

echo "CREATE DATABASE ecomdb;
CREATE USER 'ecomuser'@'localhost' IDENTIFIED BY 'ecompassword';
GRANT ALL PRIVILEGES ON *.* TO 'ecomuser'@'localhost';
FLUSH PRIVILEGES;" >> configure-db.sql

sudo mysql < configure-db.sql

echo "USE ecomdb;
CREATE TABLE products (
  id mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  Name varchar(255) DEFAULT NULL,
  Price decimal(10,2) DEFAULT NULL,
  ImageUrl varchar(255) DEFAULT NULL,
  PRIMARY KEY (id)
);
INSERT INTO products (Name, Price, ImageUrl) VALUES
  ('Laptop', 100, 'c-1.png'),
  ('Drone', 200, 'c-2.png'),
  ('VR', 300, 'c-3.png'),
  ('Tablet', 5, 'c-5.png'),
  ('Watch', 90, 'c-6.png'),
  ('Phone', 80, 'c-8.png'),
  ('Laptop', 150, 'c-4.png');" >> db-load-script.sql


sudo mysql < db-load-script.sql

sudo echo "DB_HOST=localhost
DB_USER=ecomuser
DB_PASSWORD=ecompassword
DB_NAME=ecomdb" >>  .env

sudo tee envfile <<'EOF'
<?php
// Function to load environment variables from a .env file
function loadEnv($path)
{
    if (!file_exists($path)) {
        return false;
    }

    $lines = file($path, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    foreach ($lines as $line) {
        if (strpos(trim($line), '#') === 0) {
            continue;
        }

        list($name, $value) = explode('=', $line, 2);
        $name = trim($name);
        $value = trim($value);
        putenv(sprintf('%s=%s', $name, $value));
    }
    return true;
}

// Load environment variables from .env file
loadEnv(__DIR__ . '/.env');

// Retrieve the database connection details from environment variables
$dbHost = getenv('DB_HOST');
$dbUser = getenv('DB_USER');
$dbPassword = getenv('DB_PASSWORD');
$dbName = getenv('DB_NAME');
?>
EOF

sudo sed -i '99r envfile' /var/www/html/index.php 

sudo cp .env /var/www/html

sudo sed -i 's/index.html/index.php/g' /etc/httpd/conf/httpd.conf

sudo chown -R apache:apache /var

sudo sed -i 's/172.20.1.101/localhost/g' /var/www/html/index.php

sudo systemctl restart httpd

echo -e "\e[35m___________________________Application Deployed Successfully!!!!!!!!!!!!!____________________________\e[0m"