from flask import Flask,redirect,render_template,session,request,flash,url_for,make_response
from weasyprint import HTML
import pymysql
app=Flask(__name__)

app.secret_key='yvvrcyeryueyruehddsnjnjn'
# connection=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='employee_data'
# )

connection=pymysql.connect(
    host='db4free.net',
    user='pension',
    password='pensionscheme',
    database='pension'
)

@app.route('/',methods=['POST','GET'])
def login():
    if 'username' and 'code' in session:
        flash('Please logout first to access login page','info')
        return redirect(url_for('home'))
    else:
        if request.method=='POST':
            name=request.form['name']
            code=request.form['code']
            if name=='' or code=='':
                flash('All fields are required','danger')
                return render_template('login.html',name=name,code=code)
            cur=connection.cursor()
            cur.execute('SELECT * FROM data WHERE M_NO=%s AND NAME=%s',(code,name,))
            data=cur.fetchone()
            connection.commit()
            if data:
                session['username']=data[2]
                session['code']=data[1]
                session['role']=data[3]
                return redirect(url_for('home'))
            else:
                flash('Wrong credentials','danger')
                return render_template('login.html',name=name,code=code)
        return render_template('login.html')


@app.route('/home')
def home():
    if 'username' and 'code' not in session:
        flash('Please login first','warning')
        return redirect(url_for('login'))
    else:
        name=session['username']
        code=session['code']
        cur=connection.cursor()
        cur.execute('SELECT * FROM data WHERE M_NO=%s AND NAME=%s',(code,name,))
        data=cur.fetchone()
        # if data[3]=='admin':
        #     return redirect(url_for('admin'))
        connection.commit()
        return render_template('home.html',data=data)
    return render_template('home.html',data=data)


@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/add')
def add():
    return render_template('add.html')




@app.route('/categories/<category>')
def categories(category):
    if 'username' and 'code' not in session:
        flash('Please login first','warning')
        return redirect(url_for('login'))
    else:
        if session['role']=='admin':
            cur=connection.cursor()
            cur.execute('SELECT * FROM data')
            data=cur.fetchall()
            if category=="Opening balance scb @1.07.2010":
                return render_template('category/ob_scb.html',datas=data)
            elif category=="Contributions remitted Year 2010-11":
                return render_template('category/remitted.html',datas=data)
            elif category=="bio":
                return render_template('category/bio.html',datas=data)
            elif category=="interest on opening balance scb 2010-11":
                return render_template('category/interest on opening balance scb.html',datas=data)
            elif category=="Interest on Contributions Year 2010-11":
                return render_template('category/Interest on Contributions Year.html',datas=data)
            elif category=="unremitted contributions":
                return render_template('category/unremitted contributions.html',datas=data)
            elif category=="Interest on unremitted contributions":
                return render_template('category/Interest on unremitted.html',datas=data)
            elif category=="INHRBS":
                return render_template('category/INHRBS.html',datas=data)
            elif category=="Interest due to INHRBS":
                return render_template('category/Interest due to INHRBS.html',datas=data)
            elif category=="NIC Funds @1.2.2011":
                return render_template('category/NIC Funds @1.2.2011.html',datas=data)
            elif category=="Interest due to NIC opening balance":
                return render_template('category/Interest due to NIC opening balance.html',datas=data)
        return "Not allowed"


