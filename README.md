# Ghana360
This is a telegram bot, that delivers up date posts on news as it happens.

## Coverage In Ghana

Ghana news sources: Citi Fm, Joy News, GBC Ghana.
Subscribe to the channel https://t.me/ghana360


## Run

Set up your Telegram and Twitter Keys in the `settings.py`

## Deploy to Heroku
With heroku, you would have to deploy this as a worker(script). This is not a web app!

    `worker: python app.py`

Add the above to the heroku `Procfile`

    `heroku ps:scale worker=1 --app=app-name'

Now your app should be running.

TODO:
- Add Sqlalchemy and Sqlite and store the news for 48hrs
- Check for duplicated new Items
- Truncate table after 24hrs