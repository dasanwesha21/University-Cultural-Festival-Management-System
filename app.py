from flask import Flask, render_template, request, redirect, url_for, session,flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine, text
import random
import time

engine = create_engine('postgresql://sreesaha:sree%402002@localhost/asgn4')
connection = engine.connect()

app = Flask(__name__, template_folder='templates')
app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sreesaha:sree%402002@localhost/asgn4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

acc = ['SNVH','LLR','MMM','RPH','AZAD','RK','MS','VS','NH','LBS','HJB','JCB','RP','SNIG','MT']
can = ['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20']

db = SQLAlchemy(app)

def countdown(seconds):
    for i in range(seconds, 0, -1):
        flash(f"Redirecting in {i} seconds...","redirect")
        time.sleep(1)

class User(db.Model):
    __tablename__ = 'user_'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    passwd = db.Column(db.String(50))
    role_ = db.Column(db.String(50))

# db.create_all()

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    name_ = db.Column(db.String(50))
    start_date_time = db.Column(db.DateTime)
    end_date_time = db.Column(db.DateTime)
    venue = db.Column(db.String(50))
    descr = db.Column(db.String(100))
    budget = db.Column(db.Integer)
    status = db.Column(db.String(50))
    winner_id = db.Column(db.Integer)


class Participant(db.Model):
    __tablename__ = 'participant'
    id = db.Column(db.Integer, primary_key=True)
    eventid = db.Column(db.Integer,primary_key=True)

class Volunteer(db.Model):
    __tablename__ = 'volunteer'
    id = db.Column(db.Integer, primary_key=True)
    eventid = db.Column(db.Integer,primary_key=True)

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name_ = db.Column(db.String(50))
    roll = db.Column(db.String(20))
    department = db.Column(db.String(50))
    email = db.Column(db.String(50))
    hall = db.Column(db.String(50))
    role_ = db.Column(db.String(50))
    passwd = db.Column(db.String(50))

class External(db.Model):
    __tablename__ = 'ext'
    id = db.Column(db.Integer, primary_key=True)
    name_ = db.Column(db.String(50))
    email = db.Column(db.String(50))
    college_name = db.Column(db.String(50))
    passwd = db.Column(db.String(50))
    accommodation = db.Column(db.String(50))
    canteen = db.Column(db.String(50))

class Organiser(db.Model):
    __tablename__ = 'organiser'
    id = db.Column(db.Integer, primary_key=True)
    name_ = db.Column(db.String(50))
    passwd = db.Column(db.String(50))
    email = db.Column(db.String(50))

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.String(50), primary_key=True)
    passwd = db.Column(db.String(50))
    email = db.Column(db.String(50))



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin', methods = ['POST', 'GET'])
def admin():
    if request.method == 'POST':    
        return render_template('admin.html')
    elif request.method == 'GET':
        return render_template('admin.html')
    
@app.route('/admin_submit', methods = ['POST', 'GET'])
def admin_submit():
    if request.method == 'POST':
        username = request.form['name_admin']
        email = request.form['email_admin']
        password = request.form['password_admin']
        
        user = Admin.query.filter_by(id=username).first()
        passwd = Admin.query.filter_by(passwd=password).first()

        if user and passwd:
            # Manually set the user session
            session['user_id'] = user.id
            flash('Login successful!','success')
            # return render_template('display_flash.html', link = 'main_admin.html', msg = username)
            # wait in this page for few seconds
            # countdown(5)

            return redirect(url_for('main_admin', name=username))
        else:
            flash('Invalid username or password', 'error')
            # return render_template('display_flash.html', link = 'admin.html', msg = username)
            return render_template('admin.html')
    
    elif request.method == 'GET':
        username = request.form['name_admin']
        email = request.form['email_admin']
        password = request.form['password_admin']
        
        user = Admin.query.filter_by(id=username).first()
        passwd = Admin.query.filter_by(passwd=password).first()

        if user and passwd:
            # Manually set the user session
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            # countdown(5)
            # return redirect(url_for('display_flash.html', link = 'main_admin.html', msg = username))
            return redirect(url_for('main_admin', name=username))
        else:
            flash('Invalid username or password', 'error')
            # countdown(5)
            # return redirect(url_for('display_flash.html', link = 'admin.html', msg = username))
            return render_template('admin.html')
    
@app.route('/admin_back', methods = ['POST', 'GET'])
def admin_back():
    if request.method == 'POST':
        return render_template('index.html')
    elif request.method == 'GET':
        return render_template('index.html')
    
@app.route('/main_admin/<path:name>', methods = ['POST', 'GET'])
def main_admin(name):
    if request.method == 'POST':
        # flash(get_flashed_messages())
        return render_template('main_admin.html')
    elif request.method == 'GET':
        # flash(get_flashed_messages())
        return render_template('main_admin.html')

@app.route('/user', methods = ['POST', 'GET'])
def user():
    if request.method == 'POST':
        return render_template('user.html')
    elif request.method == 'GET':
        return render_template('user.html')
    
@app.route('/user_back', methods = ['POST', 'GET'])
def user_back():
    if request.method == 'POST':
        return render_template('index.html')
    elif request.method == 'GET':
        return render_template('index.html')
    
@app.route('/org_index', methods = ['POST', 'GET'])
def org_index():
    if request.method == 'POST':
        return render_template('org_index.html')
    elif request.method == 'GET':
        return render_template('org_index.html')
    
@app.route('/org_index_back', methods = ['POST', 'GET'])
def org_index_back():
    if request.method == 'POST':
        return render_template('user.html')
    elif request.method == 'GET':
        return render_template('user.html')
    
@app.route('/student_index', methods = ['POST', 'GET'])
def student_index():
    if request.method == 'POST':
        return render_template('student_index.html')
    elif request.method == 'GET':
        return render_template('student_index.html')
    
@app.route('/student_index_back', methods = ['POST', 'GET'])
def student_index_back():
    if request.method == 'POST':
        return render_template('user.html')
    elif request.method == 'GET':
        return render_template('user.html')

@app.route('/external_index', methods = ['POST', 'GET'])
def external_index():
    if request.method == 'POST':
        return render_template('external_index.html')
    elif request.method == 'GET':
        return render_template('external_index.html')
    
@app.route('/external_index_back', methods = ['POST', 'GET'])
def external_index_back():
    if request.method == 'POST':
        return render_template('user.html')
    elif request.method == 'GET':
        return render_template('user.html')
    
@app.route('/login_org', methods = ['POST', 'GET'])
def login_org():
    if request.method == 'POST':
        return render_template('login_org.html')
    elif request.method == 'GET':
        return render_template('login_org.html')
    
@app.route('/login_submit_org', methods = ['POST', 'GET'])
def login_submit_org():
    if request.method == 'POST':
        username = request.form['id_org']
        password = request.form['password_org']
        email = request.form['email_org']

        user = User.query.filter_by(username=username, passwd=password).first()
        

        if user :
            # Manually set the user session
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('main_org', name=user.id))
        else:
            flash('Invalid username or password', 'error')
        return render_template('login_org.html')
    
    elif request.method == 'GET':
        username = request.form['id_org']
        password = request.form['password_org']
        email = request.form['email_org']

        user = User.query.filter_by(username=username, passwd=password).first()
        

        if user :
            # Manually set the user session
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('main_org', name=user.id))
        else:
            flash('Invalid username or password', 'error')
        return render_template('login_org.html')
    
