@app.route("/login")
def login():
  username = request.values.get('username')
  password = "pass"
  db = pymysql.connect("localhost")

  
  cursor = db.cursor()
  print(username)
  # cursor.execute("SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password))
  # cursor.execute(f"SELECT admin FROM users WHERE username = '{username}'");
  record = cursor.fetchone()
  session['logged_user'] = username
  db.close()
