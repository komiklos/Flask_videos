from flask import Flask, render_template

app = Flask(__name__)

#Whenever the user requests this URL profile,
#  with someone's name after it then I am goint to
# look into my directory templates for a file called profile.html
@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)




if __name__ == '__main__':
    app.run()