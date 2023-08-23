import sys,os

sys.path.append('c:/Users/ramosv/Desktop/GitHub/Flask-Website/')


from site import build

app = build()

if __name__ == '__main__':
    app.run(debug=True)
