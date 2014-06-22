from flask import Flask

from garagedoor import GarageDoor

app = Flask(__name__)
garageDoor = GarageDoor()

@app.route("/open")
def openGarage():
	garageDoor.open()
	return "open"

@app.route("/close")
def closeGarage():
	garageDoor.close()
	return "close"

if __name__ == "__main__":
	try:
		app.run(host='0.0.0.0', port=80, debug=True)
	except KeyboardInterrupt:
		garageDoor.cleanup()
