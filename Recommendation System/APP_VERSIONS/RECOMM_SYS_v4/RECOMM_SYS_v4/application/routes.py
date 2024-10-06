from application import app, db
from flask import render_template
from application.models import movies

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
    return render_template("reviews.html", navreviews=True, ratings=ratings_)

@app.route("/recommend")
def recommend():
    return render_template("recommend.html", navrecommend=True, predictions=preds_)

@app.route("/login")
def login():
    return render_template("login.html", navlogin=True)