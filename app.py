from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        event=request.form['event']
        return f"<h1> thank you {name} your registration for {event} is confirmed !</h1><p>registration deatils sent on youe email {email}</p>"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)