@app.route('/login_org_back', methods = ['POST', 'GET'])
def login_org_back():
    if request.method == 'POST':
        return render_template('org_index.html')
    elif request.method == 'GET':
        return render_template('org_index.html')
    
@app.route('/signup_org', methods = ['POST', 'GET'])
def signup_org():
    if request.method == 'POST':
        return render_template('signup_org.html')
    elif request.method == 'GET':
        return render_template('signup_org.html')
    
@app.route('/signup_submit_org', methods = ['POST', 'GET'])
def signup_submit_org():
    if request.method == 'POST':
        userid = random.randint(1000,9999)
        name = request.form['name_org']
        email = request.form['email_org']
        password = request.form['password_org']


        # Check if the username already exists
        if User.query.filter_by(id=userid).first():
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('signup_org'))
        

        # Hash the password before storing it
        # hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user
        username = "24CF"+ str(userid)
        new_user = User(id=userid,username = username, email=email, passwd=password, role_='organiser')
        new_organiser = Organiser(id=userid,name_=name,passwd=password,email=email)


        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
        db.session.add(new_organiser)
        db.session.commit()
        create_org_trigger = "CREATE TRIGGER create_user_trigger AFTER INSERT ON organiser FOR EACH ROW EXECUTE FUNCTION create_user();"
        result = connection.execute(text(create_org_trigger))
        db.session.commit()

        flash(f'Registration successful! Your username for login is {username}. Please log in.', 'success')
        return redirect(url_for('login_org'))

    if request.method == 'GET':
        userid = random.randint(1000,9999)
        name = request.form['name_org']
        email = request.form['email_org']
        password = request.form['password_org']


        # Check if the username already exists
        if User.query.filter_by(id=userid).first():
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('signup_org'))
        

        # Hash the password before storing it
        # hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user
        username = "24CF"+ str(userid)
        new_user = User(id=userid,username = username, email=email, passwd=password, role_='organiser')
        new_organiser = Organiser(id=userid,name_=name,passwd=password,email=email)


        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
        db.session.add(new_organiser)
        db.session.commit()
        create_org_trigger = "CREATE TRIGGER create_user_trigger AFTER INSERT ON organiser FOR EACH ROW EXECUTE FUNCTION create_user();"
        result = connection.execute(text(create_org_trigger))
        db.session.commit()

        flash(f'Registration successful! Your username for login is {username}. Please log in.', 'success')
        return redirect(url_for('login_org'))
    
@app.route('/signup_org_back', methods = ['POST', 'GET'])
def signup_org_back():
    if request.method == 'POST':
        return render_template('org_index.html')
    elif request.method == 'GET':
        return render_template('org_index.html')
    
@app.route('/main_org/<int:name>', methods = ['POST', 'GET'])
def main_org(name):
    if request.method == 'POST':
        return render_template('main_org.html', name=name)
    elif request.method == 'GET':
        return render_template('main_org.html',name=name)
    
@app.route('/signup_std', methods = ['POST', 'GET'])
def signup_std():
    if request.method == 'POST':
        return render_template('signup_std.html')
    elif request.method == 'GET':
        return render_template('signup_std.html')
    
@app.route('/main_std/<int:name>', methods = ['POST', 'GET'])
def main_std(name):
    if request.method == 'POST':
        return render_template('main_std.html',name=name)
    elif request.method == 'GET':
        return render_template('main_std.html',name=name)
    
@app.route('/signup_submit_std', methods = ['POST', 'GET'])
def signup_submit_std():
    if request.method == 'POST':
        userid = random.randint(1000,9999)
        name = request.form['name_std']
        roll = request.form['roll_std']
        department = request.form['dept_std']
        email = request.form['email_std']
        hall = request.form['hall_std']
        password = request.form['password_std']

        # Check if the username already exists
        if User.query.filter_by(id=userid).first():
            flash('Username already exists. Please choose a different one.', 'error')
            countdown(5)
            return redirect(url_for('signup_std'))
        

        # Hash the password before storing it
        # hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user
        username = "24CF"+ str(userid)
        new_user = User(id=userid,username = username, email=email, passwd=password, role_='student')
        new_student = Student(id=userid, name_=name, roll=roll, department=department, email=email, hall=hall, passwd=password)


        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
        db.session.add(new_student)
        db.session.commit()
        create_std_trigger = "CREATE TRIGGER create_user_trigger AFTER INSERT ON student FOR EACH ROW EXECUTE FUNCTION create_user();"
        result = connection.execute(text(create_std_trigger))
        # db.engine.execute(create_std_trigger)
        # db.session.commit()

        flash(f'Registration successful! Your username for login is {username}. Please log in.', 'success')
        countdown(10)
        return redirect(url_for('login_std'))
        # return render_template('signup_std.html')
    if request.method == 'GET':
        userid = random.randint(1000,9999)
        name = request.form['name_std']
        roll = request.form['roll_std']
        department = request.form['dept_std']
        email = request.form['email_std']
        hall = request.form['hall_std']
        password = request.form['password_std']


        # Check if the username already exists
        if User.query.filter_by(id=userid).first():
            flash('Username already exists. Please choose a different one.', 'error')
            countdown(5)
            return redirect(url_for('signup_std'))
        

        # Hash the password before storing it
        # hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user
        username = "24CF"+ str(userid)
        new_user = User(id=userid,username = username, email=email, passwd=password, role_='student')
        new_student = Student(id=userid, name_=name, roll=roll, department=department, email=email, hall=hall, passwd=password)


        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
        db.session.add(new_student)
        db.session.commit()
        create_std_trigger = "CREATE TRIGGER create_user_trigger AFTER INSERT ON student FOR EACH ROW EXECUTE FUNCTION create_user();"
        result = connection.execute(text(create_std_trigger))
        # db.engine.execute(create_std_trigger)
        # db.session.commit()

        flash(f'Registration successful! Your username for login is {username}. Please log in.', 'success')
        countdown(10)
        return redirect(url_for('login_std'))
        # return render_template('signup_std.html')

@app.route('/signup_std_back', methods = ['POST', 'GET'])
def signup_std_back():
    if request.method == 'POST':
        return render_template('student_index.html')
    elif request.method == 'GET':
        return render_template('student_index.html')   

@app.route('/signup_ext', methods = ['POST', 'GET'])
def signup_ext():
    if request.method == 'POST':
        return render_template('signup_ext.html')
    elif request.method == 'GET':
        return render_template('signup_ext.html')
    
