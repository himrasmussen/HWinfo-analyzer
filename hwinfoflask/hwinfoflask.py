from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os;print(os.getcwd())

#from hwinfoflask import hwinfo_analyze as hwinfo

from . import tester
from . import voltage
from . import helpers
from . import graph_maker
from . import gpu
from . import cpu
from . import voltage
from . import hwinfo_analyze as hwinfo


app = Flask(__name__)

<<<<<<< HEAD
UPLOAD_FOLDER = os.path.join(app.root_path, "dynamic", "uploads")
ANALYSES_FOLDER = os.path.join(app.root_path, "dynamic", "analyses")
TEMPLATE_FOLDER = os.path.join(app.root_path, "static", "templates")

ALLOWED_EXTENSIONS = set(['csv'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filenumber = str(len(os.listdir(UPLOAD_FOLDER)))
            filename =  filenumber + '.csv'
            file.save(os.path.join(UPLOAD_FOLDER, filename))


            analysis_dict, graph_name = hwinfo.main(
                                                os.path.join(
                                                    UPLOAD_FOLDER,
                                                    filename
                                                    )
                                                )


            rendered_page = render_template(
                                            'analysis.html',
                                            analysis_dict=analysis_dict,
                                            graph_name=graph_name
                                            )


            analysis_filename = os.path.join(
                                            ANALYSES_FOLDER,
                                            "{}.html".format(filenumber))
            with open(analysis_filename , "w") as f:
                f.write(rendered_page)

            return redirect(url_for("show_analysis", filenumber=filenumber))


    #return "Ahoy!"
    return send_from_directory("static", "homepage.html")
    #<a href="sample_analysis.html">Sample log.</a>

@app.route('/analysis<filenumber>')
def show_analysis(filenumber):
    with open(os.path.join(ANALYSES_FOLDER, filenumber + ".html")) as f:
        return ''.join(f.readlines())

@app.route('/graph<filename>')
def graph(filename):
    path = os.path.join(app.root_path, "dynamic", "graphs")
    return send_from_directory(path, filename)


@app.route('/sample_analysis')
def display_sample_analysis():
    with open("sample_analysis.html") as f:
        return ''.join(f.readlines())

@app.route("/hello")
def hello():
    return "YARR!!"

@app.route("/treasure")
def treasure():
    return "10 Diamonds"


if __name__ == "__main__":
    app.run(debug=True)
