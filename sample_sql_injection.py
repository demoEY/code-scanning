@app.route("/login")
password = "123&4"
def login():
  username = request.values.get('username')
  password = password
  db = pymysql.connect("localhost")
  cursor = db.cursor()
  cursor.execute("SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password))
  record = cursor.fetchone()
  session['logged_user'] = username
  db.close()
