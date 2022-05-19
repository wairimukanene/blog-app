from flask_wtf import FlaskForm 
from wtforms import SubmitField,TextAreaField,StringField,SelectField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Add or Update your bio so that we get to know you.',validators = [DataRequired()])
    submit = SubmitField('Submit')
    
class AddBlog(FlaskForm):
    title = StringField('Title', validators =[DataRequired()])
    content = TextAreaField('Content', validators = [DataRequired()])
    submit = SubmitField('Post Blog')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')
    
class AddBlog(FlaskForm):
    title = StringField('Title', validators =[DataRequired()])
    content = TextAreaField('Content', validators = [DataRequired()])
    submit = SubmitField('Post Blog')
    
    