DeveloperMail python wrapper based on official documentation https://www.developermail.com/api/v1/

### Install

```python
pip install devmail
```

### Usage

###### Creating mailbox

```python
>>> from devmail import DevMail
>>> mailbox = DevMail()
>>> mailbox.create()
{'username': 'z-werhj4', 'token': 'B1DC9D1D6C9C1519728C4056F545EA0288946D54'}
```

###### Create new token

```python
>>> mailbox.newtoken()
{'username': 'z-werhj4', 'token': 'DC7F2CD7C195E66F637123A34D3D2A57FF0A18A0'}
```

###### Get message ids

In this example, I send two message to `z-werhj4@developermail.com` from my real email.

```python
>>> mailbox.getmailids()
['637553086207559378', '637553086352838482']
```

The email id is a timestamp.

###### Get messages from list of id

```python
>>> mails = mailbox.getmails(['637553086207559378', '637553086352838482'])
>>> len(mails)
2
>>> mails[0]
{'key': '637553086207559378', 'value': 'DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=yahoo.co.id; s=s2048; t=1619711818; bh=ffhpeYB/ObY5N0hGrQtyxG3MKCJQBhB7v8HKMpfmOjU=; h=Date:From:Reply-To:To:Subject:References:From:Subject:Reply-To; b=E2 TRUNCATED}
```

It will return list of `{'key': mail id, 'value': raw mail content}`. If `mailids`  list is not supplied, it will return all email available after `mailbox.getmailids()`.

###### Get a message

```python
>>> mail = mailbox.getmail('637553086207559378', raw=True)
>>> mail
'DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=yahoo.co.id; s=s2048; t=1619711818; bh=ffhpeYB/ObY5N0hGrQtyxG3MKCJQBhB7v8HKMpfmOjU=; h=Date:From:Reply-To:To:Subject:References:From:Subject:Reply-To; b=E20 TRUNCATED'
```

Note: `raw` parameter is not useful now. I will improve the email parsing it in the future.

###### Delete a message

```python
>>> mailbox.delmail('637553086207559378')
{'success': True, 'errors': None, 'result': True}
>>> mailbox.getmail('637553086207559378', raw=True) # return None
>>> mailbox.getmailids()
['637553086352838482']
```

TBD:

3. Empty mailbox
2. Convert timestamp to Date Time
3. Save credentials
4. Refactor code