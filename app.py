from flask import Flask

app = Flask(__name__)   # 👈 THIS must come before @app.route

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Ramya's App</title>
            <style>
                body {
                    background-color: black;
                    color: white;
                    text-align: center;
                    font-family: Arial;
                }
                h1 {
                    color: cyan;
                }
            </style>
        </head>
        <body>
            <h1>Ramya's Custom UI 🚀</h1>
            <p>Flask + CI Working Successfully!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)