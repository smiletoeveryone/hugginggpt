from flask import Flask, render_template, request, jsonify
from text_image_speech import generate_text, generate_image, text_to_speech

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        generated_text = generate_text(prompt)
        image_base64 = generate_image(generated_text)
        speech_base64 = text_to_speech(generated_text)

        return jsonify(
            text=generated_text,
            image=f"data:image/png;base64,{image_base64}",
            speech=f"data:audio/mp3;base64,{speech_base64}",
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

