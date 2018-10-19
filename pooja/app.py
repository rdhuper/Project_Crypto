
# Import dependencies
import pandas as pd
from sqlalchemy import create_engine
from config import sqlpw
import decimal
from flask import Flask, jsonify
import flask.json
from time import strptime, strftime

# Import PyMySQL (Not needed if mysqlclient is installed)
import pymysql
pymysql.install_as_MySQLdb()


class MyJSONEncoder(flask.json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances to strings.
            return str(obj)
        return super(MyJSONEncoder, self).default(obj)

# Connect to database
connection_string = f"root:{sqlpw}@localhost/crypto_db"
engine = create_engine(f"mysql://{connection_string}")

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.json_encoder = MyJSONEncoder

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (f"<p>Hi There!<p><br/>"
        f"Welcome to <b>Project Crypto</b><br/><br/>"
        f"Available Routes:<br/>"
        f"To look at the jsonified data go here:<a href=\"#\"> /api/v1.0/data</a><br/>"
        f"To look at the stats for a particular period go here: <a href=\"#\">/&lt;start_date&gt;/&lt;end_date&gt;</a>"
    )


@app.route("/api/v1.0/data")
def coindata():
    # Perform a query to retrieve the data for bitcoin and ethereum
    result = engine.execute("SELECT bitcoin.date \"Date\", btc_close \"BitcoinClose\", eth_close \"EthereumClose\" FROM bitcoin INNER JOIN ethereum USING(date);")

    all_data = []
    # Create a dictionary from the row data and append to a list of all_data    
    for row in result:
        row_dict = {}
        row_dict["Date"] = row.Date
        row_dict["Bitcoin Close"] = row.BitcoinClose
        row_dict["Ethereum Close"] = row.EthereumClose
        all_data.append(row_dict)
    return jsonify(all_data)

@app.route("/api/v1.0/<start_date>/<end_date>")
def coinstats(start_date,end_date):
    # Perform a query to retrieve the data for bitcoin and ethereum
    result = engine.execute(f"SELECT avg(btc_close) \"BitcoinAvg\", avg(eth_close) \"EthereumAvg\", max(btc_close) \"BitcoinMax\", max(eth_close) \"EthereumMax\", min(btc_close) \"BitcoinMin\", min(eth_close) \"EthereumMin\" FROM bitcoin INNER JOIN ethereum USING(date) WHERE date>='{start_date}' and date<='{end_date}';")

    # Create a dictionary from the row data and append to a list of all_passengers
    all_data = []
    
    for row in result:
        row_dict = {}
        row_dict["Bitcoin Minimum"] = row.BitcoinMin
        row_dict["Bitcoin Maximum"] = row.BitcoinMax
        row_dict["Bitcoin Average"] = row.BitcoinAvg
        row_dict["Ethereum Minimum"] = row.EthereumMin
        row_dict["Ethereum Maximum"] = row.EthereumMax
        row_dict["Ethereum Average"] = row.EthereumAvg
        all_data.append(row_dict)

    return jsonify(all_data)

if __name__ == '__main__':
    app.run(debug=True)
