# app.py
import datetime
from flask import Flask, render_template, request
import Setting
import psycopg2
app = Flask(__name__)

#user registration
@app.route('/register')
def user():
    return render_template('user.html',question=Setting.question_for_magicword)

@app.route('/select/<num>')
def select(num):
    return render_template("select.html", licensenum=num)
    
@app.route('/checkin',methods = ['GET'])
def checkin():
    con=psycopg2.connect(Setting.credentials)
    cur=con.cursor()
    licensenum=request.args.get('licenseID')
    cur.execute("SELECT CheckOutTime FROM reserve WHERE licenseID = %s ORDER BY CheckOutTime DESC LIMIT 1", (licensenum,))
    data=cur.fetchone()
    latest=data[0]
    try:
        a=request.args.get('licenseID')
        b=request.args.get('user_ID')
        c=datetime.datetime.now()
        d=c+datetime.timedelta(hours=Setting.add_time)     
        if latest<c:
            cur.execute("INSERT INTO reserve (licenseid, studentid, checkintime, checkouttime) VALUES (%s,%s,%s,%s)", (a,b,c,d))
            retval=Setting.sufa.success
            reason=Setting.reason.checkin_success
        else:
            retval=Setting.sufa.fail
            reason=Setting.reason.checkin_fail_still_using
    except:
        con.rollback()
        retval=Setting.sufa.fail
        reason=Setting.reason.db_access_fail
    finally:
        cur.close()
        con.commit()
        con.close()
        return render_template("result.html",msg=retval, reason=reason )

@app.route('/license/<licensenum>')
def license(licensenum):
    db=psycopg2.connect(Setting.credentials)
    cur=db.cursor()
    cur.execute("SELECT * FROM reserve INNER JOIN users ON reserve.StudentID = users.StudentID WHERE licenseID = %s ORDER BY checkouttime DESC LIMIT 20",(licensenum,))    
    rows=cur.fetchall()
    cur.close()
    db.close()
    return render_template("showreserve.html",rows=rows, licensenum=licensenum)

@app.route('/user_info',methods = ['POST', 'GET'])
def user_info():
    if request.method == 'POST':
        try:
            db=psycopg2.connect(Setting.credentials)
            cur=db.cursor()
            user_ID = request.form['user_ID']
            user_name = request.form['user_name']
            user_phone= request.form['phonenumber']
            #evaluating if student is actually in class
            magicword = request.form['magicword']
            if magicword==Setting.magicword:
                cur.execute("INSERT INTO users (studentid, name, phonenum) VALUES (%s, %s, %s)",(user_ID,user_name, user_phone) )
                msg = Setting.sufa.success
                reason=Setting.reason.register_success
            else:
                msg = Setting.sufa.fail
                reason=Setting.reason.magicfail

        except:
            msg = Setting.sufa.fail
            reason=Setting.reason.db_access_fail

        finally:
            cur.close()
            db.commit()
            db.close()
            return render_template("result.html",msg = msg, reason = reason)
            


@app.route('/reservation/<licensenum>')
def reservation(licensenum):
    db=psycopg2.connect(Setting.credentials)
    cur=db.cursor()
    cur.execute("SELECT * FROM reserve WHERE licenseID=%s ORDER BY CheckOutTime DESC LIMIT 1",(licensenum,))
    data=cur.fetchone()
    cur.execute("SELECT * FROM users WHERE StudentID = %s",(data[1],))
    data2=cur.fetchone()
    cur.close()
    db.close()
    return render_template('reservation.html',rows=data[3], rows2=data2[1],licensenum=licensenum)

@app.route('/extension/<licensenum>', methods=['POST','GET'])
def extender(licensenum):
    try:
        db=psycopg2.connect(Setting.credentials)
        cur=db.cursor()
        cur.execute("SELECT * FROM reserve WHERE licenseID = %s ORDER BY CheckOutTime DESC LIMIT 1", (licensenum,))
        data=cur.fetchone()
        cur.execute("SELECT * FROM users WHERE StudentID = %s",(data[1],))
        data2=cur.fetchone()
        if request.method=='POST':
            try:
                userID=request.form['user_ID']
                if userID==data[1]:
                    cur.execute("SELECT CheckInTime FROM reserve WHERE licenseID = %s ORDER BY CheckOutTime DESC LIMIT 1",(licensenum,))
                    data3=cur.fetchall()
                    older=data3[0][0]
                    cur.execute("SELECT CheckOutTime FROM reserve WHERE licenseID = %s ORDER BY CheckOutTime DESC LIMIT 1",(licensenum,))
                    data3=cur.fetchall()
                    latest=data3[0][0]
                    newtime=latest+datetime.timedelta(hours=Setting.add_time)
                    if newtime-older<datetime.timedelta(hours=Setting.max_time):
                        cur.execute("INSERT INTO reserve (licenseid, studentid, checkintime, checkouttime) VALUES (%s, %s, %s, %s);", (licensenum, userID, older, newtime,))
                        reason=Setting.reason.extend_success
                        msg=Setting.sufa.success
                        return render_template('result.html', msg="Sucess", reason="잘됨")
                    else :
                        msg=Setting.sufa.fail
                        reason=Setting.reason.extend_fail
                        return render_template('result.html', msg="Error", reason = "8시간 초과")
                    
                else:
                    msg=Setting.sufa.fail
                    reason=Setting.reason.youre_not_the_one
                    return render_template('result.html',msg="Error",reason="현 사용자의 학번이 아닙니다.")
            except:
                msg=Setting.sufa.fail
                reason=Setting.reason.db_write_fail
            return render_template('result.html', msg=msg, reason=reason)
        else:
            pass
    except:
        msg=Setting.sufa.fail
        reason=Setting.reason.db_access_fail
        db.rollback()
        cur.close()
        db.close()
        return render_template('result.html',msg=msg,reason=reason)
        

    finally:    
        cur.close()
        db.commit()
        db.close()
    return render_template('extension.html',rows=data[3], rows2=data2[1], licensenum=licensenum)



@app.route('/')
def index():
    return render_template('index.html')
