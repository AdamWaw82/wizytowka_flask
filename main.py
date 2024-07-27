from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__)

    @app.route("/mypage/me")
    def me():
        return render_template("me.html")

    @app.route("/mypage/contact", methods=['GET', 'POST'])
    def contact():
        if request.method == "POST":
            print(f"Otrzymałeś wiadomość o treści: {request.form.get('wiadomosc')}")
        return render_template("contact.html")

    return app



if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)