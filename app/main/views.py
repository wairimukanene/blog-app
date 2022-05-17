from flask import render_template
from . import main
from flask_login import login_required,current_user


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Blogger'
    
    return render_template('index.html', title = title)
  
@main.route('/quotes')
def quotes():

    '''
    '''
    quote = get_quote()
    title = 'Blogger | Quotes'
    
    return render_template('quotes.html', title = title,quote = quote)
  
@main.route('/loggedin')
def loggedin():

    title = 'Blogger'

    return render_template('loggedin.html',title =title)

