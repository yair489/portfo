from flask import Flask , render_template , url_for , request , redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route("/")
def my_home():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "did not save to database"
    else:
        return "somthing get worng"
    # return 'form submitted hooorayy'
    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    # return render_template('login.html', error=error)




def write_to_file(data):
    with open('database.txt' , mode = "a") as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email} ,{subject} ,{message}')

def write_to_csv(data):
    with open('database.csv' , mode = "a", newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writetr = csv.writer(database2 , delimiter="," , quotechar='"' , quoting= csv.QUOTE_MINIMAL)
        csv_writetr.writerow([email,subject,message])






# @app.route("/")
# def my_home():
#     return render_template('index.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/works.html")
# def work():
#     return render_template('works.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')


