from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime

app = Flask(__name__)
DATA_FILE = "data.json"

# Function untuk load/save data (sama seperti storage.py)
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Halaman utama - list semua expenses
@app.route("/")
def index():
    data = load_data()
    return render_template("index.html", expenses=data)

# Add expense
@app.route("/add", methods=["POST"])
def add():
    data = load_data()
    expense = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": request.form["category"],
        "amount": float(request.form["amount"]),
        "description": request.form["description"]
    }
    data.append(expense)
    save_data(data)
    return redirect(url_for("index"))

# Delete expense
@app.route("/delete/<int:index>")
def delete(index):
    data = load_data()
    if 0 <= index < len(data):
        data.pop(index)
        save_data(data)
    return redirect(url_for("index"))

# Edit expense
@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    data = load_data()
    if request.method == "POST":
        e = data[index]
        e['category'] = request.form['category']
        e['amount'] = float(request.form['amount'])
        e['description'] = request.form['description']
        save_data(data)
        return redirect(url_for("index"))
    return render_template("edit.html", expense=data[index], index=index)

# Category summary
@app.route("/summary")
def summary():
    data = load_data()
    summary = {}
    for e in data:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]
    return render_template("summary.html", summary=summary)

if __name__ == "__main__":
    app.run()
