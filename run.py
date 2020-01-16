import os
from bot import main_bot
from multiprocessing import Process, Value
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
	return "<h1>Hello! Bot is working!</h1>", 200


if __name__ == "__main__":
	recording_on = Value('b', True)
	p = Process(target=main_bot)
	p.start()
	app.run(debug=True, use_reloader=False, host='0.0.0.0', port=int(os.getenv('PORT', 8000)))
	p.join()
