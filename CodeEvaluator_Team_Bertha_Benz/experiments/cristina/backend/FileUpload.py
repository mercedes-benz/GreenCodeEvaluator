from flask import Flask, request
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route('/uploader', methods = ['GET', 'POST'])
def uploaderfile():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
if __name__ == '__main__':
   app.run(debug = True)