@app.route('/signup_submit_ext', methods = ['POST', 'GET'])
def signup_submit_ext():
    
    

    if request.method == 'POST':
        userid = random.randint(1000,9999)
        name = request.form['name_ext']
        email = request.form['email_ext']
        college_name = request.form['college_name_ext']
        password = request.form['password_ext']
        accommodation = random.choice(acc)
        canteen = random.choice(can)
        

        # Check if the username already exists
        if User.query.filter_by(id=userid).first():
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('signup_ext'))
        

        # Hash the password before storing it
        # hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user
        username = "24CF"+ str(userid)
        new_user = User(id=userid,username = username, email=email, passwd=password, role_='external')
        new_external = External(id=userid, name_=name, email=email, college_name=college_name, passwd=password, accommodation=accommodation, canteen=canteen)


        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
        db.session.add(new_external)
        db.session.commit()
        create_std_trigger = "CREATE TRIGGER create_user_trigger AFTER INSERT ON ext FOR EACH ROW EXECUTE FUNCTION create_user();"
        result = connection.execute(text(create_std_trigger))
        # db.engine.execute(create_std_trigger)
        # db.session.commit()

        flash(f'Registration successful! Your username for login is {username}. Please log in.', 'success')
        return redirect(url_for('login_ext'))
        # return render_template('signup_ext.html')
    elif request.method == 'GET':
        userid = random.randint(1000,9999)
        name = request.form['name_ext']
        email = request.form['email_ext']
        college_name = request.form['college_name_ext']
        password = request.form['password_ext']
        accommodation = random.choice(acc)
        canteen = random.choice(can)
        

        # Check if the username already exists
        if User.query.filter_by(id=userid).first():
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('signup_ext'))
        

        # Hash the password before storing it
        # hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user
        username = "24CF"+ str(userid)
        new_user = User(id=userid,username = username, email=email, passwd=password, role_='external')
        new_external = External(id=userid, name_=name, email=email, college_name=college_name, passwd=password, accommodation=accommodation, canteen=canteen)


        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
        db.session.add(new_external)
        db.session.commit()
        create_std_trigger = "CREATE TRIGGER create_user_trigger AFTER INSERT ON ext FOR EACH ROW EXECUTE FUNCTION create_user();" 
    
        db.engine.execute(text(create_std_trigger))
        db.session.commit()

        flash(f'Registration successful! Your username for login is {username}. Please log in.', 'success')
        return redirect(url_for('login_ext'))
        # return render_template('signup_ext.html')
    
@app.route('/signup_ext_back', methods = ['POST', 'GET'])
def signup_ext_back():
    if request.method == 'POST':
        return render_template('external_index.html')
    elif request.method == 'GET':
        return render_template('external_index.html')
    
@app.route('/login_std', methods = ['POST', 'GET'])
def login_std():
    if request.method == 'POST':
        return render_template('login_std.html')
    elif request.method == 'GET':
        return render_template('login_std.html')    
    
@app.route('/login_submit_std', methods = ['POST', 'GET'])
def login_submit_std():
    if request.method == 'POST':
        username = request.form['id_std']
        password = request.form['password_std']
        email = request.form['email_std']

        user = User.query.filter_by(username=username,passwd = password).first()
        # passwd = User.query.filter_by(passwd=password).first()

        if user :
            # Manually set the user session
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            countdown(5)
            return redirect(url_for('main_std', name=user.id))
        else:
            flash('Invalid username or password', 'error')
            countdown(5)
        return render_template('login_std.html')
    elif request.method == 'GET':
        username = request.form['id_std']
        password = request.form['password_std']
        email = request.form['email_std']

        user = User.query.filter_by(username=username,passwd = password).first()
        # passwd = User.query.filter_by(passwd=password).first()

        if user :
            # Manually set the user session
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            countdown(5)
            return redirect(url_for('main_std', name=user.id))
        else:
            flash('Invalid username or password', 'error')
            countdown(5)
        return render_template('login_std.html')
    elif request.method == 'GET':
        return render_template('index.html')
    
@app.route('/login_std_back', methods = ['POST', 'GET'])
def login_std_back():
    if request.method == 'POST':
        return render_template('student_index.html')
    elif request.method == 'GET':
        return render_template('student_index.html')
    
@app.route('/login_ext', methods = ['POST', 'GET'])
def login_ext():
    if request.method == 'POST':
        return render_template('login_ext.html')
    elif request.method == 'GET':
        return render_template('login_ext.html')
    
@app.route('/login_submit_ext', methods = ['POST', 'GET'])
def login_submit_ext():
    if request.method == 'POST':
        username = request.form['id_ext']
        password = request.form['password_ext']
        email = request.form['email_ext']

        user = User.query.filter_by(username=username , passwd = password).first()
        # passwd = User.query.filter_by(passwd=password).first()

        if user :
            # Manually set the user session
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('main_ext', name=user.id))
        else:
            flash('Invalid username or password', 'error')
        return render_template('login_ext.html')
    elif request.method == 'GET':
        return render_template('index.html')
    
@app.route('/login_ext_back', methods = ['POST', 'GET'])
def login_ext_back():
    if request.method == 'POST':
        return render_template('external_index.html')
    elif request.method == 'GET':
        return render_template('external_index.html')
    
@app.route('/main_ext/<int:name>', methods = ['POST', 'GET'])
def main_ext(name):
    if request.method == 'POST':
        return render_template('main_ext.html', ext_name = name)
    elif request.method == 'GET':
        return render_template('main_ext.html', ext_name = name)
    
@app.route('/logout', methods = ['POST', 'GET'])
def logout():
    if request.method == 'POST':
        return render_template('index.html')
    elif request.method == 'GET':
        return render_template('index.html')
    
@app.route('/std_list', methods = ['POST', 'GET'])
def std_list():
    if request.method == 'POST':
        students = Student.query.all()
        return render_template('std_list.html', users = students)
    elif request.method == 'GET':
        students = Student.query.all()
        return render_template('std_list.html', users = students)
    
@app.route('/ext_list', methods = ['POST', 'GET'])
def ext_list():
    if request.method == 'POST':
        externals = External.query.all()
        return render_template('ext_list.html', externals = externals)
    elif request.method == 'GET':
        externals = External.query.all()
        return render_template('ext_list.html', externals = externals)
    
@app.route('/org_list', methods = ['POST', 'GET'])
def org_list():
    if request.method == 'POST':
        organisers = Organiser.query.all()
        return render_template('org_list.html', organisers = organisers)
    elif request.method == 'GET':
        organisers = Organiser.query.all()
        return render_template('org_list.html', organisers = organisers)
    
@app.route('/part_list', methods = ['POST', 'GET'])
def part_list():
    if request.method == 'POST':
        participants = Participant.query.all()
        return render_template('part_list.html', participants = participants)
    elif request.method == 'GET':
        participants = Participant.query.all()
        return render_template('part_list.html', participants = participants)
    
@app.route('/delete_part/<int:part_id>/<int:ev_id>', methods=['POST','GET'])
def delete_part(part_id,ev_id):
    if request.method == 'POST':
        participant = Participant.query.get_or_404(id=part_id,eventid=ev_id)
        db.session.delete(participant)
        db.session.commit()
        return redirect(url_for('part_list'))
    elif request.method == 'GET':
        participant = Participant.query.get_or_404(id=part_id,eventid=ev_id)
        db.session.delete(participant)
        db.session.commit()
        return redirect(url_for('part_list'))
    
