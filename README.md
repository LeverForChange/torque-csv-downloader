# Torque/Global View Proposal Downloader

This package will download all data from Global View. Edit the `args.json` file with your API credentials, desired fields, and excluded competitions. For convenience, I would recommend creating an `args.local.json` file, which is already ignored by git, in which you can store your sensitive username/api-key for Torque. __Absolutely do not push a commit wth your Torque username or API key.__

For convenvience, a list of available fields can be printed using the `getAvailableFields.py` file. Note that some fields are competition specific and may not appear in the resulting CSV if a requested field does not exist for the set of competitions downloaded.
