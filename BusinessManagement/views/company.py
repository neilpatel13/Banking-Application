from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import pycountry
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search(): #NeilPatel UCID: NP656 DATE: 4/14
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    # don't do SELECT *    
    query = """SELECT IS601_MP3_Companies.id, IS601_MP3_Companies.name, IS601_MP3_Companies.address, IS601_MP3_Companies.city, IS601_MP3_Companies.country, IS601_MP3_Companies.state, IS601_MP3_Companies.zip, IS601_MP3_Companies.website, 
            COUNT(employee.id) as employees FROM IS601_MP3_Companies company LEFT JOIN employee IS601_MP3_Employees ON IS601_MP3_Companies.id = IS601_MP3_Employees.company_id WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    # TODO search-2 get name, country, state, column, order, limit request args
    name = request.args.get('name')
    country = request.args.get('country')
    state = request.args.get('state')
    column = request.args.get('column')
    order = request.args.get('order')
    limit = request.args.get('limit', 10)
 #NeilPatel UCID: NP656 DATE: 4/14
    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += " AND c.name LIKE %(name)s"
        args['name'] = f"%{name}%"
    # TODO search-4 append an equality filter for country if provided
     #NeilPatel UCID: NP656 DATE: 4/14
    if country:
        query += " AND c.country = %(country)s"
        args['country'] = country
    # TODO search-5 append an equality filter for state if provided
     #NeilPatel UCID: NP656 DATE: 4/14
    if state:
        query += " AND c.state = %(state)s"
        args['state'] = state
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
     #NeilPatel UCID: NP656 DATE: 4/14
    if column and column in allowed_columns and order in ['asc', 'desc']:
        query += f" ORDER BY {column} {order}"
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    try:
        limit = int(limit)
        if limit < 1 or limit > 100:
            raise ValueError
    except ValueError:
        limit = 10
        flash('Invalid limit. Limit must be a number between 1 and 100.', 'error')
    else:
        query += f" LIMIT {limit}"
 #NeilPatel UCID: NP656 DATE: 4/14
    args["limit"] = limit
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        #print(f"result {result.rows}")
        if result.status:
            rows = result.rows
            print(f"rows {rows}")
    except Exception as e:
        # TODO search-9 make message user friendly
        flash(str(e), "danger")
        flash("Error has occured, try again later", "warning")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
     #NeilPatel UCID: NP656 DATE: 4/15
    column_choices = [(col, col.capitalize()) for col in allowed_columns]
    return render_template("list_companies.html", rows=rows, column_choices=column_choices)

@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zip_code = request.form.get("zip")
        website = request.form.get("website")
        # TODO add-2 name is required (flash proper error message)
        if not name:
            flash("Name is required.", "danger")
            has_error = True
        # TODO add-3 address is required (flash proper error message)
        if not address:
            has_error = True
            flash("Address is required.", "danger")
        # TODO add-4 city is required (flash proper error message)
        if not city:
            has_error = True
            flash("City is required.", "danger")
        # TODO add-5 state is required (flash proper error message)
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation
        if not state:
            flash("Please provide a state.", "danger")
            has_error = True
        else:
            try:
                subdivisions = pycountry.subdivisions.get(country_code=country)
                valid_states = [subdivision.code for subdivision in subdivisions]
                if state not in valid_states:
                    flash("Please provide a valid state.", "danger")
                    has_error = True
            except KeyError:
                flash("Please provide a valid country.", "danger")
                has_error = True
        # TODO add-6 country is required (flash proper error message)
        # TODO add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation
        if not country:
            flash("Please provide a country.", "danger")
            has_error = True
        else:
            try:
                pycountry.countries.get(alpha_2=country)
            except KeyError:
                flash("Please provide a valid country.", "danger")
                has_error = True

        if not zip_code:
            flash("Please provide a zip code.", "danger")
            has_error = True
        # TODO add-7 website is not required
        # TODO add-8 zipcode is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        has_error = False # use this to control whether or not an insert occurs
        

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO companies (name, address, city, state, country, zip, website)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (name, address, city, state, country, zip_code, website)) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash("Error has occured, try again later", "warning")
                flash(str(e), "danger")
        
    return render_template("add_company.html")

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = False
    if not id: # TODO update this for TODO edit-1
        pass
    else:
        if request.method == "POST":
            data = {"id": id} # use this as needed, can convert to tuple if necessary
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            # TODO edit-2 name is required (flash proper error message)
            # TODO edit-3 address is required (flash proper error message)
            # TODO edit-4 city is required (flash proper error message)
            # TODO edit-5 state is required (flash proper error message)
            # TODO edit-5a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            # TODO edit-6 country is required (flash proper error message)
            # TODO edit-6a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            # TODO edit-7 website is not required
            # TODO edit-8 zipcode is required (flash proper error message)
            
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings
            has_error = False # use this to control whether or not an insert occurs

            
            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    # name, address, city, state, country, zip, website
                    result = DB.update("""
                    UPDATE ...
                    SET
                    ...
                    """, data)
                    if result.status:
                        print("updated record")
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    print(f"{e}")
                    flash(str(e), "danger")
        row = {}
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("SELECT ... FROM ... WHERE ...", id)
            if result.status:
                row = result.row
                
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash(str(e), "danger")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", ...)

@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete company by id (unallocate any employees see delete-5)
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 for all employees assigned to this company set their company_id to None/null
    # TODO delete-6 if id is missing, flash necessary message and redirect to search
    pass
    