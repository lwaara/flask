from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	print "something"
	return "Hello World!"

@app.route("/leslie", methods=['GET'])
def leslie():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()