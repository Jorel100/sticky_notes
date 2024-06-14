
### Step 15: Investigate Django Database Migrations to MariaDB

#### Setting Up MariaDB with Django

1. **Install MariaDB**:
   ```bash
   sudo apt-get update
   sudo apt-get install mariadb-server
   sudo mysql_secure_installation

2. # Create a Database and User

CREATE DATABASE sticky_notes_db;
CREATE USER 'sticky_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON sticky_notes_db.* TO 'sticky_user'@'localhost';
FLUSH PRIVILEGES;

3. # Configure Django to Use MariaDB

pip install mysqlclient

# Edit 'settings.py'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sticky_notes_db',
        'USER': 'sticky_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

4. # Run Migrations

python manage.py makemigrations
python manage.py migrate








