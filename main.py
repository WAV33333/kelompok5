from flask import Flask

# Membuat instance dari Flask
app = Flask(__name__)

# Menentukan route/halaman utama
@app.route("/")
def home():
    return "Halo, dunia! Ini adalah aplikasi Flask pertama saya."

# Menjalankan aplikasi jika file ini dieksekusi langsung
if __name__ == "__main__":
    app.run(debug=True)
