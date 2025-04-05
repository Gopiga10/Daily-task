from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# Load stock data
df = pd.read_csv("data/stock_data.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

@app.route("/")
def index():
    # Create a stock price chart
    fig = px.line(df, x="date", y="close", title="Stock Price Over Time")

    # Convert to HTML
    graph_html = fig.to_html(full_html=False)

    return render_template("index.html", graph_html=graph_html)

if __name__ == "__main__":
    app.run(debug=True)
