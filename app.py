import re, html
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)   # lets your React app call this API

clf = pipeline("text-classification", model="stress_model_final", tokenizer="stress_model_final")

def light_clean(t):   # same cleaning as training
    t = html.unescape(str(t))
    t = re.sub(r"[\u200B\u200C\u200D\uFEFF]", "", t)
    t = re.sub(r"https?://\S+|www\.\S+", " URL ", t)
    t = re.sub(r"@\w+|\bu/\w+", " USER ", t)
    return re.sub(r"\s+", " ", t).strip()

@app.route("/predict", methods=["POST"])
def predict():
    text = light_clean((request.json or {}).get("text", ""))
    if len(text) < 20:
        return jsonify({"error": "Please write at least a couple of sentences."}), 400

    r = clf(text, truncation=True, max_length=128)[0]
    stressed = r["label"] == "LABEL_1"
    conf = r["score"] if stressed else r["score"]   # confidence in the predicted label
    return jsonify({"stressed": stressed, "confidence": round(conf, 3)})

if __name__ == "__main__":
    app.run(port=5000)