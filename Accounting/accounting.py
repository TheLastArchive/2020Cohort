import sys

if __name__ == '__main__':

    import user.authentication

    import transactions.journal

    from banking.fvb import reconciliation

    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)): print(sys.argv[i])

    user.authentication.authenticate_user()
    transactions.journal.receive_income(100)
    transactions.journal.pay_expense(100)
    reconciliation.do_reconciliation()
