DeveloperMail python wrapper based on official documentation https://www.developermail.com/api/v1/

### Install

```python
pip install devmail
```

### Usage

```python
> from devmail import DevMail
> mailbox = DevMail.create()
> print(mailbox.username)
> print(mailbox.token)
```



TBD:

1. Send mail
2. Delete mail
3. Empty mailbox
4. Save credentials
5. Refactor code