from flask_wtf import FlaskForm
from flask_login import UserMixin
from wtforms import StringField, DecimalField, SubmitField, SelectField, DateTimeField
from wtforms.validators import InputRequired, DataRequired, ValidationError, NumberRange, Length
#Neil Patel UCID: NP656 DOC: 5/3

class AccountCreateForm(FlaskForm):
    account_type = StringField("Account Type", validators=[InputRequired()])
    initial_deposit = DecimalField(
        "Initial deposit", validators=[InputRequired(), NumberRange(min=5)], default=5
    )
    submit = SubmitField("Create account")
#Neil Patel UCID: NP656 DOC: 5/3
#creating the withdraw form for the banking project
class WithdrawalForm(FlaskForm):
    account = SelectField("Account Number", [DataRequired()])
    amount = DecimalField("Amount", [DataRequired(), NumberRange(min=1)])
    memo = StringField("Memo")
    submit = SubmitField("Withdraw")
#Neil Patel UCID: NP656 DOC: 5/3
class TransferForm(FlaskForm):
    src_account_number = SelectField("Source Account Number", [DataRequired()])
    dest_account_number = SelectField("Destination Account Number", [DataRequired()])
    amount = DecimalField("Amount", [DataRequired(), NumberRange(min=1)])
    memo = StringField("Memo")
    submit = SubmitField("Transfer")



#Neil Patel UCID: NP656 DOC: 5/3
class DepositForm(FlaskForm):
    account = SelectField("Account Number", [DataRequired()])
    amount = DecimalField("Amount", [DataRequired(), NumberRange(min=1)])
    memo = StringField("Memo")
    submit = SubmitField("Deposit")


#creating the deposit form for the banking project




class TransferToOtherUserForm(FlaskForm):
    src_account_number = SelectField("From Account", validators=[InputRequired()])
    last_name = StringField("Last Name of Recepient User", validators=[InputRequired()])
    account_number_ending = StringField(
        "Last 4 Digits of Recepient Account Number",
        validators=[InputRequired(), Length(min=4, max=4)],
    )#Neil Patel UCID: NP656 DOC: 5/3
    amount = DecimalField("Amount", validators=[InputRequired(), NumberRange(min=1)])
    memo = StringField("Memo")
    submit = SubmitField("Transfer")#Neil Patel UCID: NP656 DOC: 5/3

    #creating the transfer form for the banking project
