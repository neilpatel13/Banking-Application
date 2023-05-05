from datetime import datetime
from common.utils import Pagination
from sql.db import DB
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
import random
from accounts.forms import (AccountCreateForm,DepositForm,TransferForm,TransferToOtherUserForm,WithdrawalForm,)
accounts = Blueprint(
    "accounts", __name__, url_prefix="/accounts", template_folder="templates"
)
world_Account = "000000000000"
@accounts.route("/create_account", methods=["GET", "POST"])
@login_required
def create_account():
    form = AccountCreateForm()
    form.account_type.choices = (
        ("saving", "Saving Account"),
        ("credit", "Credit Account"),
        ("checking", "Checking Account"),
    )
    if request.method == "POST":
        if form.validate_on_submit():
            # Get account type and initial deposit from form
            account_type = form.account_type.data
            initial_deposit = form.initial_deposit.data

            # Generate random 12 digit account number that isn't previously used
            account_number = "".join([str(random.randint(0, 9)) for i in range(12)])
            try:
                result = DB.insertOne(
                    """INSERT INTO IS601_Accounts (account_number, account_type, balance, user_id) 
                    VALUES (%s, %s, %s, %s)""", account_number, account_type, initial_deposit, current_user.id,)
                # Create  transaction entries for the user initial deposit
                world_account = DB.selectOne("SELECT * FROM IS601_Accounts WHERE account_number=%s", world_Account).row
                
                user_account = DB.selectOne("SELECT * FROM IS601_Accounts WHERE account_number=%s", account_number ).row
                
                DB.insertOne("""
                INSERT INTO IS601_TransactionHistory (account_src, account_dest, balance_change, transaction_type, memo, 
                expected_total, created, modified)
                VALUES (%s, %s,%s, %s,%s, %s,%s, %s )""", world_account["id"], user_account["id"], -initial_deposit, "deposit", "Initial deposit to acc no " + account_number,
                world_account["balance"] - initial_deposit, datetime.utcnow(), datetime.utcnow())
                
                DB.insertOne("""INSERT INTO IS601_TransactionHistory (account_src, account_dest, balance_change, transaction_type, memo, expected_total, created, modified)
                VALUES (%s, %s,%s, %s,%s, %s,%s, %s )""",user_account["id"],world_account["id"],initial_deposit,"deposit","Initial deposit to acc no " + account_number,initial_deposit,datetime.utcnow(),datetime.utcnow())

                # update system account balance
                DB.update( """UPDATE IS601_Accounts SET balance = balance - %s  WHERE account_number = %s
                """, initial_deposit,world_Account)
                # Create new account and associate it with the current user
                if result.status:
                    flash("Account created successfully!", "success")
                    return redirect(url_for("home.index"))
            except Exception as e:
                flash("Account not created", "danger")
                print(e)
    return render_template("create_account.html", form=form)

@accounts.route("/my_account", methods=["GET", "POST"])
@login_required
def my_account():
    accounts = DB.selectAll("SELECT * FROM IS601_Accounts WHERE user_id=%s LIMIT 10", current_user.id).rows
    return render_template("my_account.html", accounts=accounts)


@accounts.route("/details/<account_number>")
@login_required
def account_details(account_number):
    # retrieve account details and transaction history
    account = DB.selectOne("SELECT * FROM IS601_Accounts WHERE account_number=%s",account_number).row
    transaction_history = DB.selectAll("""SELECT account_src, account_dest, balance_change, transaction_type, memo, expected_total, created 
                                        FROM IS601_TransactionHistory WHERE account_src=%s ORDER BY created DESC """,account["id"]).rows
    # Get filters from request parameters, if any
    transaction_type = request.args.get("type")
    start_date = request.args.get("from_date")
    end_date = request.args.get("to_date")
    page = int(request.args.get("page") or 1)

    # Filter Transactions
    if transaction_type:
        transaction_history = [hist for hist in transaction_history if hist["transaction_type"].lower() == transaction_type.lower()]

    if start_date and end_date:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        transaction_history = [ hist for hist in transaction_history if start_date <= hist["created"] <= end_date ]

    elif start_date:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        transaction_history = [hist for hist in transaction_history if start_date <= hist["created"]]

    elif end_date:
        transaction_history = [hist for hist in transaction_history if hist["created"] <= end_date]

    # render template with account details and transaction history
    return render_template("account_details.html",account_details=account,paginator=Pagination(transaction_history, page, 10))


