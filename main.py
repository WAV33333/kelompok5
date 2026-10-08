from flask import Flask

# Membuat instance dari Flask
app = Flask(__name__)

# Menentukan route/halaman utama
@app.route("/")
def home():
    return "Dzaki Suka Jonathan."

# Menjalankan aplikasi jika file ini dieksekusi langsung
if __name__ == "__main__":
    app.run(debug=True)