@app.route('/category_pdf/<category>')
def category_pdf(category):
    if 'username' and 'code' not in session:
            flash('Please login first', 'warning')
            return redirect(url_for('login'))
    else:
        if session['role']=='admin':
            name = session['username']
            code = session['code']
            role=session['role']
            cur = connection.cursor()
            cur.execute('SELECT * FROM data WHERE M_NO=%s AND NAME=%s', (code, name,))
            data = cur.fetchone()
            connection.commit()
            base_url = request.base_url
            if role=="admin":
                cur.execute('SELECT * FROM data')
                data=cur.fetchall()
                if category=="Opening balance scb @1.07.2010":
                    html_content = render_template('category/ob_scb.html', datas=data, base_url=base_url)
                    pdf = HTML(string=html_content, base_url=base_url).write_pdf()
                    response = make_response(pdf)
                    response.headers['Content-Disposition'] = 'attachment; filename=Opening balance scb @1.07.2010.pdf'
                    response.headers['Content-Type'] = 'application/pdf'
                    return response
                elif category=="Contributions remitted Year 2010-11":
                    html_content = render_template('category/remitted.html', datas=data, base_url=base_url)
                    pdf = HTML(string=html_content, base_url=base_url).write_pdf()
                    response = make_response(pdf)
                    response.headers['Content-Disposition'] = 'attachment; filename=Contributions remitted Year 2010-11.pdf'
                    response.headers['Content-Type'] = 'application/pdf'
                    return response
                elif category=="bio":
                    html_content = render_template('category/bio.html', datas=data, base_url=base_url)
                    pdf = HTML(string=html_content, base_url=base_url).write_pdf()
                    response = make_response(pdf)
                    response.headers['Content-Disposition'] = 'attachment; filename=bio.pdf'
                    response.headers['Content-Type'] = 'application/pdf'
                    return response
                elif category=="interest on opening balance scb 2010-11":
                    html_content = render_template('category/interest on opening balance scb.html', datas=data, base_url=base_url)
                    pdf = HTML(string=html_content, base_url=base_url).write_pdf()
                    response = make_response(pdf)
                    response.headers['Content-Disposition'] = 'attachment; filename=interest on opening balance scb 2010-11.pdf'
                    response.headers['Content-Type'] = 'application/pdf'
                    return response
                elif category=="Interest on Contributions Year 2010-11":
                    html_content = render_template('category/Interest on Contributions Year.html', datas=data, base_url=base_url)
                    pdf = HTML(string=html_content, base_url=base_url).write_pdf()
                    response = make_response(pdf)
                    response.headers['Content-Disposition'] = 'attachment; filename=Interest on Contributions Year 2010-11.pdf'
                    response.headers['Content-Type'] = 'application/pdf'
                    return response
                elif category=="unremitted contributions":
                    html_content = render_template('category/unremitted contributions.html', datas=data, base_url=base_url)
                    pdf = HTML(string=html_content, base_url=base_url).write_pdf()
                    response = make_response(pdf)
                    response.headers['Content-Disposition'] = 'attachment; filename=unremitted contributions.pdf'
                    response.headers['Content-Type'] = 'application/pdf'
                    return response
                elif category=="Interest on unremitted contributions":
                    html_content = render_template('category/Interest on unremitted.html', datas=data, base_url=base_url)
                    pdf = HTML(string=html_content, base_url=base_url).write_pdf()
                    response = make_response(pdf)
                    response.headers['Content-Disposition'] = 'attachment; filename=Interest on unremitted contributions.pdf'
                    response.headers['Content-Type'] = 'application/pdf'
                    return response
                elif category=="INHRBS":
                    html_content = render_template('category/INHRBS.html', datas=data, base_url=base_url)
                    pdf = HTML(string=html_content, base_url=base_url).write_pdf()
                    response = make_response(pdf)
                    response.headers['Content-Disposition'] = 'attachment; filename=INHRBS.pdf'
                    response.headers['Content-Type'] = 'application/pdf'
                    return response
                elif category=="Interest due to INHRBS":
                    html_content = render_template('category/Interest due to INHRBS.html', datas=data, base_url=base_url)
                    pdf = HTML(string=html_content, base_url=base_url).write_pdf()
                    response = make_response(pdf)
                    response.headers['Content-Disposition'] = 'attachment; filename=Interest due to INHRBS.pdf'
                    response.headers['Content-Type'] = 'application/pdf'
                    return response
                elif category=="NIC Funds @1.2.2011":
                    html_content = render_template('category/NIC Funds @1.2.2011.html', datas=data, base_url=base_url)
                    pdf = HTML(string=html_content, base_url=base_url).write_pdf()
                    response = make_response(pdf)
                    response.headers['Content-Disposition'] = 'attachment; filename=NIC Funds @1.2.2011.pdf'
                    response.headers['Content-Type'] = 'application/pdf'
                    return response
                elif category=="Interest due to NIC opening balance":
                    html_content = render_template('category/Interest due to NIC opening balance.html', datas=data, base_url=base_url)
                    pdf = HTML(string=html_content, base_url=base_url).write_pdf()
                    response = make_response(pdf)
                    response.headers['Content-Disposition'] = 'attachment; filename=Interest due to NIC opening balance.pdf'
                    response.headers['Content-Type'] = 'application/pdf'
                    return response


@app.route('/download_pdf')
def download_pdf():
    if 'username' and 'code' not in session:
        flash('Please login first', 'warning')
        return redirect(url_for('login'))
    else:
        name = session['username']
        code = session['code']
        role=session['role']
        cur = connection.cursor()
        cur.execute('SELECT * FROM data WHERE M_NO=%s AND NAME=%s', (code, name,))
        data = cur.fetchone()
        connection.commit()
        base_url = request.base_url
        html_content = render_template('pdf.html', data=data, base_url=base_url)
        pdf = HTML(string=html_content, base_url=base_url).write_pdf()
        response = make_response(pdf)
        response.headers['Content-Disposition'] = 'attachment; filename=pension_scheme.pdf'
        response.headers['Content-Type'] = 'application/pdf'
        return response




@app.route('/logout')
def logout():
    if 'username' or 'code' in session:
        session.clear()
        flash('You have been logged out','warning')
        return redirect(url_for('login'))



if __name__=="__main__":
    app.run(debug=True,port=8001)