@accounts.route("/withdraw", methods=["GET", "POST"])
@login_required
def withdraw():
    form = WithdrawalForm()
    # Populate the account choices for the form
    accounts = DB.selectAll("SELECT * FROM IS601_Accounts WHERE user_id=%s AND account_number!=%s", current_user.id, world_Account).rows
    
    form.account.choices = [(account["account_number"], account["account_number"]) for account in accounts]

    if request.method == "POST" and form.validate_on_submit():
        try:
            account_number = form.account.data
            amount = form.amount.data
            memo = form.memo.data

            # Retrieve the account and world account objects
            account = DB.selectOne("SELECT * FROM IS601_Accounts WHERE account_number=%s",account_number).row
            world_account = DB.selectOne("SELECT * FROM IS601_Accounts WHERE account_number=%s", world_Account).row

            # Check that the account has enough balance
            if account["balance"] < amount:
                flash(f"You Can Not Withdraw More Than Your Balance! Balance: ${account['balance']} ", "danger")
                #used flash message instead of forms message to show failure of withdraw.
                '''form.amount.errors.append(
                    f"You Can Not Withdraw More Than Your Balance. Your balance is {account['balance']} "
                )'''
                return render_template("withdraw.html", form=form)

            # Create the transaction pair
            DB.insertOne("""INSERT INTO IS601_TransactionHistory (account_src, account_dest, balance_change, transaction_type, memo, expected_total, created, modified)
                    VALUES (%s, %s,%s, %s,%s, %s,%s, %s ) """,account["id"], world_account["id"],-amount,"withdraw",memo,account["balance"] - amount, datetime.utcnow(), datetime.utcnow())
            
            DB.insertOne("""INSERT INTO IS601_TransactionHistory (account_src, account_dest, balance_change, transaction_type, memo, expected_total, created, modified)
                    VALUES (%s, %s,%s, %s,%s, %s,%s, %s )""", world_account["id"], account["id"], amount, "withdraw", memo, world_account["balance"] + amount, datetime.utcnow(), datetime.utcnow(),)

            # update  account balance
            # Since its a withdrawal, we increment world account balance and
            # decrease user account balance
            DB.update("""UPDATE IS601_Accounts SET balance = balance + %s WHERE account_number = %s""",amount, world_Account)
            DB.update("""UPDATE IS601_Accounts SET balance = balance - %s  WHERE account_number = %s """,amount,account_number)
            flash("Successful Withdrawal!", "success")
            return redirect(
                url_for("accounts.account_details", account_number=account_number)
            )
        except Exception as e:
            print(e)
            flash("Withdrawal was not successful!, try again", "danger")
    return render_template("withdraw.html", form=form)


@accounts.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    form = DepositForm()
    # Populate the account choices for the form
    accounts = DB.selectAll("SELECT * FROM IS601_Accounts WHERE user_id=%s AND account_number!=%s",  current_user.id, world_Account).rows
    
    form.account.choices = [(account["account_number"], account["account_number"]) for account in accounts]

    if request.method == "POST" and form.validate_on_submit():
        try:
            account_number = form.account.data
            amount = form.amount.data
            memo = form.memo.data

            # Retrieve the account and world account objects
            account = DB.selectOne("SELECT * FROM IS601_Accounts WHERE account_number=%s", account_number).row
            world_account = DB.selectOne("SELECT * FROM IS601_Accounts WHERE account_number=%s",world_Account ).row

            # Create the transaction pair
            DB.insertOne("""INSERT INTO IS601_TransactionHistory (account_src, account_dest, balance_change, transaction_type, memo, expected_total, created, modified)
                    VALUES (%s, %s,%s, %s,%s, %s,%s, %s )""", account["id"], world_account["id"], amount, "deposit", memo,account["balance"] + amount, datetime.utcnow(),datetime.utcnow())
            
            DB.insertOne("""INSERT INTO IS601_TransactionHistory (account_src, account_dest, balance_change, transaction_type, memo, expected_total, created, modified)
                    VALUES (%s, %s,%s, %s,%s, %s,%s, %s )""", world_account["id"], account["id"], -amount,"deposit", memo, world_account["balance"] - amount, datetime.utcnow(), datetime.utcnow())

            # update  account balance
            # Since its a deposital, we increment world account balance and
            # decrease user account balance
            DB.update( """UPDATE IS601_Accounts SET balance = balance - %s  WHERE account_number = %s """, amount, world_Account)
            DB.update("""UPDATE IS601_Accounts SET balance = balance + %s  WHERE account_number = %s """,amount,account_number)
            flash("Deposit was successfully!", "success")
            return redirect(url_for("accounts.account_details", account_number=account_number))
        except Exception as e:
            print(e)
            flash("Failed to deposit!", "danger")
    return render_template("deposit.html", form=form)


