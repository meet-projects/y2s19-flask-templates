from flask import Flask, render_template
evn = 0
#if evn ==0 then deployment server or else if  development server 

app = Flask(__name__)

@app.route('/')
def home_page():
    return "Hello World"

if __name__ == '__main__':
    if (env == 0):
      port = int(os.environ.get('PORT', 5000))
      app.run(host='0.0.0.0', port=port)
    else :
        app.run(debug = True)
