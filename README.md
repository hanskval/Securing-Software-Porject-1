# Testing the application
These instructions are for macOS/Linux operating systems.
- Clone the GitHub repository --> "git clone https://github.com/hanskval/Securing-Software-Porject-1.git"
- Navigate to the downloaded folder --> "cd Securing-Software-Porject-1"
- Create a Python virtual environment --> "python3 -m venv venv"
- Activate the virtual environment --> "source venv/bin/activate"
- Install the required Python libraries --> "pip install Flask" and "pip install python-dotenv" and "pip install pyopenssl"
- Copy .env.example to .env and set your own SECRET_KEY value --> 
  "cp .env.example .env"
  "python3 -c 'import secrets; print(secrets.token_hex(32))'"
  (paste the generated value into the SECRET_KEY line in the .env file)
- Create the required database using the schema.sql file --> "sqlite3 database.db < schema.sql"
- Start Flask --> "flask run --cert=adhoc"
- The website will then be available at the address shown in the terminal.
