import flask

app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
TVshows = ["House MD","WWE", "Cowboy Bebop","Arcane","Rick and Morty"]
@app.route("/")

def index():
    return flask.render_template("index.html", name= "Abdi", len = len(TVshows), TVshows = TVshows)


app.run(use_reloader= True ,debug=True)

