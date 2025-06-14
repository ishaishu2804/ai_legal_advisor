from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load law data
with open("law_data.json") as f:
    law_data = json.load(f)

# Simple matching function
def find_matching_section(user_input):
    user_input = user_input.lower()
    for law in law_data:
        for keyword in law['keywords']:
            if keyword.lower() in user_input:
                return law
    return None

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        query = request.form["query"]
        match = find_matching_section(query)
        if match:            
            result = f"<strong>{match['section']}:</strong> {match['title']}<br><br>" \
                     f"<strong>What you can do:</strong> {match['procedure']}"

        else:
            result = "Sorry, no matching legal section found."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
