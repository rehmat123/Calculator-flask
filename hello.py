from flask import Flask, render_template, request
import re
app = Flask(__name__)
@app.route('/')
def student():
   return render_template('calculator.html')
@app.route('/',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
      result = request.form['answer']
      first = re.search(r'\d+', result).group()
      last = re.match('.*?([0-9]+)$', result).group(1)
      char =  re.findall('[^A-Za-z0-9]',result)[0]
      final =0
      if(char=='+'):
          final = int(first) + int(last)
      if(char=='-'):
          final = int(first) - int(last)
      if(char == '*'):
          final = int(first) * int(last)
      if(char == '/'):
          if(int(last) == 0):
              final =0
          else:
              final = int(first) / int(last)


      return render_template('calculator.html',result=final)

if __name__ == '__main__':
   app.run(debug = True)