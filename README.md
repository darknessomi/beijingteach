# beijingteach
BEIJING TEACH

### run it!
The simplest way to load this site for local development.

Use heroku sdk, the [Heroku Toolbelt](https://toolbelt.heroku.com/)!

After install, go with this:

```
virtualenv venv
source venv/bin/activate
python manage.py migrate
python manage.py init_data
heroku local
```

For more help please read [heroku python doc](https://devcenter.heroku.com/articles/getting-started-with-python).
