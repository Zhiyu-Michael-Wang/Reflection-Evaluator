from flask import Flask,request,redirect,render_template,url_for
from markupsafe import escape
import amNLU

application = Flask(__name__)

@application.route('/')
def index():
    return redirect(url_for('evaluation'))


@application.route('/evaluation', methods=["POST", "GET"])
def evaluation():
    if request.method == "POST":
        text_input = str(request.form["information"])       

        result = int(amNLU.analyze(textInput = text_input))
        result = result if result > 0 else 0
        if(result <= 3):
            result = str(result) + '/10 -' + '\nIt is unlikely to have negative outcomes for sharing this piece of information.'
        elif (result <= 5):
            result = str(result) + '/10 -' + '\nThere might be negative outcomes for sharing this piece of information.'
        elif (result <= 7):
            result = str(result) + '/10 -' + '\nThis piece of information is likely to be inflammatory and biased. Please have a closer look before sharing it.'
        else:
            result = str(result) + '/10 -' + '\nMake sure that you know the repercussion of sharing this piece of information as it is highly likely to be inflammatory and biased.'
        
        
        return render_template('evaluation.html', estimation=result, lastInput=text_input)
    else:
        return render_template(
            'evaluation.html', 
            estimation="This tool provides you suggestions on the need of reflection before sharing anything on social media to help you avoid becoming a potential misinformation spreader.",
            lastInput="Type in something you want to share"
            )



if __name__ == "__main__":
    application.run()
