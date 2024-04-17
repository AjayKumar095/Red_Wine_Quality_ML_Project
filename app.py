from flask import Flask, render_template, request

app=Flask(__name__)


@app.route('/', methods=['GET', "POST"])
def homepage():
    try :
        return render_template('index.html')
    
    except:
        return render_template('PageError.html', error=f'500 - Internal Server Error')


if __name__ == '__main__':
    
    app.run(debug=True, port=5000)