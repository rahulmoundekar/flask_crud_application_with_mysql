from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flaskapp'
db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    contact = db.Column(db.String(12), nullable=False)


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


if __name__ == "__main__":
    app.run(debug=True)
