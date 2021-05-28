DeveloperMail python wrapper based on official documentation https://www.developermail.com/api/v1/

## Install

```python
pip install devmail
```

## Usage

### Create mailbox

```python
>>> from devmail import DevMail
>>> mailbox = DevMail()
>>> mailbox.create()
{'username': 'z-pypjq7', 'token': 'AD5002F7F660C2D61A91B5F1DCABF0819E2F79D4'}
```

### Create new token

```python
>>> mailbox.newtoken()
{'username': 'z-pypjq7', 'token': 'FA3CEC39B32E03DD6E5011FE4B1A4FCA7EC9C28A'}
```

### Send a message

```python
>>> mail = {'subject': 'Hello!', 'body': 'There!', 'isHtml': False}
>>> mailbox.sendmail(mail)
{'success': True, 'errors': None, 'result': True}
```

### Send another message

```python
>>> mail = {'subject': 'Hello!', 'body': 'Again!', 'isHtml': False}
>>> mailbox.sendmail(mail)
{'success': True, 'errors': None, 'result': True}
```

### Get message IDs

```python
>>> mailbox.getmailids()
['637578381535439379', '637578381749371824']
```

The email id is a unix timestamp.

### Get messages from list of id

```python
>>> mails = mailbox.getmails(['637578381535439379', '637578381749371824'], raw=False)
>>> len(mails)
2
>>> mails[0]
{'key': '637578381535439379', 'value': {'MIME-Version': '1.0', 'From': 'z-pypjq7@developermail.com', 'To': 'z-pypjq7@developermail.com', 'Date': '28 May 2021 22:35:53 +0000', 'Subject': 'Hello!', 'Content-Type': 'text/plain; charset=us-ascii', 'Content-Transfer-Encoding': 'quoted-printable'}}
```

It will return list of `{'key': mail id, 'value': parsed mail content}`. If `mailids` list is not supplied, it will return all emails available after the last call to `mailbox.getmailids()`. This method parses raw email content by default. To disable this behaviour, set `raw=True`.

### Get a single message

```python
>>> mail = mailbox.getmail('637578381749371824')
>>> mail
{'MIME-Version': '1.0', 'From': 'z-pypjq7@developermail.com', 'To': 'z-pypjq7@developermail.com', 'Date': '28 May 2021 22:36:14 +0000', 'Subject': 'Hello!', 'Content-Type': 'text/plain; charset=us-ascii', 'Content-Transfer-Encoding': 'quoted-printable'}
```

### Delete a message

```python
>>> mailbox.delmail('637578381535439379')
{'success': True, 'errors': None, 'result': True}
>>> mailbox.getmail('637578381535439379', raw=True) # return None
>>> mailbox.getmailids()
['637578381749371824']
```

TBD:

3. Empty mailbox
2. Convert timestamp to Date Time
3. Save credentials
4. Refactor code