@app.route('/vol_list', methods = ['POST', 'GET'])
def vol_list():
    if request.method == 'POST':
        volunteers = Volunteer.query.all()
        return render_template('vol_list.html', volunteers = volunteers)
    elif request.method == 'GET':
        volunteers = Volunteer.query.all()
        return render_template('vol_list.html', volunteers = volunteers)
    
@app.route('/delete_vol/<int:vol_id>/<int:eventid>', methods=['POST','GET'])
def delete_vol(vol_id,ev_id):
    if request.method == 'POST':
        volunteer = Volunteer.query.get_or_404(id=vol_id,eventid=ev_id)
        db.session.delete(volunteer)
        db.session.commit()
        return redirect(url_for('vol_list'))
    elif request.method == 'GET':
        volunteer = Volunteer.query.get_or_404(id=vol_id,eventid=ev_id)
        db.session.delete(volunteer)
        db.session.commit()
        return redirect(url_for('vol_list'))
    
@app.route('/event_list', methods = ['POST', 'GET'])
def event_list():
    if request.method == 'POST':
        events = Event.query.all()
        return render_template('event_list.html', events = events)
    elif request.method == 'GET':
        events = Event.query.all()
        return render_template('event_list.html', events = events)
    
@app.route('/delete_event/<int:event_id>', methods=['POST','GET'])
def delete_event(event_id):
    if request.method == 'POST':
        event = Event.query.get_or_404(event_id)
        db.session.delete(event)
        db.session.commit()
        #delete corresponding participant and volunteer
        if Participant.query.filter_by(event_id=event_id).all():
            for participant in Participant.query.filter_by(event_id=event_id).all():
                db.session.delete(participant)
                db.session.commit()
            # participant = Participant.query.get_or_404(event_id)
            # db.session.delete(participant)
            # db.session.commit()
        if Volunteer.query.filter_by(event_id=event_id).all():
            for volunteer in Volunteer.query.filter_by(event_id=event_id).all():
                db.session.delete(volunteer)
                db.session.commit()
        #     volunteer = Volunteer.query.get_or_404(event_id)
        #     db.session.delete(volunteer)
        #     db.session.commit()
        return redirect(url_for('event_list'))
    elif request.method == 'GET':
        event = Event.query.get_or_404(event_id)
        db.session.delete(event)
        db.session.commit()
        #delete corresponding participant and volunteer
        if Participant.query.filter_by(event_id=event_id).all():
            for participant in Participant.query.filter_by(event_id=event_id).all():
                db.session.delete(participant)
                db.session.commit()
            # participant = Participant.query.get_or_404(event_id)
            # db.session.delete(participant)
            # db.session.commit()
        if Volunteer.query.filter_by(event_id=event_id).all():
            for volunteer in Volunteer.query.filter_by(event_id=event_id).all():
                db.session.delete(volunteer)
                db.session.commit()
        #     volunteer = Volunteer.query.get_or_404(event_id)
        #     db.session.delete(volunteer)
        #     db.session.commit()
        return redirect(url_for('event_list'))
    
@app.route('/delete_user/<int:user_id>', methods=['POST','GET'])
def delete_user(user_id):
    if request.method == 'POST':
        if User.query.filter_by(id=user_id).first(): 
            if User.query.filter_by(id=user_id,role_='student').first():
                student = Student.query.get_or_404(id = user_id)
                if student.role_ == 'participant': 
                    db.session.delete(student)
                    db.session.commit()
                    participant = Participant.query.get_or_404(id=user_id)
                    db.session.delete(participant)
                    db.session.commit()
                    
                elif student.role_ == 'volunteer':
                    db.session.delete(student)
                    db.session.commit()
                    volunteer = Volunteer.query.get_or_404(id=user_id)
                    db.session.delete(volunteer)
                    db.session.commit()
                else:
                    db.session.delete(student)
                    db.session.commit()
                user = User.query.get_or_404(user_id)
                db.session.delete(student)
                db.session.commit()
                return redirect(url_for('std_list'))

            elif User.query.filter_by(id=user_id,role_='external').first():
                external = External.query.get_or_404(id=user_id)
                db.session.delete(external)
                db.session.commit()
                if Participant.query.filter_by(id=user_id).first():
                    participant = Participant.query.get_or_404(id=user_id)
                    db.session.delete(participant)
                    db.session.commit()
                user = User.query.get_or_404(id=user_id)
                db.session.delete(user)
                db.session.commit()
                return redirect(url_for('ext_list'))

            elif User.query.filter_by(id = user_id,role_='organiser').first():
                organiser = Organiser.query.get_or_404(id=user_id)
                db.session.delete(organiser)
                db.session.commit()
                user = User.query.get_or_404(id=user_id)
                db.session.delete(user)
                db.session.commit()
                return redirect(url_for('org_list'))

            return redirect(url_for('main_admin'))
    elif request.method == 'GET':
        if User.query.filter_by(id=user_id).first(): 
            if User.query.filter_by(id=user_id,role_='student').first():
                student = Student.query.get_or_404(id = user_id)
                if student.role_ == 'participant': 
                    db.session.delete(student)
                    db.session.commit()
                    participant = Participant.query.get_or_404(id=user_id)
                    db.session.delete(participant)
                    db.session.commit()
                    
                elif student.role_ == 'volunteer':
                    db.session.delete(student)
                    db.session.commit()
                    volunteer = Volunteer.query.get_or_404(id=user_id)
                    db.session.delete(volunteer)
                    db.session.commit()
                else:
                    db.session.delete(student)
                    db.session.commit()
                user = User.query.get_or_404(user_id)
                db.session.delete(student)
                db.session.commit()
                return redirect(url_for('std_list'))

            elif User.query.filter_by(id=user_id,role_='external').first():
                external = External.query.get_or_404(id=user_id)
                db.session.delete(external)
                db.session.commit()
                if Participant.query.filter_by(id=user_id).first():
                    participant = Participant.query.get_or_404(id=user_id)
                    db.session.delete(participant)
                    db.session.commit()
                user = User.query.get_or_404(id=user_id)
                db.session.delete(user)
                db.session.commit()
                return redirect(url_for('ext_list'))

            elif User.query.filter_by(id = user_id,role_='organiser').first():
                organiser = Organiser.query.get_or_404(id=user_id)
                db.session.delete(organiser)
                db.session.commit()
                user = User.query.get_or_404(id=user_id)
                db.session.delete(user)
                db.session.commit()
                return redirect(url_for('org_list'))

            return redirect(url_for('main_admin'))
        
