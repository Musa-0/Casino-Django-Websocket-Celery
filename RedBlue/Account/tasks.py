import asyncio
import datetime
from Account.models import CodeVerefication
from RedBlue.celery import app


@app.task
def clear_verifications_code():
    code_accounts = CodeVerefication.objects.all()
    for account in code_accounts:
        if((account.datetime + datetime.timedelta(minutes=10)).timestamp()<datetime.datetime.now().timestamp()):
            account.user.delete()