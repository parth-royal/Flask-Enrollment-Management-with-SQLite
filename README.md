## Flask Enrollment Management with SQLite

This code implements a Flask application for managing enrollments using an SQLite database. It demonstrates the use of SQLAlchemy for interacting with the database and defines routes for adding enrollments.

### Project Structure

The project contains the following files:

* **`app.py`:** The main Flask application code, handling routing, form processing, and database interactions.
* **`database.db`:**  The SQLite database file, which will be created automatically when the application starts.

### Functionality

1. **Database Setup:**
    * The code defines three SQLAlchemy models: `Student`, `Course`, and `Enrollment`. These models represent the database tables and their relationships.
    * The `db.create_all()` function creates the database tables based on the models.
2. **Routes:**
    * `/`: The home route serves an HTML form to add enrollments.
    * `/enrollments`: Handles POST requests to add new enrollments.
3. **Form Processing:**
    * The `/enrollments` route receives POST requests containing form data for the enrollment.
    * It parses the form data, creates an `Enrollment` object, and saves it to the database.

### Running the Application

1. **Install Dependencies:**
    * Make sure you have Python and Flask installed.
    * Install Flask-SQLAlchemy: `pip install Flask-SQLAlchemy`
2. **Run the Application:** Execute `python app.py` to start the Flask application.
3. **Access the Application:** Open a web browser and navigate to `http://127.0.0.1:5000/` to see the enrollment form.

### Considerations

* **Data Persistence:**  The application stores enrollment data in the SQLite database file (`database.db`), making the data persistent.
* **ORM (Object-Relational Mapping):**  SQLAlchemy provides an object-oriented way to interact with the database, making it easier to work with data.
* **Form Handling:**  The application uses Flask's built-in form handling to process form data.
* **HTML Template:**  Consider using a more comprehensive HTML template to provide a user-friendly interface.
* **Additional Routes:**  Implement additional routes for retrieving, updating, and deleting enrollments.
* **Security:**  Add security measures to protect the database and the application.

### Further Development

* **Improve HTML:**  Create a more user-friendly HTML template with a table to display existing enrollments.
* **Add CRUD Operations:** Implement routes for getting, updating, and deleting enrollments.
* **Database Migration:** Use `Flask-Migrate` to manage database schema changes.
* **User Authentication:** Implement user login to restrict access to the enrollment management features.

This README provides a basic overview of the project. Further documentation for specific functionalities or additional features can be added as needed. 