@app.route('/add_std', methods = ['POST', 'GET'])
def add_std():
    if request.method == 'POST':
        userid = random.randint(1000,9999)
        name = request.form['name_std']
        roll = request.form['roll_std']
        department = request.form['dept_std']
        email = request.form['email_std']
        hall = request.form['hall_std']
        password = request.form['password_std']




        # Check if the username already exists
        if User.query.filter_by(id=userid).first():
            flash('Username already exists. Please choose a different one.', 'error')
            countdown(5)
            return redirect(url_for('add_std'))
        

        # Hash the password before storing it
        # hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user
        username = "24CF"+ str(userid)
        new_user = User(id=userid,username = username, email=email, passwd=password, role_='student')
        new_student = Student(id=userid, name_=name, roll=roll, department=department, email=email, hall=hall, passwd=password)


        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
        db.session.add(new_student)
        db.session.commit()
        create_std_trigger = "CREATE TRIGGER create_user_trigger AFTER INSERT ON student FOR EACH ROW EXECUTE FUNCTION create_user();"
        result = connection.execute(text(create_std_trigger))
        # db.engine.execute(create_std_trigger)
        # db.session.commit()

        
        return render_template('add_user.html')
        # return render_template('signup_std.html')
    if request.method == 'GET':
        userid = random.randint(1000,9999)
        name = request.form['name_std']
        roll = request.form['roll_std']
        department = request.form['dept_std']
        email = request.form['email_std']
        hall = request.form['hall_std']
        password = request.form['password_std']




        # Check if the username already exists
        if User.query.filter_by(id=userid).first():
            flash('Username already exists. Please choose a different one.', 'error')
            countdown(5)
            return redirect(url_for('add_std'))
        

        # Hash the password before storing it
        # hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user
        username = "24CF"+ str(userid)
        new_user = User(id=userid,username = username, email=email, passwd=password, role_='student')
        new_student = Student(id=userid, name_=name, roll=roll, department=department, email=email, hall=hall, passwd=password)


        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
        db.session.add(new_student)
        db.session.commit()
        create_std_trigger = "CREATE TRIGGER create_user_trigger AFTER INSERT ON student FOR EACH ROW EXECUTE FUNCTION create_user();"
        result = connection.execute(text(create_std_trigger))
        # db.engine.execute(create_std_trigger)
        # db.session.commit()

        # flash(f'Registration successful! Your username for login is {username}. Please log in.', 'success')
        # countdown(10)
        return render_template('add_user.html')
    
@app.route('/add_ext', methods = ['POST', 'GET'])
def add_ext():
    if request.method == 'POST':
        userid = random.randint(1000,9999)
        name = request.form['name_ext']
        email = request.form['email_ext']
        college_name = request.form['college_name_ext']
        password = request.form['password_ext']
        accommodation = random.choice(acc)
        canteen = random.choice(can)
        

        # Check if the username already exists
        if User.query.filter_by(id=userid).first():
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('add_ext'))
        

        # Hash the password before storing it
        # hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user
        username = "24CF"+ str(userid)
        new_user = User(id=userid,username = username, email=email, password=password, role='external')
        new_external = External(id=userid, name=name, email=email, college_name=college_name, password=password, accommodation=accommodation, canteen=canteen)


        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
        db.session.add(new_external)
        db.session.commit()
        create_std_trigger = "CREATE TRIGGER create_user_trigger AFTER INSERT ON ext FOR EACH ROW EXECUTE FUNCTION create_user();"
        result = connection.execute(create_std_trigger)
        # db.engine.execute(create_std_trigger)
        # db.session.commit()

        # flash(f'Registration successful! Your username for login is {username}. Please log in.', 'success')
        return render_template('add_user.html')
        # return render_template('signup_ext.html')
    elif request.method == 'GET':
        userid = random.randint(1000,9999)
        name = request.form['name_ext']
        email = request.form['email_ext']
        college_name = request.form['college_name_ext']
        password = request.form['password_ext']
        accommodation = random.choice(acc)
        canteen = random.choice(can)
        

        # Check if the username already exists
        if User.query.filter_by(id=userid).first():
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('add_ext'))
        

        # Hash the password before storing it
        # hashed_password = generate_password_hash(password, method='sha256')

        # Create
        username = "24CF"+ str(userid)
        new_user = User(id=userid,username = username, email=email, password=password, role='external')
        new_external = External(id=userid, name=name, email=email, college_name=college_name, password=password, accommodation=accommodation, canteen=canteen)


        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
        db.session.add(new_external)
        db.session.commit()
        create_std_trigger = "CREATE TRIGGER create_user_trigger AFTER INSERT ON ext FOR EACH ROW EXECUTE FUNCTION create_user();"
        result = connection.execute(create_std_trigger)
        # db.engine.execute(create_std_trigger)
        # db.session.commit()

        # flash(f'Registration successful! Your username for login is {username}. Please log in.', 'success')
        return render_template('add_user.html')
    
@app.route('/add_org', methods = ['POST', 'GET'])
def add_org():
    if request.method == 'POST':
        userid = random.randint(1000,9999)
        name = request.form['name_org']
        email = request.form['email_org']
        password = request.form['password_org']
        

        # Check if the username already exists
        if User.query.filter_by(id=userid).first():
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('add_org'))
        

        # Hash the password before storing it
        # hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user
        username = "24CF"+ str(userid)
        new_user = User(id=userid,username = username, email=email, passwd=password, role_='organiser')
        new_organiser = Organiser(id=userid,name_=name,passwd=password,email=email)


        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
        db.session.add(new_organiser)
        db.session.commit()
        create_org_trigger = """
                    CREATE TRIGGER create_user_trigger
                    AFTER INSERT ON organiser
                    FOR EACH ROW
                    EXECUTE FUNCTION create_user();
        """
        db.engine.execute(create_org_trigger)
        db.session.commit()

        return render_template('add_user.html')
        # return render_template('signup_org.html')
    elif request.method == 'GET':
        userid = random.randint(1000,9999)
        name = request.form['name_org']
        email = request.form['email_org']
        password = request.form['password_org']
        

        # Check if the username already exists
        if User.query.filter_by(id=userid).first():
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('add_org'))
        

        # Hash the password before storing it
        # hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user
        username = "24CF"+ str(userid)
        new_user = User(id=userid,username = username, email=email, passwd=password, role_='organiser')
        new_organiser = Organiser(id=userid,name_=name,passwd=password,email=email)


        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
        db.session.add(new_organiser)
        db.session.commit()
        create_org_trigger = """
                    CREATE TRIGGER create_user_trigger
                    AFTER INSERT ON organiser
                    FOR EACH ROW
                    EXECUTE FUNCTION create_user();
        """
        db.engine.execute(create_org_trigger)
        db.session.commit()

        return render_template('add_user.html')
    
