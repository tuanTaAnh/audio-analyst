from flask import *
from test import *
import os


app=Flask(__name__,template_folder='templates')
UPLOAD_FOLDER = r"data/test"


@app.route('/')
def upload():
    return render_template("file_upload_form.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        # print("f: ", f)
        print("f.filename: ", f.filename)
        savepath = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(savepath)
        # f.save(savepath)
        probs, segs, class_names, c = test(savepath)
        # print("AAAAAA"*10)
        # print(probs)
        # print("AAAAAA" * 10)
        return render_template("success.html", name=f.filename, probs = probs, segs = segs, class_names = class_names, c = c)


if __name__ == '__main__':
    app.run(debug=True)