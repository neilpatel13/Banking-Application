import re
from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')

@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    query = """SELECT IS601_MP3_Employees.id as id, IS601_MP3_Employees.first_name, IS601_MP3_Employees.last_name, 
            IS601_MP3_Employees.email, IS601_MP3_Employees.company_id, IS601_MP3_Companies.name as company_name
            FROM IS601_MP3_Employees 
            LEFT JOIN IS601_MP3_Companies 
            ON IS601_MP3_Employees.company_id = IS601_MP3_Companies.id WHERE 1=1"""

    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    fn = request.args.get('first_name')
    ln = request.args.get('last_name')
    email = request.args.get('email')
    company = request.args.get('company_id')
    column = request.args.get('column')
    order = request.args.get('order')
    limit = request.args.get('limit', '10')
    # TODO search-3 append like filter for first_name if provided  #NeilPatel UCID: NP656 DATE: 4/15
    if fn:
        query += " AND IS601_MP3_Employees.first_name LIKE %(fn)s"
        args['fn'] = f"%{fn}%"
    # TODO search-4 append like filter for last_name if provided  #NeilPatel UCID: NP656 DATE: 4/15
    if ln:
        query += " AND IS601_MP3_Employees.last_name LIKE %(ln)s"
        args['ln'] = f"%{ln}%"
    # TODO search-5 append like filter for email if provided  #NeilPatel UCID: NP656 DATE: 4/15
    if email:
        query += " AND IS601_MP3_Employees.email LIKE %(email)s"
        args['email'] = f"%{email}%"
    # TODO search-6 append equality filter for company_id if provided  #NeilPatel UCID: NP656 DATE: 4/15
    if company:
        query += " AND IS601_MP3_Employees.company_id = %(company)s"
        args['company'] = company
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if column and column in allowed_columns and order in ['asc', 'desc']:
        query += f" ORDER BY {column} {order}"
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    try:
        limit = int(limit)
        if limit < 1 or limit > 100:
            raise ValueError
    except ValueError:
        limit = 10
        flash('Invalid limit. Limit must be a number between 1 and 100.', 'error')
    else:
        query += f" LIMIT {limit}"
    args['limit'] = limit
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
            print(f"rows {rows}")
    except Exception as e:
        # TODO search-10 make message user friendly
        flash(e, "error")
        flash("Error has occured, try again later", "warning")
        print(e)
#Neil Patel UCID: NP656, DOC: 4/23

    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    column_choices = [(col, col.capitalize()) for col in allowed_columns]  #NeilPatel UCID: NP656 DATE: 4/15
    return render_template("list_employees.html", rows=rows, column_choices=column_choices)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        fn = request.form.get("first_name")
        ln = request.form.get("last_name")
        company = request.args.get('company_id' )
        email = request.form.get("email")
        
        # TODO add-2 first_name is required (flash proper error message)
        if not fn:
            flash("First name is required", "danger")
            has_error = True
        
        # TODO add-3 last_name is required (flash proper error message)
        if not ln:
            flash("Last name is required", "danger")
            has_error = True
        
        # TODO add-4 company (may be None)
        if not company:
            company = None
        
        # TODO add-5 email is required (flash proper error message)
        if not email:
            flash("Email is required", "danger")
            has_error = True
        else:
            # TODO add-5a verify email is in the correct format
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                flash("Invalid email format", "danger")
                has_error = True
        
        has_error = False # use this to control whether or not an insert occurs
        if not has_error:
            try:
                result = DB.insertOne("""
                    INSERT INTO IS601_MP3_Employees (first_name, last_name, company_id, email)
                    VALUES (%s, %s, %s, %s)
                    """,fn, ln, company, email) # <-- TODO add-6 add query and add arguments
                if result.status:
                    flash("Created Employee Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                flash(str(e), "danger")
                print(e)
                flash("Invalid", "danger")

    return render_template("add_employee.html")


@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    if not id:
        flash("Employee ID is required", "danger")
    else:
        if request.method == "POST":
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            company = request.form.get("company_id")
            email = request.form.get("email")
            # TODO edit-2 first_name is required (flash proper error message)
            if not first_name:
                flash("First name is required", "danger")
                has_error = True
            else:
                has_error = False

            # TODO edit-3 last_name is required (flash proper error message)
            if not last_name:
                flash("Last name is required", "danger")

            # TODO edit-4 company (may be None)
            if not company:
                company = None

            # TODO edit-5 email is required (flash proper error message)
            # TODO edit-5a verify email is in the correct format
            if not email:
                flash("Email is required", "danger")
                has_error = True
            else:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    flash("Invalid email format", "danger")
                    has_error = True
                else:
                    has_error = False
            has_error = False # use this to control whether or not an insert occurs
                
            if not has_error:
                try:
                    # TODO edit-6 fill in proper update query
                    result = DB.update("""
                    UPDATE IS601_MP3_Employees SET first_name = %s, last_name = %s, company_id = %s, email = %s
                    WHERE id = %s """, first_name, last_name, company, email, id)
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    flash("Error, try again later", "danger")
                    flash(e, "danger")
                    print(e)
        row = {}
        try:
            # TODO edit-8 fetch the updated data 
            result = DB.selectOne("""
        SELECT IS601_MP3_Employees.id, first_name, last_name, email, company_id
        FROM IS601_MP3_Employees 
        LEFT JOIN IS601_MP3_Companies ON IS601_MP3_Employees.company_id = IS601_MP3_Employees.company_id
        WHERE IS601_MP3_Employees.id = %s
        """, id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash("Error", "danger")
            flash(str(e), "danger")
            print(e)

    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", employee=row)

@employee.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    try:
        if not id:
            # TODO delete-4 ensure a flash message shows for successful delete
            # TODO delete-5 if id is missing, flash necessary message and redirect to search
            flash("Employee ID is missing.", "danger")
            return redirect(url_for("employee.search"))

        # TODO delete-1 delete employee by id
        result = DB.delete("DELETE FROM IS601_MP3_Employees WHERE IS601_MP3_Employees.id = %s", id)
        if result.status:
            flash("Employee deleted successfully", "success")
            # TODO delete-2 redirect to employee search
            return redirect(url_for("employee.search"))

    except Exception as e:
        flash(str(e), "danger")
        print(e)

    # TODO delete-3 pass all argument except id to this route
