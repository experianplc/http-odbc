from waitress import serve
import app
import os 

try:
    port = os.environ["HTTP_ODBC_PORT"]
except:
    port = 8005

serve(app.app, host="0.0.0.0", port=port)