@accounts.route("/transfer/", methods=["GET", "POST"])
@login_required
def transfer():
    self_form = TransferForm()
    other_user_form = TransferToOtherUserForm()

    # Populate the account choices for the form
    accounts = DB.selectAll(
        "SELECT * FROM IS601_Accounts WHERE user_id=%s AND account_number!=%s",
        current_user.id,
        world_Account,
    ).rows
    self_form.src_account_number.choices = [
        (account["account_number"], account["account_number"]) for account in accounts
    ]
    self_form.dest_account_number.choices = [
        (account["account_number"], account["account_number"]) for account in accounts
    ]
    other_user_form.src_account_number.choices = [
        (account["account_number"], account["account_number"]) for account in accounts
    ]
    transfer_type = None
    if request.method == "POST":
        transfer_type = request.form.get("transfer-type")
        is_valid = (
            other_user_form.validate_on_submit()
            if transfer_type == "other"
            else self_form.validate_on_submit()
        )
        if is_valid:
            try:
                if transfer_type == "other":
                    src_account_number = other_user_form.src_account_number.data
                    # Get the destination account from the database
                    last_name = other_user_form.last_name.data
                    account_last4_dig = other_user_form.account_number_ending.data
                    account_to = DB.selectOne("""SELECT account_number FROM IS601_Accounts a JOIN IS601_Users u ON a.user_id = u.id WHERE u.lastname = %s AND a.account_number LIKE %s
                    """,last_name,"%%%%" + account_last4_dig )
                    if not account_to.row:
                        flash(f"Error for transfer for account ending '{account_last4_dig}' ","danger",)
                        return render_template("transfer.html", self_form=self_form, other_user_form=other_user_form,transfer_type=transfer_type)

                    dest_account_number = account_to.row["account_number"]
                    amount = other_user_form.amount.data
                    memo = other_user_form.memo.data

                else:
                    src_account_number = self_form.src_account_number.data
                    dest_account_number = self_form.dest_account_number.data
                    amount = self_form.amount.data
                    memo = self_form.memo.data
                    if src_account_number == dest_account_number:
                        form = other_user_form if transfer_type == "other" else self_form
                        flash("You cannot transfer money to the same account.", "danger")
                        return render_template("transfer.html",self_form=self_form,other_user_form=other_user_form,transfer_type=transfer_type )
                    
                # Retrieve the account and world account objects
                from_account = DB.selectOne("SELECT * FROM IS601_Accounts WHERE account_number=%s",src_account_number).row
                to_account = DB.selectOne("SELECT * FROM IS601_Accounts WHERE account_number=%s",dest_account_number).row

                # Check that the account has enough balance
                if from_account["balance"] < amount:
                    form = other_user_form if transfer_type == "other" else self_form
                    form.amount.errors.append(f"Error transfering money between accounts. You Can Not Transfer More Than Your Balance: ${from_account['balance']} ")
                    return render_template("transfer.html", self_form=self_form, other_user_form=other_user_form, transfer_type=transfer_type )

                # Create the transaction pair
                DB.insertOne("""
                            INSERT INTO IS601_TransactionHistory (account_src, account_dest, balance_change, transaction_type, memo, expected_total, created, modified)
                            VALUES (%s, %s,%s, %s,%s, %s,%s, %s )""",
                            from_account["id"], to_account["id"], -amount, "transfer", memo, from_account["balance"] - amount, datetime.utcnow(), datetime.utcnow())
                DB.insertOne("""
                            INSERT INTO IS601_TransactionHistory (account_src, account_dest, balance_change, transaction_type, memo, expected_total, created, modified)
                            VALUES (%s, %s,%s, %s,%s, %s,%s, %s )""",
                            to_account["id"], from_account["id"],amount, "transfer", memo, to_account["balance"] + amount, datetime.utcnow(),datetime.utcnow())

                # update  account balance
                # Since its a withdrawal, we increment world account balance and
                # decrease user account balance
                DB.update("""
                        UPDATE IS601_Accounts SET balance = balance + %s  WHERE account_number = %s """, amount, dest_account_number)
                DB.update(""" UPDATE IS601_Accounts SET balance = balance - %s WHERE account_number = %s """,amount,src_account_number)
                flash("Transfer was successfull!", "success")

                return redirect(url_for("accounts.my_account"))
            except Exception as e:
                print(e)
                flash("Transfer unsuccessfull, try again", "danger")

    return render_template("transfer.html", self_form=self_form, other_user_form=other_user_form, transfer_type=transfer_type)

