from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/thanku.html')
    else:
        return 'something went wrong'


if __name__ == '__main__':
    app.run(debug=True)



# @app.route("/index.html")
# def my_home2():
#     return render_template('index.html')
#
# @app.route("/works.html")
# def my_works():
#     return render_template("works.html")
#
# @app.route("/work.html")
# def my_work():
#     return render_template("work.html")
#
# @app.route("/about.html")
# def about_me():
#     return render_template("about.html")
#
# @app.route("/contact.html")
# def contact_me():
#     return render_template("contact.html")
#
# @app.route("/components.html")
# def my_components():
#     return render_template("components.html")



