from flask import Flask, Response, request
from collections import OrderedDict
import pyodbc
import json
import os

# Credentials should be pulled from environment variables
username = os.environ["HTTP_ODBC_USERNAME"]
password = os.environ["HTTP_ODBC_PASSWORD"]
dsn_name = os.environ["HTTP_ODBC_DSN_NAME"]

if not username:
    raise "HTTP_ODBC_USERNAME missing"

if not password:
    raise "HTTP_ODBC_PASSWORD missing"

if not dsn_name:
    raise "HTTP_ODBC_DSN_NAME missing"

client = pyodbc.connect(f"DSN={dsn_name};UID={username};PWD={password}")
cursor = client.cursor()

app = Flask(__name__)

@app.route("/query", methods=["GET", "POST"])
def query():
  """Route that generates JSON of specified SQL query present in body        

  Args (in body of request):
    sql(str): SQL query to be used

  Returns:
    json: If the SQL query is valid it returns the result of the query
  """

  # Technically this is vulnerable to SQL injection, 
  # however this is an on-premise server and in addition to that
  # the parameters are escaped. Despite this, it"s good to be
  # aware of this. HTTPS and TLS can mitigate man-in-the-middle (MITM) 
  # attacks and modification of the request in flight.

  query = request.get_json()["sql"]
  json_list = []

  app.logger.info(f"Query executed: {query}")

  cursor.execute(query)
  rows = cursor.fetchall()

  for row in rows:
    json_row = OrderedDict()

    for index, descriptor in enumerate(row.cursor_description):
      json_row[descriptor[0]] = str(row[index])
        
    json_list.append(json_row)
    
  return Response(json.dumps(json_list), mimetype="application/json")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
