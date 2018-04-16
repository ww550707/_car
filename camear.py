from flask import Flask , render_template

app  =  Flask(__name__)

'''
@app.route('/')
def  index():
    return 'hello world'
'''

'''
@app.route('/hello')
def  world():
    return 'hello'
'''

@app.route('/')
def html_test():
	return render_template('index.html')

@app.route('/<name>')
def  index(name):
	
	if(name == 'forward'):
		print('up')
	if (name == 'back'):
		print('down')
	if (name == 'left'):
		print('left')
	if (name == 'right'):
		print('right')
		
	return render_template('index.html')

if __name__=='__main__':
	app.run(debug=True,host='192.168.3.23',port=8080)
	'''
    app.run(debug=True,host='0.0.0.0',port=5000)
	'''
