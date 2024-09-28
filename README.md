Travel Booking System API
This is a RESTful API built using Flask for managing a Travel Booking System. The API allows users to register, log in, view available flights, book flights, and cancel bookings

Features
User Registration & Authentication: Users can register and log in.
Flight Management: View available flights.
Booking Management: Book flights and cancel bookings.
Secure Endpoints: Uses JWT for securing API endpoints.
Technologies
Programming Language: Python
Framework: Flask
Database: SQLite (can be changed to PostgreSQL or MySQL)
Authentication: Flask-JWT-Extended
Object Relational Mapper (ORM): SQLAlchemy
Database Migrations: Flask-Migrate

Database Models
User: Stores user information, including id, username, and password_hash.
Flight: Stores flight information, including id, origin, destination, departure_time, and arrival_time.
Booking: Stores booking details, including id, user_id, flight_id, and booking_date.
How to Use
Start by registering a new user through the /register endpoint.
Log in to get a JWT token, which you will need to include in the headers for protected routes.
View available flights, book a flight, and cancel bookings as needed.
