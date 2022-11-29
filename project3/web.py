from project3 import app
#Port is currently set to open on port 3000
if __name__ == "__main__":
    app.run(debug=True, port=3000, host='0.0.0.0')