from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    query = """SELECT IS601_MP3_Employees.id, IS601_MP3_Employees.first_name, IS601_MP3_Employees.last_name, IS601_MP3_Employees.email, IS601_MP3_Employees.company_id, IS601_MP3_Companies.name AS company_name
               FROM IS601_MP3_Employees employees LEFT JOIN companies IS601_MP3_Companies ON IS601_MP3_Employees.company_id = IS601_MP3_Companies.id WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    fn = request.args.get('fn', '')
    ln = request.args.get('ln', '')
    email = request.args.get('email', '')
    company = request.args.get('company', '')
    column = request.args.get('column', '')
    order = request.args.get('order', '')
    limit = request.args.get('limit', '10')
    # TODO search-3 append like filter for first_name if provided  #NeilPatel UCID: NP656 DATE: 4/15
    if fn:
        query += " AND e.first_name LIKE %(fn)s"
        args['fn'] = f"%{fn}%"
    # TODO search-4 append like filter for last_name if provided  #NeilPatel UCID: NP656 DATE: 4/15
    if ln:
        query += " AND e.last_name LIKE %(ln)s"
        args['ln'] = f"%{ln}%"
    # TODO search-5 append like filter for email if provided  #NeilPatel UCID: NP656 DATE: 4/15
    if email:
        query += " AND e.email LIKE %(email)s"
        args['email'] = f"%{email}%"
    # TODO search-6 append equality filter for company_id if provided  #NeilPatel UCID: NP656 DATE: 4/15
    if company:
        query += " AND e.company_id = %(company)s"
        args['company'] = company
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if column and order and column in allowed_columns and order in ['asc', 'desc']:
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
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    column_choices = [(col, col.capitalize()) for col in allowed_columns]  #NeilPatel UCID: NP656 DATE: 4/15
    return render_template("list_employees.html", rows=rows, column_choices=column_choices)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        # TODO add-2 first_name is required (flash proper error message)
        # TODO add-3 last_name is required (flash proper error message)
        # TODO add-4 company (may be None)
        # TODO add-5 email is required (flash proper error message)
        # TODO add-5a verify email is in the correct format
        has_error = False # use this to control whether or not an insert occurs
            
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO ...
                """, ...
                ) # <-- TODO add-6 add query and add arguments
                if result.status:
                    flash("Created Employee Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                flash(str(e), "danger")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = False
    if not id: # TODO update this for TODO edit-1
        pass
    else:
        if request.method == "POST":
            
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            # TODO edit-2 first_name is required (flash proper error message)
            # TODO edit-3 last_name is required (flash proper error message)
            # TODO edit-4 company (may be None)
            # TODO edit-5 email is required (flash proper error message)
            # TODO edit-5a verify email is in the correct format
            has_error = False # use this to control whether or not an insert occurs

            
                
            if not has_error:
                try:
                    # TODO edit-6 fill in proper update query
                    result = DB.update("""
                    UPDATE ... SET
                    ...
                    """, ...)
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    flash(e, "danger")
        row = {}
        try:
            # TODO edit-8 fetch the updated data 
            result = DB.selectOne("""SELECT 
            ...
            FROM ... LEFT JOIN ... 
              
              WHERE ..."""
            , id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash(str(e), "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", ...)

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 if id is missing, flash necessary message and redirect to search
    pass