@app.route('/add_user', methods = ['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        return render_template('add_user.html')
    elif request.method == 'GET':
        return render_template('add_user.html')
    
@app.route('/add_admin', methods = ['POST', 'GET'])
def add_admin():
    if request.method == 'POST':
        role = request.form['role']
        return render_template('add_admin.html', role = role)
    elif request.method == 'GET':
        role = request.form['role']
        return render_template('add_admin.html', role = role)
    
@app.route('/event_listext/<int:ext_name>', methods = ['POST', 'GET']) 
def event_listext(ext_name):
    if request.method == 'POST':
        events = Event.query.all()
        return render_template('event_list_ext.html',ext_id = ext_name,events = events)
    elif request.method == 'GET':
        events = Event.query.all()
        return render_template('event_list_ext.html',ext_id = ext_name,events = events)
    
@app.route('/register_ext/<int:user_id>/<int:ext_id>', methods = ['POST', 'GET'])
def register_ext(user_id,ext_id):
    if request.method == 'POST':
        id = Participant.query.filter_by(id=ext_id , eventid = user_id).first()
        if not id :
            new_part = Participant(id=ext_id, eventid=user_id)
            db.session.add(new_part)
            db.session.commit()
        else:
            flash('Already registered for the event', 'error')
            return redirect(url_for('event_listext'))
        return redirect(url_for('event_listext'))
    elif request.method == 'GET':
        id = Participant.query.filter_by(id=ext_id , eventid = user_id).first()
        if not id :
            new_part = Participant(id=ext_id, eventid=user_id)
            db.session.add(new_part)
            db.session.commit()
        else:
            flash('Already registered for the event', 'error')
            return redirect(url_for('event_listext'))

    
@app.route('/profile_ext/<int:ext_name>', methods = ['POST', 'GET'])
def profile_ext(ext_name):
    if request.method == 'POST':
        # ext_name = request.args.get('ext_name')
        external = External.query.get_or_404(ext_name)
        return render_template('profile_ext.html', external = external)
    elif request.method == 'GET':
        # ext_name = request.args.get('ext_name')
        external = External.query.get_or_404(ext_name)
        return render_template('profile_ext.html', external = external)
    
@app.route('/edit_profile_ext/<int:ext_id>', methods = ['POST', 'GET'])
def edit_profile(ext_id):
    if request.method == 'POST':
        external = External.query.get_or_404(ext_id)
        return render_template('edit_profile_ext.html', external = external)
    elif request.method == 'GET':
        external = External.query.get_or_404(ext_id)
        return render_template('edit_profile_ext.html', external = external)
    
@app.route('/submit_profile_ext/<int:ext_id>', methods = ['POST', 'GET'])
def submit_profile_ext(ext_id):
    if request.method == 'POST':
        external = External.query.get_or_404(ext_id)
        name_ = request.form.get('name_external')
        email = request.form.get('email')
        college_name = request.form.get('college_name')
        old_password = request.form.get('old_password')
        passwd = request.form.get('new_password')
        user = User.query.filter_by(id=ext_id , passwd=old_password).first()
        user_= User.query.get_or_404(ext_id)
        username = user_.username
        if old_password==None and not user:
            flash('Old password is incorrect', 'error')
            return redirect(url_for('edit_profile_ext', ext_id = ext_id))
        if request.form.get('new_password') != None:
            db.session.delete(external)
            db.session.commit()
            new_external = External(id=ext_id, name_=name_, email=email, college_name=college_name, passwd=passwd)
            db.session.add(new_external)
            db.session.commit()
            db.session.delete(user_)
            db.session.commit()
            new_user = User(id=ext_id,username=username,email = email,passwd=passwd,role_='external')
            db.session.add(new_user)
            db.session.commit()
        else:
            db.session.delete(external)
            db.session.commit()
            new_external = External(id=ext_id, name_=name_, email=email, college_name=college_name)
            db.session.add(new_external)
            db.session.commit()
            db.session.delete(user_)
            db.session.commit()
            new_user = User(id=ext_id,username=username,email = email,passwd=old_password,role_='external')
            db.session.add(new_user)
            db.session.commit()
        
        
        
        return render_template('profile_ext.html', external = external)
    elif request.method == 'GET':
        external = External.query.get_or_404(ext_id)
        name_ = request.form.get('name_external')
        email = request.form.get('email')
        college_name = request.form.get('college_name')
        old_password = request.form.get('old_password')
        passwd = request.form.get('new_password')
        user = User.query.filter_by(id=ext_id , passwd=old_password).first()
        user_= User.query.get_or_404(ext_id)
        username = user_.username
        if old_password==None and not user:
            flash('Old password is incorrect', 'error')
            return redirect(url_for('edit_profile_ext', ext_id = ext_id))
        if request.form.get('new_password') != None:
            db.session.delete(external)
            db.session.commit()
            new_external = External(id=ext_id, name_=name_, email=email, college_name=college_name, passwd=passwd)
            db.session.add(new_external)
            db.session.commit()
            db.session.delete(user_)
            db.session.commit()
            new_user = User(id=ext_id,username=username,email = email,passwd=passwd,role_='external')
            db.session.add(new_user)
            db.session.commit()
        else:
            db.session.delete(external)
            db.session.commit()
            new_external = External(id=ext_id, name_=name_, email=email, college_name=college_name)
            db.session.add(new_external)
            db.session.commit()
            db.session.delete(user_)
            db.session.commit()
            new_user = User(id=ext_id,username=username,email = email,passwd=old_password,role_='external')
            db.session.add(new_user)
            db.session.commit()
        
        
        
        return render_template('profile_ext.html', external = external)
    
@app.route('/event_liststd/<int:std_name>', methods = ['POST', 'GET']) 
def event_liststd(std_name):
    if request.method == 'POST':
        events = Event.query.all()
        return render_template('event_list_std.html',std_id = std_name,events = events)
    elif request.method == 'GET':
        events = Event.query.all()
        return render_template('event_list_std.html',std_id = std_name,events = events)
    
@app.route('/register_std_part/<int:user_id>/<int:std_id>', methods = ['POST', 'GET'])
def register_std_part(user_id,std_id):
    if request.method == 'POST':
        if not Volunteer.query.filter_by(id=std_id).all():
            id = Participant.query.filter_by(id=std_id , eventid = user_id).first()
            if not id :
                new_part = Participant(id=std_id, eventid=user_id)
                db.session.add(new_part)
                db.session.commit()
            else:
                flash('Already registered for the event', 'error')
                return redirect(url_for('event_liststd',std_name = std_id))
            return redirect(url_for('event_liststd',std_name = std_id))
        else:
            flash('You are a volunteer. You cannot participate in the event', 'error')
            return redirect(url_for('event_liststd',std_name = std_id))
    elif request.method == 'GET':
        if not Volunteer.query.filter_by(id=std_id).all():
            id = Participant.query.filter_by(id=std_id , eventid = user_id).first()
            if not id :
                new_part = Participant(id=std_id, eventid=user_id)
                db.session.add(new_part)
                db.session.commit()
            else:
                flash('Already registered for the event', 'error')
                return redirect(url_for('event_liststd',std_name = std_id))
            return redirect(url_for('event_liststd',std_name = std_id))
        else:
            flash('You are a volunteer. You cannot participate in the event', 'error')
            return redirect(url_for('event_liststd',std_name = std_id))
        
@app.route('/register_std_vol/<int:user_id>/<int:std_id>', methods = ['POST', 'GET'])
def register_std_vol(user_id,std_id):
    if request.method == 'POST':
        if not Participant.query.filter_by(id=std_id).all():
            id = Volunteer.query.filter_by(id=std_id , eventid = user_id).first()
            if not id :
                new_vol = Volunteer(id=std_id, eventid=user_id)
                db.session.add(new_vol)
                db.session.commit()
            else:
                flash('Already registered for the event', 'error')
                return redirect(url_for('event_liststd'))
            return redirect(url_for('event_liststd'))
        else:
            flash('You are a participant. You cannot volunteer for the event', 'error')
            return redirect(url_for('event_liststd'))
    elif request.method == 'GET':
        if not Participant.query.filter_by(id=std_id).all():
            id = Volunteer.query.filter_by(id=std_id , eventid = user_id).first()
            if not id :
                new_vol = Volunteer(id=std_id, eventid=user_id)
                db.session.add(new_vol)
                db.session.commit()
            else:
                flash('Already registered for the event', 'error')
                return redirect(url_for('event_liststd'))
            return redirect(url_for('event_liststd'))
        else:
            flash('You are a participant. You cannot volunteer for the event', 'error')
            return redirect(url_for('event_liststd'))
        
@app.route('/profile_std/<int:std_name>', methods = ['POST', 'GET'])
def profile_std(std_name):
    if request.method == 'POST':
        student = Student.query.get_or_404(std_name)
        return render_template('profile_std.html', student = student)
    elif request.method == 'GET':
        student = Student.query.get_or_404(std_name)
        return render_template('profile_std.html', student = student)
    
@app.route('/edit_profile_std/<int:std_id>', methods = ['POST', 'GET'])
def edit_profile_std(std_id):
    if request.method == 'POST':
        student = Student.query.get_or_404(std_id)
        return render_template('edit_profile_std.html', student = student)
    elif request.method == 'GET':
        student = Student.query.get_or_404(std_id)
        return render_template('edit_profile_std.html', student = student)
    
@app.route('/submit_profile_std/<int:std_id>', methods = ['POST', 'GET'])
def submit_profile_std(std_id):
    if request.method == 'POST':
        student = Student.query.get_or_404(std_id)
        name_ = request.form.get('name_student')
        email = request.form.get('email')
        roll = request.form.get('roll')
        department = request.form.get('department')
        hall = request.form.get('hall')
        old_password = request.form.get('old_password')
        user = User.query.filter_by(id=std_id , passwd = old_password).first()
        user_ = User.query.get_or_404(std_id)
        username = user_.username
        passwd = request.form.get('new_password')
        
        if old_password != None and not user:
            flash('Old password is incorrect', 'error')
            return redirect(url_for('edit_profile_std', std_id = std_id))
        if request.form.get('new_password') !=None:
            
            db.session.delete(student)
            db.session.commit()
            new_student = Student(id=std_id, name_ = name_, email = email, roll = roll, department = department, hall = hall, passwd = passwd)
            db.session.add(new_student)
            db.session.commit()
            db.session.delete(user_)
            db.session.commit()
            new_user = User(id=std_id,username = username,passwd=passwd,email=email,role_='student')
            db.session.add(new_user)
            db.session.commit()
        else :
            db.session.delete(student)
            db.session.commit()
            new_student = Student(id=std_id, name_ = name_, email = email, roll = roll, department = department, hall = hall, passwd = old_password)
            db.session.add(new_student)
            db.session.commit()
            db.session.delete(user_)
            db.session.commit()
            new_user = User(id=std_id,username =username,passwd=old_password,email=email,role_='student')
            db.session.add(new_user)
            db.session.commit()

        return render_template('profile_std.html', student = student)
    elif request.method == 'GET':
        student = Student.query.get_or_404(std_id)
        name_ = request.form.get('name_student')
        email = request.form.get('email')
        roll = request.form.get('roll')
        department = request.form.get('department')
        hall = request.form.get('hall')
        old_password = request.form.get('old_password')
        user = User.query.filter_by(id=std_id , passwd = old_password).first()
        user_ = User.query.get_or_404(std_id)
        username = user_.username
        
        if old_password != None and not user:
            flash('Old password is incorrect', 'error')
            return redirect(url_for('edit_profile_std', std_id = std_id))
        if request.form.get('new_password') !=None:
            passwd = request.form.get('new_password')
            db.session.delete(student)
            db.session.commit()
            new_student = Student(id=std_id, name_ = name_, email = email, roll = roll, department = department, hall = hall, passwd = passwd)
            db.session.add(new_student)
            db.session.commit()
            db.session.delete(user_)
            db.session.commit()
            new_user = User(id=std_id,username = username,passwd=passwd,email=email,role_='student')
            db.session.add(new_user)
            db.session.commit()
        else :
            db.session.delete(student)
            db.session.commit()
            new_student = Student(id=std_id, name_ = name_, email = email, roll = roll, department = department, hall = hall, passwd = old_password)
            db.session.add(new_student)
            db.session.commit()
            db.session.delete(user_)
            db.session.commit()
            new_user = User(id=std_id,username =username,passwd=old_password,email=email,role_='student')
            db.session.add(new_user)
            db.session.commit()

        return render_template('profile_std.html', student = student)
    
@app.route('/profile_org/<int:org_name>', methods = ['POST', 'GET'])
def profile_org(org_name):
    if request.method == 'POST':
        organiser = Organiser.query.get_or_404(org_name)
        return render_template('profile_org.html', organiser = organiser)
    elif request.method == 'GET':
        organiser = Organiser.query.get_or_404(org_name)
        return render_template('profile_org.html', organiser = organiser)
    
@app.route('/edit_profile_org/<int:org_id>', methods = ['POST', 'GET'])
def edit_profile_org(org_id):
    if request.method == 'POST':
        organiser = Organiser.query.get_or_404(org_id)
        return render_template('edit_profile_org.html', organiser = organiser)
    elif request.method == 'GET':
        organiser = Organiser.query.get_or_404(org_id)
        return render_template('edit_profile_org.html', organiser = organiser)
    
@app.route('/submit_profile_org/<int:org_id>', methods = ['POST', 'GET'])
def submit_profile_org(org_id):
    if request.method == 'POST':
        organiser = Organiser.query.get_or_404(org_id)
        # print(request.form)
        name_ = request.form.get('name_organiser')
        email = request.form.get('email')
        old_password = request.form.get('old_password')
        user  = User.query.filter_by(id=org_id , passwd = old_password).first()
        user_= User.query.get_or_404(org_id)
        username = user_.username
        passwd = request.form.get('new_password')
        if old_password != None and not user :
            flash('Old password is incorrect', 'error')
            print("incorrect old password")
            return redirect(url_for('edit_profile_org', org_id = org_id))
        if request.form.get('new_password') != None:
            db.session.delete(organiser)            
            db.session.commit()
            new_organiser = Organiser(id=org_id,name_=name_,passwd=passwd,email=email)
            db.session.add(new_organiser)
            db.session.commit()
            db.session.delete(user_)
            db.session.commit()
            new_user = User(id=org_id,username=username,email=email,passwd=passwd,role_='organiser')
            db.session.add(new_user)
            db.session.commit()
        else :
            db.session.delete(organiser)            
            db.session.commit()
            new_organiser = Organiser(id=org_id,name_=name_,passwd=old_password,email=email)
            db.session.add(new_organiser)
            db.session.commit()
            db.session.delete(user_)
            db.session.commit()
            new_user = User(id=org_id,username=username,email=email,passwd=old_password,role_='organiser')
            db.session.add(new_user)
            db.session.commit()
            
        organiser = Organiser.query.get_or_404(org_id)
        return render_template('profile_org.html', organiser = organiser)

    elif request.method == 'GET':
        organiser = Organiser.query.get_or_404(org_id)
        # print(request.form)
        name_ = request.form.get('name_organiser')
        email = request.form.get('email')
        old_password = request.form.get('old_password')
        user  = User.query.filter_by(id=org_id , passwd = old_password).first()
        user_= User.query.get_or_404(org_id)
        username = user_.username
        passwd = request.form.get('new_password')
        if old_password != None and not user :
            flash('Old password is incorrect', 'error')
            print("incorrect old password")
            return redirect(url_for('edit_profile_org', org_id = org_id))
        if request.form.get('new_password') != None:
            db.session.delete(organiser)            
            db.session.commit()
            new_organiser = Organiser(id=org_id,name_=name_,passwd=passwd,email=email)
            db.session.add(new_organiser)
            db.session.commit()
            db.session.delete(user_)
            db.session.commit()
            new_user = User(id=org_id,username=username,email=email,passwd=passwd,role_='organiser')
            db.session.add(new_user)
            db.session.commit()
        else :
            db.session.delete(organiser)            
            db.session.commit()
            new_organiser = Organiser(id=org_id,name_=name_,passwd=old_password,email=email)
            db.session.add(new_organiser)
            db.session.commit()
            db.session.delete(user_)
            db.session.commit()
            new_user = User(id=org_id,username=username,email=email,passwd=old_password,role_='organiser')
            db.session.add(new_user)
            db.session.commit()

        # db.session.delete(organiser)            
        # db.session.commit()
        # db.session.add(new_organiser)
        # db.session.commit()
        # db.session.delete(user_)
        # db.session.commit()
        # db.session.add(new_user)
        # db.session.commit()
            
        organiser = Organiser.query.get_or_404(org_id)
        return render_template('profile_org.html', organiser = organiser)

    
@app.route('/add_event', methods = ['POST', 'GET'])
def add_event():
    if request.method == 'POST':
        return render_template('add_event.html')
    elif request.method == 'GET':
        return render_template('add_event.html')
    
@app.route('/add_event_submit', methods = ['POST', 'GET'])
def add_event_submit():
    if request.method == 'POST':
        id = request.form['id_event']
        name = request.form['name_event']
        start = request.form['start_date_time_event']
        end = request.form['end_date_time_event']
        venue= request.form['venue_event']
        des = request.form['description_event']
        budget = request.form['budget_event']

        new_event = Event(id=int(id),name_ = name,start_date_time = start,end_date_time = end,venue = venue,descr = des,budget = int(budget),status ="Not started",winner_id = 0)



        # Add the user to the database
        db.session.add(new_event)
        db.session.commit()
        return render_template('main_org.html',name=int(id))
    elif request.method == 'GET':
        id = request.form['id_event']
        name = request.form['name_event']
        start = request.form['start_date_time_event']
        end = request.form['end_date_time_event']
        venue= request.form['venue_event']
        des = request.form['description_event']
        budget = request.form['budget_event']

        new_event = Event(id=int(id),name_ = name,start_date_time = start,end_date_time = end,venue = venue,descr = des,budget = int(budget),status = 'Not started',winner_id = 0)



        # Add the user to the database
        db.session.add(new_event)
        db.session.commit()
        return render_template('main_org.html',name=int(id))


@app.route('/update_event', methods = ['POST', 'GET'])
def update_event():
    if request.method == 'POST':
        events = Event.query.all()
        return render_template('update_event.html', events = events)
    elif request.method == 'GET':
        events = Event.query.all()
        return render_template('update_event.html', events = events)


@app.route('/update_event_submit/<int:event_id>', methods  = ['POST', 'GET'])
def update_event_submit(event_id):
    if request.method == 'POST':
        event = Event.query.get_or_404(event_id)
        return render_template('edit_event.html', event=event)
    elif request.method == 'GET':
        event = Event.query.get_or_404(event_id)
        return render_template('edit_event.html', event=event)
    
@app.route('/submit_event/<int:event_id>',methods = ['POST','GET'])
def submit_event(event_id):
    if request.method == 'POST':
        event =Event.query.get_or_404(event_id)
        new_name = request.form.get('name_event')
        new_start = request.form.get('start_date_time')
        new_end = request.form.get('end_date_time')
        new_venue = request.form.get('venue_')
        new_descr = request.form.get('description_event')
        new_budget = request.form.get('budget')
        new_status = request.form.get('status_event')
        new_winner = request.form.get('winner_id')
        db.session.delete(event)
        db.session.commit()
        new_event = Event(id=event_id,name_ = new_name,start_date_time = new_start,end_date_time = new_end,venue = new_venue,descr = new_descr,budget = int(new_budget),status = new_status,winner_id = int(new_winner))
        db.session.add(new_event)
        db.session.commit()
        events = Event.query.all()
        return render_template('update_event.html', events = events)
    elif request.method == 'GET':
        event =Event.query.get_or_404(event_id)
        new_name = request.form.get('name_event')
        new_start = request.form.get('start_date_time')
        new_end = request.form.get('end_date_time')
        new_venue = request.form.get('venue_')
        new_descr = request.form.get('description_event')
        new_budget = request.form.get('budget')
        new_status = request.form.get('status_event')
        new_winner = request.form.get('winner_id')
        db.session.delete(event)
        db.session.commit()
        new_event = Event(id=event_id,name_ = new_name,start_date_time = new_start,end_date_time = new_end,venue = new_venue,descr = new_descr,budget = int(new_budget),status = new_status,winner_id = int(new_winner))
        db.session.add(new_event)
        db.session.commit()
        events = Event.query.all()
        return render_template('update_event.html', events = events)
    
@app.route('/delete_event_org/<int:event_id>',methods = ['POST','GET'])
def delete_event_org(event_id):
    if request.method == 'POST':
        event = Event.query.get_or_404(event_id)
        if Participant.query.filter_by(eventid = event_id).all():
            part_ev=Participant.query.filter_by(eventid = event_id).all()
            db.session.delete(part_ev)
            db.session.commit()
        elif Volunteer.query.filter_by(eventid = event_id).all():
            vol_ev = Volunteer.query.filter_by(eventid = event_id).all()
            db.session.delete(vol_ev)
            db.session.commit()

        db.session.delete(event)
        db.session.commit()
        return render_template('update_event.html')
    elif request.method == 'GET':
        event = Event.query.get_or_404(event_id)
        if Participant.query.filter_by(eventid = event_id).all():
            part_ev=Participant.query.filter_by(eventid = event_id).all()
            db.session.delete(part_ev)
            db.session.commit()
        elif Volunteer.query.filter_by(eventid = event_id).all():
            vol_ev = Volunteer.query.filter_by(eventid = event_id).all()
            db.session.delete(vol_ev)
            db.session.commit()

        db.session.delete(event)
        db.session.commit()
        return render_template('update_event.html')

# app.route('/flash/<message>')
# def flash(message):
#     return render_template('flash.html', msg=message)




if __name__ == '__main__':
    app.run(debug=True)