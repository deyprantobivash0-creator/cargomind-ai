from flask import Flask, render_template, request

from backend.tools.shipment_tool import get_shipment
from backend.tools.message_parser import extract_shipment_id
from backend.tools.response_generator import generate_response
from backend.tools.ai_service import ask_ai

app = Flask(
    __name__,
    template_folder="frontend/templates"
)

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data["message"]

    shipment_id = extract_shipment_id(user_message)

    if shipment_id:

        shipment = get_shipment(shipment_id)

        if shipment:

            return {
                "reply": generate_response(shipment)
            }

    ai_reply = ask_ai(user_message)

    return {
        "reply": ai_reply
    }


if __name__=="__main__":
    app.run(debug=True)