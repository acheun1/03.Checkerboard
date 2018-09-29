#CheckerBoard
#2018 09 20
#Cheung Anthony


from flask import Flask, render_template
app = Flask(__name__)

# Write a program that generates an HTML page that looks like a checkerboard.  For this assignment, you're allowed to use <table> if you want.  You could use <div> if desired.  (Note: During Web Fundamentals, we discouraged you from using <table> as we didn't want you to use <table> to position different contents of your website on different parts of the table.  For this assignment however, you are allowed to use <table>.)

# @app.route('/')
# def index():
#     height=str(int(8*50))+"px"
#     width=str(int(8*54))+"px"
#     return render_template('index.html',height=height,width=width)
# if __name__=="__main__":
#     app.run(debug=True)

@app.route('/<height>/<width>')
def index(height,width):
    height_int=int(height)
    width_int=int(width)
    height=str(height_int*50)+"px"
    width=str(width_int*54)+"px"
    sqcnt=round((height_int*width_int)/16)
    return render_template('index1.html',height=height,width=width,sqcnt=sqcnt)
if __name__=="__main__":
    app.run(debug=True)
