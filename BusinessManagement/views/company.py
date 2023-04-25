from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import pycountry
import traceback
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search(): #NeilPatel UCID: NP656 DATE: 4/14
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    # don't do SELECT *    
    query = """
            SELECT IS601_MP3_Companies.id, IS601_MP3_Companies.name, IS601_MP3_Companies.address, IS601_MP3_Companies.city, 
                IS601_MP3_Companies.country, IS601_MP3_Companies.state, IS601_MP3_Companies.zip, IS601_MP3_Companies.website,
                (SELECT COUNT(IS601_MP3_Employees.id) FROM IS601_MP3_Employees WHERE IS601_MP3_Employees.company_id = IS601_MP3_Companies.id) AS employees 
            FROM IS601_MP3_Companies 
            WHERE 1=1 
            """
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    # TODO search-2 get name, country, state, column, order, limit request args
    name = request.args.get('name')
    country = request.args.get('country')
    state = request.args.get('state')
    column = request.args.get('column')
    order = request.args.get('order')
    limit = request.args.get('limit', 10)
    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += "AND IS601_MP3_Companies.name LIKE %(name)s "
        args['name'] = f"%{name}%"
    # TODO search-4 append an equality filter for country if provided
    if country:
        query += "AND IS601_MP3_Companies.country = %(country)s "
        args['country'] = country
    # TODO search-5 append an equality filter for state if provided
    if state:
        query += "AND IS601_MP3_Companies.state = %(state)s "
        args['state'] = state
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    if column and column in allowed_columns and order in ['asc', 'desc']:
        query += f" ORDER BY {column} {order}"
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
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


#Neil Patel, UCID: NP656 DOC 4/15
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
#Neil Patel, UCID: NP656 DOC 4/15

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
        #Neil Patel, UCID: NP656 DOC 4/15

        if not state:
            flash("Please provide a state.", "danger")
            has_error = True
        else:
            try:
                subdivisions = pycountry.subdivisions.get(country_code=country)
                valid_states = [subdivision.code.split('-')[1] for subdivision in subdivisions]
                if state not in valid_states:
                    flash("Please provide a valid state.", "danger")
                    has_error = True
            except KeyError as e:
                print("error")
                print(e)
                flash("Error with states", "danger")
                has_error = True
#Neil Patel, UCID: NP656 DOC 4/15

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
#Neil Patel, UCID: NP656 DOC 4/15

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
                INSERT INTO IS601_MP3_Companies (name, address, city, state, country, zip, website)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, name, address, city, state, country, zip_code, website) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash("Error has occured, try again later", "warning")
                traceback.print_exc()
                print(e)
                flash(str(e), "danger")

        #Neil Patel, UCID: NP656 DOC 4/15

    return render_template("add_company.html")







#Neil Patel, UCID: NP656 DOC 4/15


@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    if not id:
        flash("ID is required", "danger")
    else:
        if request.method == "POST":
            data = {"id": id} # use this as needed, can convert to tuple if necessary
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            name = request.form.get("name")
            address = request.form.get("address")
            city = request.form.get("city")
            state = request.form.get("state")
            country = request.form.get("country")
            zip_code = request.form.get("zip")
            website = request.form.get("website")
            # TODO edit-2 name is required (flash proper error message)
            if not name:
                flash("Name is required", "danger")
                has_error = True
            # TODO edit-3 address is required (flash proper error message)
            if not address:
                flash("Address is required", "danger")
                has_error = True
            # TODO edit-4 city is required (flash proper error message)
            if not city:
                flash("City is required", "danger")
                has_error = True
            # TODO edit-5 state is required (flash proper error message)
            # TODO edit-5a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            if not state:
                flash("Please provide a state.", "danger")
                has_error = True
                #Neil Patel, UCID: NP656 DOC 4/15

            else:
                try:
                    subdivisions = pycountry.subdivisions.get(country_code=country)
                    valid_states = [subdivision.code.split('-')[1] for subdivision in subdivisions]
                    if state not in valid_states:
                        flash("Please provide a valid state.", "danger")
                        has_error = True
                except KeyError as e:
                    print("error")
                    print(e)
                    flash("Error with states", "danger")
                    has_error = True
            # TODO edit-6 country is required (flash proper error message)
            # TODO edit-6a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            if not country:
                flash("Please provide a country.", "danger")
                has_error = True
                #Neil Patel, UCID: NP656 DOC 4/15

            else:
                try:
                    pycountry.countries.get(alpha_2=country)
                except KeyError:
                    flash("Please provide a valid country.", "danger")
                    has_error = True
            # TODO edit-7 website is not required
            # TODO edit-8 zipcode is required (flash proper error message)
            if not zip_code:
                flash("Please provide a zip code.", "danger")
                has_error = True
            has_error = False # use this to control whether or not an insert occurs
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings
            data["name"] = name
            data["address"] = address
            data["city"] = city
            data["state"] = state
            data["country"] = country
            data["zip"] = zip_code
            data["website"] = website
#Neil Patel, UCID: NP656 DOC 4/15

            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    # name, address, city, state, country, zip, website
                    result = DB.update("""
                    UPDATE IS601_MP3_Companies
                    SET name=%s, address=%s, city=%s, state=%s, country=%s, zip=%s, website=%s
                    WHERE id=%s """, name, address, city, state, country, zip_code, website, id)
                    if result.status:
                        print("updated record")
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    print(f"{e}")
                    flash(str(e), "danger")
                    flash("Error has occured, try again later, error")
        #Neil Patel, UCID: NP656 DOC 4/15

        row = {}
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("""
                    SELECT id, name, address, city, state, country, zip, website
                    FROM IS601_MP3_Companies
                    WHERE id=%s 
                    """, id)
            if result.status:
                row = result.row
                
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash(str(e), "danger")
            flash("Error has occured, try again later, error")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", company=row)

#Neil Patel, UCID: NP656 DOC 4/15




#Neil Patel, UCID: NP656 DOC 4/15


@company.route("/company/delete/<int:id>", methods=["GET"])
def delete(id):
    try:
        if not id:
            # TODO delete-6 if id is missing, flash necessary message and redirect to search
            flash("Invalid or missing company ID", "danger")
            return redirect(url_for('company.search'))
        # TODO delete-5 set company_id to None/null for all employees assigned to this company
        result = DB.update("""
            UPDATE IS601_MP3_Employees SET IS601_MP3_Employees.company_id = NULL WHERE IS601_MP3_Employees.company_id = %s
        """, id)
        if result.status:
            print("unallocated employees")
        #Neil Patel, UCID: NP656 DOC 4/15

        # TODO delete-1 delete company by id (unallocate any employees see delete-5)
        result = DB.delete("DELETE FROM IS601_MP3_Companies WHERE id = %s", id)
        if result.status:
            print("deleted company")
            # TODO delete-4 show success flash message
            flash("Company deleted successfully", "success")
    except Exception as e:
        # TODO delete-7 make error message user-friendly
        print(f"{e}")
        flash(str(e), "danger")
        flash("Error has occured, try again later", "warning")
    # TODO delete-2 redirect to company search
    return redirect(url_for('company.search'))
#Neil Patel, UCID: NP656 DOC 4/15

    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 for all employees assigned to this company set their company_id to None/null
    