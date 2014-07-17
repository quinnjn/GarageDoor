from flask import Flask, render_template, request

from garagedoor import GarageDoor

app = Flask(__name__)
garageDoor = GarageDoor()

@app.route("/", methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		garageDoor.open()
	return render_template('index.html')

if __name__ == "__main__":
	try:
		app.run(host='0.0.0.0', port=80, debug=True)
	except KeyboardInterrupt:
		garageDoor.cleanup()
