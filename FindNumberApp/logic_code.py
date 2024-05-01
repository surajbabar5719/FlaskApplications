from flask import Flask,render_template,request,redirect
from application_functions.FindNumberFunctions import getRandomNumber
from application_functions.calculatorFunctions import getCalculatorAction
app = Flask(__name__)

randnum = getRandomNumber()
count_numbers = 0

@app.route('/')
def homePage():
    return render_template('HomePage.html')

@app.route('/findNumberGame',methods=['GET','POST'])
def displayApp():
    global count_numbers,randnum
    STRING_PLACEHOLDER = 'ADD YOUR NUMBER FIRST'
    if request.method=='POST':
        formnumber = int(request.form.get('number'))
        # print(formnumber,randnum)
        count_numbers += 1
        if randnum == formnumber:
            STRING_PLACEHOLDER = f'CONGRATULATIONS YOU HAVE GUESSED THE CORRECT NUMBER IN {count_numbers} ATTEMPTS'
            randnum = getRandomNumber()
            count_numbers = 0
        elif randnum > formnumber:
            STRING_PLACEHOLDER =f'YOUR NUMBER {formnumber} is less than the Target Number'
        else:
            STRING_PLACEHOLDER =f'YOUR NUMBER {formnumber} is more than the Target Number'
        return render_template('NumberFormat.html',STRING_PLACEHOLDER_HTML=STRING_PLACEHOLDER,ATTEMPT_NUMBER=count_numbers)
    count_numbers = 0
    return render_template('NumberFormat.html',STRING_PLACEHOLDER_HTML=STRING_PLACEHOLDER,ATTEMPT_NUMBER=count_numbers)


    

@app.route('/calculator',methods=['GET','POST'])
def calculator():
    if request.method == 'POST':
        first_number = int(request.form.get('first_number')   )
        second_number = int(request.form.get('second_number'))
        action =request.form.get('ACTION')
        return render_template('CalculatorTemplate.html',RESULT= getCalculatorAction(first_number,second_number,action))
    return render_template('CalculatorTemplate.html',RESULT='')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8000',debug=True)