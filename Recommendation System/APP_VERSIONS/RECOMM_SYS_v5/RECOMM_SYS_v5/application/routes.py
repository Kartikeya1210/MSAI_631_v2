from application import app, db
from flask import render_template, url_for, request, redirect, flash, session
from application.models import movies, users
from application.forms import LoginForm

ratings_ = [{'Movie_Id': 6552,
  'Cust_Id': 1132304,
  'Rating': 1.0,
  'Name': "Charlie's Angels"},
 {'Movie_Id': 8099,
  'Cust_Id': 1132304,
  'Rating': 1.0,
  'Name': 'Reign of Fire'},
 {'Movie_Id': 9340, 'Cust_Id': 1132304, 'Rating': 4.0, 'Name': 'Pearl Harbor'},
 {'Movie_Id': 12672, 'Cust_Id': 1132304, 'Rating': 4.0, 'Name': 'John Q'},
 {'Movie_Id': 16272,
  'Cust_Id': 1132304,
  'Rating': 2.0,
  'Name': 'Crouching Tiger'},
 {'Movie_Id': 17157,
  'Cust_Id': 1132304,
  'Rating': 3.0,
  'Name': 'Saving Private Ryan'}]

preds_ = [{'Movie_Id': 11283,
  'Cust_Id': 1132304,
  'Predicted_Rating': 3.2,
  'Name': 'Forrest Gump'},
 {'Movie_Id': 17085,
  'Cust_Id': 1132304,
  'Predicted_Rating': 3.0,
  'Name': '24: Season 2'},
 {'Movie_Id': 13468,
  'Cust_Id': 1132304,
  'Predicted_Rating': 3.0,
  'Name': 'Law & Order: Season 3'},
 {'Movie_Id': 7234,
  'Cust_Id': 1132304,
  'Predicted_Rating': 3.0,
  'Name': 'Men of Honor'},
 {'Movie_Id': 15861,
  'Cust_Id': 1132304,
  'Predicted_Rating': 2.9,
  'Name': 'CSI: Season 2'}]

@app.route("/")
def index():
    return render_template("index.html", navindex=True)

@app.route("/catalog")
def catalog():
    moviecat_ = movies.objects.all()
    return render_template("catalog.html", navcatalog=True, moviecat=moviecat_)

@app.route("/reviews")
def reviews():
    if not session.get('Cust_Id'):
        flash(f"Please login to access reviews", "danger")
        return redirect(url_for('login')) # If not logged in, redirect user to login page
    return render_template("reviews.html", navreviews=True, ratings=ratings_)

@app.route("/recommend")
def recommend():
    if not session.get('Cust_Id'):
        flash(f"Please login to access recommendations", "danger")
        return redirect(url_for('login'))  # If not logged in, redirect user to login page
    return render_template("recommend.html", navrecommend=True, predictions=preds_)

@app.route("/login", methods=["GET","POST"])
def login():
    if session.get('Cust_Id'):
        return redirect(url_for('index'))  # If already logged in, redirect user to home page
    
    form = LoginForm()
    if form.validate_on_submit():
        # Get form data
        femail = request.form.get("email")
        fpassword = request.form.get("password")
        # Compare data against db
        #user = users.objects(Email = femail, Password = fpassword).first() # clear password
        user = users.objects(Email = femail).first()
        #user.print_password(fpassword)
        if user and user.get_password(fpassword): # encrypted password
            flash(f"Welcome back, {user.First_Name}", "success")
            session['Cust_Id'] = user.Cust_Id
            session['First_Name'] = user.First_Name
            session['Last_Name'] = user.Last_Name
            return redirect("/")
        else:
            flash("Sorry, login failed", "danger")            
    return render_template("login.html", form=form, navlogin=True)

@app.route("/logout")
def logout():
    session['Cust_Id'] = False
    session.pop('First_Name', None)
    session.pop('Last_Name', None)
    return redirect("/")