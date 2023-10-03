from flask import Flask
dict = {'78':{'link':'https://replit.com/@Emmanuel2018/Day78100Days?s=app', 'text':'The task was way too sophisticated'}}
marach = Flask(__name__)

@marach.route('/')
def home():
  return 'Welcome to my Homepage. You can type /"daynumber" to load the relevant day reflection'
  
@marach.route('/<num>')
def content(num):
  title = f'Day {num}'
  a = f'Day {num} Reflection'
  template = ''
  file = open('template/reflection.html', 'r')
  template = file.read()
  file.close()

  template = template.replace('{title}', title)
  template = template.replace('{daynumber}', a)
  template = template.replace('{link}', dict['78']['link'])
  template = template.replace('{text}', dict['78']['text'])
  
  return template
  
  
marach.run(host='0.0.0.0', port=81)