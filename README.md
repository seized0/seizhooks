# Seizhooks
 https://pypi.org/project/seizhooks
 https://discord.gg/wyUuYr9DEN
 https://github.com/seized0/seizhooks

 Seizhooks is a simple lib using discord api to interact with webhook
 Made by uhq.s

# REQUIREMENTS 

pip install requests
pip install colorama

# USING

# DELETE WEBHOOK

```python

webhook = seizhooks.Hook(webhook='YOUR WEBHOOK URL')

webhook.Delete()

```
# SEND A MESSAGE WITH WEBHOOK

```python

webhook = seizhooks.Hook(webhook='YOUR WEBHOOK URL')

webhook.SendMessage(message='TEXT',name='webhook name',avatar='avatar url')
or
webhook.SendMessage(message='TEXT',name=None,avatar=None)


```

Made with ❤️
By uhq.s

