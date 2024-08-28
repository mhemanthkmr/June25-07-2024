from flask import Flask, render_template, request, redirect, url_for, session
from controller import getData, addData, changeData, removeData
from dbService import createConnection, executeQuery, closeConnection
from rich import print

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management

# Dummy data for user authentication
users = {
    'admin': 'password123',
    'user1': 'mypassword',
    # Add more users if needed
}

@app.route('/getData', methods=['GET'])
def fetchData():
    response = getData()
    return render_template('for.html', result=response)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        
        # Create database connection
        db_Conn = createConnection()
        cursor = db_Conn.cursor(dictionary=True)
        
        # Query to check if the username and password match
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        executeQuery(query, cursor)
        account = cursor.fetchone()
        
        # Close the cursor and connection
        closeConnection(cursor)
        db_Conn.close()

        # If account exists, set up the session
        if account:
            session['loggedin'] = True
            session['username'] = username
            msg = 'Logged in successfully!'
            return redirect(url_for('fetchData'))  # Redirect to getData page after login
        else:
            msg = 'Incorrect username or password!'

    return render_template('login.html', msg=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        # Create database connection
        db_Conn = createConnection()
        cursor = db_Conn.cursor()

        # Check if the username already exists
        query_check = f"SELECT * FROM users WHERE username = '{username}'"
        executeQuery(query_check, cursor)
        account = cursor.fetchone()

        if account:
            msg = 'Username already exists!'
        else:
            # Insert new user into the users table
            query_insert = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
            executeQuery(query_insert, cursor)
            msg = 'You have successfully registered!'

            return redirect(url_for('login'))  # Redirect to login page after successful registration

        # Close the cursor and connection
        closeConnection(cursor)
        db_Conn.close()

    return render_template('register.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/createData', methods=['POST'])
def createData():
    body = request.get_json()
    print(body)
    addData(body=body)
    responseBody = {
        "message": "Record Inserted Successfully",
        "status": 200
    }
    return responseBody

@app.route('/updateData', methods=['POST'])
def updateData():
    body = request.get_json()
    print(body)
    changeData(body=body)
    responseBody = {
        "message": "Record Updated Successfully",
        "status": 200
    }
    return responseBody

@app.route('/deleteData', methods=['POST'])
def deleteData():
    body = request.get_json()
    print(body)
    removeData(body=body)
    responseBody = {
        "message": "Record Deleted Successfully",
        "status": 200
    }
    return responseBody

if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")
