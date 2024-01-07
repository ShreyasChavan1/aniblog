from flask import Flask,flash,redirect,render_template,request,session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from sqlalchemy import distinct
from datetime import datetime
from flask_mail import Mail,Message
import os
import json

with open('config.json','r') as f:
   params = json.load(f)['params'] 


app = Flask(__name__,template_folder='template',static_folder='static')
app.secret_key = 'the random string'
# change if server is production server to False
local = True
if (local):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['db-server']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod-server']
db = SQLAlchemy(app)

app.config.update(
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_PORT = "465",
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['Admin_email'],
    MAIL_PASSWORD = params['gmail_pass'] 
)
mail = Mail(app)

app.config['UPLOAD_FOLDER'] = params['upload_loc']
class Post(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),  nullable=False)
    tagline = db.Column(db.String(20),  nullable=True)
    slug = db.Column(db.String(12) , nullable=False)
    content = db.Column(db.String(120),  nullable=False)
    date = db.Column(db.String(120),  nullable=True)
    img = db.Column(db.String(20),  nullable=True)
    category = db.Column(db.String(20),  nullable=True)
    author = db.Column(db.String(20),  nullable=True)
    author_img = db.Column(db.String(20),  nullable=True)
    author_desc = db.Column(db.String(20),  nullable=True)
    

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),  nullable=False)
    email = db.Column(db.String(20),  nullable=True)
    message = db.Column(db.String(120),  nullable=False)
    date = db.Column(db.String(120),  nullable=True)


@app.route('/')
def index():
    all_categories = db.session.query(distinct(Post.category)).all()
    categories = [category[0] for category in all_categories]

    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date.desc()).paginate(page=page, per_page=params['no_posts'], error_out=False)
    return render_template('index.html', params=params, posts=posts ,categories = categories)

# @app.route('/category/<string:cat>')
# def category(cat):
#     posts= Post.query.filter_by(category = cat)
#     return render_template('category.html',params = params,posts = posts,cat = cat )

@app.route('/category/<string:cat>')
def category(cat):
    posts = Post.query.filter_by(category=cat)
    # Retrieve a list of other categories excluding the current category
    other_categories = Post.query.filter(Post.category != cat).distinct(Post.category).values(Post.category)
    other_categories = [category[0] for category in other_categories]

    return render_template('category.html', params=params, posts=posts, cat=cat, other_categories=other_categories)


@app.route('/contact',methods = ['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        entry = Contacts(name = name,email = email,message = message,date = datetime.now())
        db.session.add(entry)
        db.session.commit()
        # mail.send_message('New message from '+name, sender = email, recipients = [params['Admin_email']] ,body = message )
        msg = Message( 
                f'contact request from {name} email: {email}', 
                sender = email, 
                recipients = [params['Admin_email']] 
               ) 
        msg.body = message
        mail.send(msg)
    return render_template('contact.html',params = params)

@app.route('/about')
def about():
    return render_template('about.html',params = params)

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route('/delete/<string:srno>')
def delete(srno):
    if ('user' in session and session['user'] == params['admin']):
        post = Post.query.filter_by(srno = srno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')

@app.route('/edit/<string:srno>',methods= ['GET','POST'])
def edit(srno):
    if ('user' in session and session['user'] == params['admin']): 
        if request.method == 'POST':
            title = request.form.get('title')
            slug = request.form.get('slug')
            tagline = request.form.get('tline')
            content = request.form.get('content')
            img = request.form.get('img')
            cat = request.form.get('category')
            auth = request.form.get('author')
            auth_img = request.form.get('author_img')
            auth_desc = request.form.get('auth_desc')
            date = datetime.now()
            if srno == '0':
                ent = Post(title = title, slug = slug, tagline = tagline, content = content , img=img,category = cat,author = auth,author_img = auth_img,author_desc = auth_desc,date = date)
                db.session.add(ent)
                db.session.commit()
            else : 
                post = Post.query.filter_by(srno = srno).first()
                post.title = title
                post.slug = slug
                post.tagline = tagline
                post.content = content
                post.img = img
                post.category = cat
                post.author = auth
                post.author_img = auth_img
                post.author_desc = auth_desc
                db.session.commit()
            return redirect('/edit/' + srno)
        post = Post.query.filter_by(srno = srno).first()
        return render_template('edit.html',params = params, post = post, srno = srno)
    

@app.route('/post/<string:post_slug>',methods=['GET'])
def pst(post_slug):
    post = Post.query.filter_by(slug = post_slug).first()
    return render_template('post.html',params = params,post = post)

@app.route('/dashboard',methods = ['GET','POST'])
def Admin():
    if ('user' in session and session['user'] == params['admin']):
        posts = Post.query.filter_by().all()
        return render_template('dashboard.html', params=params, posts=posts)
    if request.method == 'POST':
        name1 = request.form.get('uname')
        passw = request.form.get('upass')
        if (name1 == params['admin'] and passw == params['pass']):
            # we have to set the sessionn before login in 
            session['user'] = name1
            posts = Post.query.all()
            return render_template('dashboard.html',params = params,posts = posts)
    else:
        return render_template('login.html',params = params)
    
@app.route('/upload',methods = ['GET','POST'])
def upload():
    if ('user' in session and session['user'] == params['admin']):
        if request.method == 'POST':
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
            return 'uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)