from flask import Flask, json, request, jsonify, render_template
from flask_mysqldb import MySQL, MySQLdb
from collections import Counter

# from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)
# cors = CORS(app, resources={r"/foo": {"origins": "*"}})

app.secret_key = 'nono'

app.config['MYSQL_HOST'] = "103.153.141.22"
app.config['MYSQL_USER'] = "pyspark"
app.config['MYSQL_PASSWORD'] = "P@ssw0rd"
app.config['MYSQL_DB'] = "fk"
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JSON_AS_ASCII'] = False

mysql = MySQL(app)
counter = Counter()

@app.route('/')
# @cross_origin(origin='*',headers=['Content-Type','Authorization'])
def index():
   cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
   curr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
   cur.execute("SELECT * FROM links")
   curr.execute("SELECT * FROM nodes")
   rv = cur.fetchall()
   rb = curr.fetchall()
   links = []
   nodes = []
   content = []
   cont = []
   for result in rv:
       cont = {'source': result['source'], 'target':result['target'], 'type':result['type']}
       data = (cont)
       links.append(data)
       data = {}
   for resultt in rb:
       content = {'id': resultt['id'], 'name': resultt['name']}
       dataa = content
       nodes.append(dataa)
       dataa = {}
   aa = ({'nodes':nodes, 'links': links})
   response = (jsonify(aa))
   response.headers.add('Access-Control-Allow-Origin', '*')
   return response
if __name__ == '__main__':
    app.run(debug=True)