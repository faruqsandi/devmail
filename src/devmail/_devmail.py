import requests


class DevMail:

    def __init__(self):
        self.username = None
        self.token = None
        self.last_success = None
        self.last_errors = None
        self.last_result = None
        self.raw = None
        self.mailsid = None
        self.mails = None

    def create(self, force=False):
        headers = {
            'accept': 'application/json',
        }

        if self.username:
            pass
        else:
            self.response = requests.put(
                'https://www.developermail.com/api/v1/mailbox', headers=headers)
            self.response = self.response.json()
            self.last_success = self.response['success']
            self.last_errors = self.response['errors']
            self.last_result = self.response['result']
            self.username = self.response['result']['name']
            self.token = self.response['result']['token']

        return self.last_success

    def destroy(self):
        headers = {
            'accept': 'application/json',
            'X-MailboxToken': self.token,
        }
        self.response = requests.delete(
            f'https://www.developermail.com/api/v1/mailbox/{self.username}', headers=headers)
        self.response = self.response.json()
        self.last_success = self.response['success']
        self.last_errors = self.response['errors']
        self.last_result = self.response['result']
        self.username = None
        self.token = None
        return self.last_success

    def newtoken(self):
        headers = {
            'accept': 'application/json',
            'X-MailboxToken': self.token,
        }
        self.response = requests.put(
            f'https://www.developermail.com/api/v1/mailbox/{self.username}/token', headers=headers)
        self.response = self.response.json()
        self.last_success = self.response['success']
        self.last_errors = self.response['errors']
        self.last_result = self.response['result']
        self.token = self.response['result']['token']
        return self.last_success

    def getmailid(self):
        headers = {
            'accept': 'application/json',
            'X-MailboxToken': self.token,
        }

        self.response = requests.get(
            f'https://www.developermail.com/api/v1/mailbox/{self.username}', headers=headers)
        self.response = self.response.json()
        self.last_success = self.response['success']
        self.last_errors = self.response['errors']
        self.last_result = self.response['result']
        self.mailsid = self.response['result']
        return self.last_success

    def getmail(self, mailid: list = None):
        headers = {
            'accept': 'application/json',
            'X-MailboxToken': self.token,
            'Content-Type': 'application/json',
        }

        if mailid is None:
            mail_list = self.mailsid

        data = str(mail_list)

        self.response = requests.post(
            f'https://www.developermail.com/api/v1/mailbox/{self.username}/messages', headers=headers, data=data)
        self.response = self.response.json()
        self.last_success = self.response['success']
        self.last_errors = self.response['errors']
        self.last_result = self.response['result']
        self.mails = self.response['result']
        return self.last_success
