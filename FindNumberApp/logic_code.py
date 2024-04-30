from flask import Flask,render_template,request
import random
app = Flask(__name__)

randnum=random.randint(1,100)
count_numbers = 0

@app.route('/',methods=['GET','POST'])
def displayApp():
    global count_numbers,randnum
    STRING_PLACEHOLDER = 'ADD YOUR NUMBER FIRST'
    if request.method=='POST':
        formnumber = int(request.form.get('number'))
        # print(formnumber,randnum)
        count_numbers += 1
        if randnum == formnumber:
            STRING_PLACEHOLDER = f'CONGRATULATIONS YOU HAVE GUESSED THE CORRECT NUMBER IN {count_numbers} ATTEMPTS'
            randnum = random.randint(1,100)
            count_numbers = 0
        elif randnum > formnumber:
            STRING_PLACEHOLDER =f'YOUR NUMBER {formnumber} is less than the Target Number'
        else:
            STRING_PLACEHOLDER =f'YOUR NUMBER {formnumber} is more than the Target Number'
        return render_template('NumberFormat.html',STRING_PLACEHOLDER_HTML=STRING_PLACEHOLDER,ATTEMPT_NUMBER=count_numbers)
    count_numbers = 0
    return render_template('NumberFormat.html',STRING_PLACEHOLDER_HTML=STRING_PLACEHOLDER,ATTEMPT_NUMBER=count_numbers)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8000',debug=True)