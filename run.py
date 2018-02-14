from app import app
from app import CONFIG

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=CONFIG['PORT'], debug=CONFIG['DEBUG'])
