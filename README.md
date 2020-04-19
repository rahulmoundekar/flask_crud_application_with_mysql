# Flask CURD Application SqlAlchemy and MySQL :

 In Python, packages such as Flask are available in a public repository, from where anybody can download them and install them.
    
# What is SqlAlchemy?
SQLAlchemy is a popular SQL toolkit and Object Relational Mapper. It is written in Python and gives full power and flexibility of SQL to an application developer. It is an open source and cross-platform software released under MIT license.

SQLAlchemy is famous for its object-relational mapper (ORM), using which, classes can be mapped to the database, thereby allowing the object model and database schema to develop in a cleanly decoupled way from the beginning.


# Project Setup

  - Making the project as :
     ```
        mkdir flask_crud_application_with_mysql
		cd flask_crud_application_with_mysql
    ```
  - Install flask:
    ```
        pip install flask
    ```
 - Integrating SqlAlchemy
    ```
      pip install sqlalchemy
    ```
 - Create EmployeeManagementSystem.py for development    
 - Add 'SqlAlchemy configuration' to EmployeeManagementSystem.py as:
    ```
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flaskapp'
    db = SQLAlchemy(app)
    ```
 - Declaring Models:
     ```
     class Employee(db.Model):
         id = db.Column(db.Integer, primary_key=True)
         name = db.Column(db.String(80), nullable=False)
         email = db.Column(db.String(20), nullable=False)
         contact = db.Column(db.String(12), nullable=False)
    ```
 - Make a runserver configuration
     ``` 
    app = Flask(__name__)
    
    if __name__ == "__main__":
        app.run(debug=True)
    ```
 - create html file inside templates folder
    * check project directory for index.html file
    
 - create curd def in EmployeeManagementSystem.py
    ``` 
      @app.route("/", methods=['GET', 'POST'])
      @app.route("/<int:employee_id>", methods=['GET'])
        def employeeHome(employee_id=None):
            if request.method == 'POST':
                eid = request.form.get('id')
                name = request.form.get('name')
                email = request.form.get('email')
                contact = request.form.get('contact')
                if eid:  # if id present update records
                    employee = Employee.query.filter_by(id=eid).first()
                    employee.name = name
                    employee.email = email
                    employee.contact = contact
                    db.session.commit()
                else:
                    # id not None save record
                    entry = Employee(name=name, contact=contact, email=email)
                    db.session.add(entry)
                    db.session.commit()
            employee = None
            if employee_id:  # load record form edit form data
                employee = Employee.query.filter_by(id=employee_id).first()
        
            employees = Employee.query.all()  # get list of records
            return render_template('index.html', employees=employees, employee=employee)
    
    
        @app.route("/delete/<int:employee_id>", methods=['GET'])
        def deleteEmployee(employee_id):
            employee = Employee.query.filter_by(id=employee_id).first()
            db.session.delete(employee)
            db.session.commit()
            return redirect("/")
      ``` 
 - In order to run app:
      ```
	python EmployeeManagementSystem.py
      ```

 - run on your browser
    * Your should run at: http://127.0.0.1:5000/
