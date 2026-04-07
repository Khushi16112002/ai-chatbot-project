from flask import Flask, render_template, request

app = Flask(__name__)

def chatbot_response(message):
    message = message.lower()

    if "hello" in message:
        return "Hi! Welcome to our service 😊"
    elif "website" in message:
        return "We create professional websites for businesses."
    elif "logo" in message:
        return "We design creative logos for your brand."
    elif "price" in message:
        return "Prices depend on your requirement. Contact us!"
    elif "contact" in message:
        return "You can contact us at +91 XXXXXXXX"
    elif "bye" in message:
        return "Thank you! Have a great day ❤️"
    else:
        return "I can help with services, pricing, and contact info."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]
    return chatbot_response(user_text)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=10000)

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/chat")
def chat():
    return render_template("index.html")
