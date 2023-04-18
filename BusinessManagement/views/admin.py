import io
import csv
from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from sql.db import DB
import traceback
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/import", methods=["GET","POST"])
def importCSV():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file', "warning")
            return redirect(request.url)
        filename_parts = file.filename.split('.')
        if filename_parts[-1].lower() != 'csv':
            flash('Invalid file type, please upload a CSV file.', "warning")
            return redirect(request.url)        
        if file and secure_filename(file.filename):
            companies = []
            employees = []
            # DON'T EDIT
            company_query = """
            INSERT INTO IS601_MP3_Companies (name, address, city, country, state, zip, website)
                        VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s)
                        ON DUPLICATE KEY UPDATE 
                        address=values(address),
                        city=values(city),
                        country=values(country),
                        state=values(state),
                        zip=values(zip),
                        website=values(website)
            """
            # DON'T EDIT
            employee_query = """
             INSERT INTO IS601_MP3_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, (SELECT id FROM IS601_MP3_Companies WHERE name = %(company_name)s LIMIT 1))
                        ON DUPLICATE KEY UPDATE first_name=%(first_name)s, 
                        last_name = %(last_name)s, email = %(email)s, 
                        company_id = (SELECT id FROM IS601_MP3_Companies WHERE name=%(company_name)s LIMIT 1)
            """
            # Note: this reads the file as a stream instead of requiring us to save it
            # TODO importcsv-2 read the csv file stream as a dict 
            stream = io.TextIOWrapper(file.stream._file, "UTF8", newline=None)
            csv_reader = csv.DictReader(stream)
            for row in csv_reader:
                company = {
                    'name': row.get("name"),
                    'address': row.get("address"),
                    'city': row.get("city"),
                    'state': row.get("state"),
                    'zip': row.get("zip"),
                    'country': row.get("country"),
                    'website':row.get("website")
                }
                
                if None not in company.values():
                    companies.append(company)
                # todo remove 
                # print(row) #example
                # TODO importcsv-3 extract company data and append to company list 
                # as a dict only with company data if all is present
                
                # TODO importcsv-4 extract employee data and append to employee list 
                # as a dict only with employee data if all is present
                employee = {
                    'first_name': row.get("first_name"),
                    'last_name': row.get("last_name"),
                    'email': row.get("email"),
                    'company_name': row.get("company_name")
                }

                if None not in employee.values():
                    employees.append(employee)
               
            if len(companies) > 0:
                print(f"Inserting or updating {len(companies)} companies")
                try:
                    result = DB.insertMany(company_query, companies)
                    flash(f"{len(companies)} companies loaded successfully.", "success")
                except Exception as e:
                    traceback.print_exc()
                    print(e)
                    flash("There was an error loading in the csv data", "danger")
            
            else:
                traceback.print_exc()
                print("error")
                flash("No companies were loaded.", "info")
            
            if len(employees) > 0:
                print(f"Inserting or updating {len(employees)} employees")
                try:
                    result = DB.insertMany(employee_query, employees)
                    flash(f"{len(employees)} employees loaded successfully.", "success")
                except Exception as e:
                    traceback.print_exc()
                    print(e)
                    flash("There was an error loading in the csv data", "info")
            else:
                traceback.print_exc()
                flash("No employees were loaded", "warning")
            try:
                result = DB.selectOne("SHOW SESSION STATUS LIKE 'questions'")
                print(f"Result {result}")
            except Exception as e:
                traceback.print_exc()
                print(e)
                flash("There was an error counting session queries", "danger")
    return render_template("upload.html")
