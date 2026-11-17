
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>VR GADGET</title>
        <style>
            body {
                background: #050b18;
                color: white;
                font-family: Arial;
                text-align: center;
                margin: 0;
            }

            header {
                background: #081426;
                padding: 25px;
                border-bottom: 2px solid #00d9ff;
            }

            h1 {
                color: #00d9ff;
                font-size: 42px;
            }

            .content {
                padding: 60px 20px;
            }

            .service {
                background: #101f35;
                border: 1px solid #00d9ff;
                padding: 20px;
                margin: 15px auto;
                max-width: 350px;
                border-radius: 12px;
            }

            button {
                background: #00d9ff;
                color: #00101b;
                padding: 15px 30px;
                border: none;
                border-radius: 8px;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <header>
            <h1>VR GADGET</h1>
            <p>PHONE REPAIR SPECIALIST</p>
        </header>

        <div class="content">
            <h2>REPAIR IPHONE & ANDROID</h2>
            <p>Servis cepat dan harga berpatutan!</p>

            <div class="service">
                <h3>LCD REPAIR</h3>
                <p>Servis penukaran skrin telefon</p>
            </div>

            <div class="service">
                <h3>BATTERY REPAIR</h3>
                <p>Servis penukaran bateri</p>
            </div>

            <div class="service">
                <h3>CHARGING PORT</h3>
                <p>Servis masalah pengecasan</p>
            </div>

            <button>VR GADGET</button>
        </div>
<a href="https://wa.me/60176933120" target="_blank" class="whatsapp">
    CHAT WHATSAPP
</a>

<style>
.whatsapp {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: #00c853;
    color: white;
    padding: 15px 20px;
    border-radius: 30px;
    text-decoration: none;
    font-weight: bold;
}
</style>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
