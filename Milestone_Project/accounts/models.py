from common.utils import JsonSerializable
from sql.db import DB
#Neil Patel UCID: NP656 DOC: 5/3

class Account(JsonSerializable):
    def __init__(self, id = -1, balance = 0):
        self.id = id
        self.balance = balance
    def add_points(self, change = 0, from_acct = -1, transaction_type="", memo = ""):
        return self.__Change__Points(from_acct, self.id, change, transaction_type, memo)
    def _Remove__Points(self, change = 0, to_acct = -1, transaction_type="", memo=""):
        return self.__Change__Points(self.id, to_acct, change, transaction_type, memo)
    def __Change__Points(self, account_src, account_dest, change, transaction_type, memo):
        DB.getDB().autocommit = False
        if change > 0:
            # first of the pair should be negative
            change *= -1
        query = """INSERT INTO FROM IS601_TransactionHistory (account_src, account_dest, balance_change, transaction_type, memo) VALUES (%s, %s, %s, %s, %s)"""
        pairs = []
        pairs.append((account_src, account_dest, change, transaction_type, memo))
        pairs.append((account_dest, account_src, change * -1, transaction_type, memo))
        try:#Neil Patel UCID: NP656 DOC: 5/3

            result = DB.insertMany(query, pairs)
            if result.status:
                print("Recored transations pairs", account_src, account_src, change, transaction_type, memo)
                if self.__update__balance():
                    DB.getDB().commit()
                    return True
        except Exception as e:
            print("Error recording point history", e)
            DB.getDB().rollback()
        return False
    def __update__balance(self):
        from sql.db import DB
        try:#Neil Patel UCID: NP656 DOC: 5/5

            result = DB.update("""UPDATE IS601_Accounts set balance = (SELECT IFNULL(SUM(balance_change), 0) FROM IS601_TransactionHistory WHERE account_src = %(acct)s)WHERE id = %(acct)s
            """, {"acct":int(self.id)})
            if result.status:
                result = DB.selectOne("SELECT balance FROM IS601_Accounts WHERE id = %s", self.id)
                if result.status and result.row:
                    self.balance = result.row["balance"]
                    from flask import session
                    from flask_login import current_user
                    session["user"] = current_user.toJson()
                    return True
        except Exception as e:
            print("Error updating balance", e)
            DB.getDB().rollback()
        return False
    #Neil Patel UCID: NP656 DOC: 5/3
