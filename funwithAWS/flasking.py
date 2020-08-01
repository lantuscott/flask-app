from flask import Flask, jsonify, request
import pyodbc, pandas as pd

app = Flask(__name__)

# connection object which will contain SQL Server Connection
connect = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.1.189;DATABASE=stuff;UID=sa;PWD=40634630Leo*")
cursor = connect.cursor()

@app.route('/')
def hello():
    return 'hello world!'

@app.route('/getDB', methods=['GET'])
def connect_to_DB():

    df = pd.read_sql("SELECT * FROM dbo.ForecastWeekFour", connect)
    response = df.to_dict(orient='records')
    return jsonify(response), 200

@app.route('/filter', methods=['POST'])
def filter_data():
    payload = request.get_json()
    query=("SELECT * "
           "FROM dbo.ForecastWeekFour "
           f"WHERE {payload['filter']}='{payload['value']}'")

    df=pd.read_sql(query,connect)
    response=df.to_dict(orient='records')
    return jsonify(response),200

if __name__ == '__main__':
    app.run(debug=True)
