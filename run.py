from app import app
import os

if __name__ == '__main__':
    print(os.environ.get('DATABASE_URL'))
    app.run(host='0.0.0.0', port=8080, debug=True)
