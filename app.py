from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    experience = float(request.form["experience"])

    prediction = model.predict([[experience]])

    return render_template("index.html",
                           prediction_text=f"Predicted Salary: {prediction[0]}")

if __name__ == "__main__":
    app.run(debug=True)
