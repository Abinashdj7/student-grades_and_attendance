from flask import Flask, jsonify, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__,template_folder='C:\\Users\\abi11\\Abinash_Sasikumar_S1_project\\site\\templates')
db = mysql.connector.connect(
    host="localhost", username="root", password="", database="epi_db_s1"
)


@app.route("/")
def index():
    query1 = "select count(*) from students where student_population_code_ref='ISM' group by student_population_year_ref "
    cursor1 = db.cursor()
    cursor1.execute(query1)
    ISM_count = cursor1.fetchall()
    query2 = "select count(*) from students where student_population_code_ref='DSA' group by student_population_year_ref "
    cursor2 = db.cursor()
    cursor2.execute(query2)
    DSA_count = cursor2.fetchall()
    query3 = "select count(*) from students where student_population_code_ref='CS' group by student_population_year_ref "
    cursor3 = db.cursor()
    cursor3.execute(query3)
    CS_count = cursor3.fetchall()
    query4 = "select count(*) from students where student_population_code_ref='SE' group by student_population_year_ref "
    cursor4 = db.cursor()
    cursor4.execute(query4)
    SE_count = cursor4.fetchall()
    query5 = "select count(*) from students where student_population_code_ref='AIs' group by student_population_year_ref "
    cursor5 = db.cursor()
    cursor5.execute(query5)
    AIs_count = cursor5.fetchall()
    todos = (
        [
            ISM_count[0][0],
            DSA_count[0][0],
            CS_count[0][0],
            SE_count[0][0],
            AIs_count[0][0],
        ],
        [
            ISM_count[1][0],
            DSA_count[1][0],
            CS_count[1][0],
            SE_count[1][0],
            AIs_count[1][0],
        ],
    )
    query6_0_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='ISM'and s.student_population_year_ref='2020' group by s.student_epita_email;"
    cursor6_0_2020 = db.cursor()
    cursor6_0_2020.execute(query6_0_2020)
    attendance_ISM_present_2020 = cursor6_0_2020.fetchall()
    query_6_1_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='ISM' and s.student_population_year_ref='2020'"
    cursor6_1_2020 = db.cursor()
    cursor6_1_2020.execute(query_6_1_2020)
    attendance_ISM_total_2020 = cursor6_1_2020.fetchall()
    attendance_ISM_present_sum_2020 = [
        attendance_ISM_present_2020[i][0]
        for i in range(len(attendance_ISM_present_2020))
    ]
    attendance_ISM_2020 = (
        sum(attendance_ISM_present_sum_2020) / attendance_ISM_total_2020[0][0]
    ) * 100
    query6_0_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='ISM'and s.student_population_year_ref='2021' group by s.student_epita_email;"
    cursor6_0_2021 = db.cursor()
    cursor6_0_2021.execute(query6_0_2021)
    attendance_ISM_present_2021 = cursor6_0_2021.fetchall()
    query_6_1_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='ISM' and s.student_population_year_ref='2021'"
    cursor6_1_2021 = db.cursor()
    cursor6_1_2021.execute(query_6_1_2021)
    attendance_ISM_total_2021 = cursor6_1_2021.fetchall()
    attendance_ISM_present_sum_2021 = [
        attendance_ISM_present_2021[i][0]
        for i in range(len(attendance_ISM_present_2021))
    ]
    attendance_ISM_2021 = (
        sum(attendance_ISM_present_sum_2021) / attendance_ISM_total_2021[0][0]
    ) * 100
    query7_0_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='DSA' and s.student_population_year_ref='2020' group by s.student_epita_email;"
    cursor7_0_2020 = db.cursor()
    cursor7_0_2020.execute(query7_0_2020)
    attendance_DSA_present_2020 = cursor7_0_2020.fetchall()
    query7_1_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='DSA' and s.student_population_year_ref='2020'"
    cursor7_1_2020 = db.cursor()
    cursor7_1_2020.execute(query7_1_2020)
    attendance_DSA_total_2020 = cursor7_1_2020.fetchall()
    attendance_DSA_present_sum_2020 = [
        attendance_DSA_present_2020[i][0]
        for i in range(len(attendance_DSA_present_2020))
    ]
    attendance_DSA_2020 = (
        sum(attendance_DSA_present_sum_2020) / attendance_DSA_total_2020[0][0]
    ) * 100
    query7_0_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='DSA' and s.student_population_year_ref='2021' group by s.student_epita_email;"
    cursor7_0_2021 = db.cursor()
    cursor7_0_2021.execute(query7_0_2021)
    attendance_DSA_present_2021 = cursor7_0_2021.fetchall()
    query7_1_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='DSA' and s.student_population_year_ref='2021'"
    cursor7_1_2021 = db.cursor()
    cursor7_1_2021.execute(query7_1_2021)
    attendance_DSA_total_2021 = cursor7_1_2021.fetchall()
    attendance_DSA_present_sum_2021 = [
        attendance_DSA_present_2021[i][0]
        for i in range(len(attendance_DSA_present_2021))
    ]
    attendance_DSA_2021 = (
        sum(attendance_DSA_present_sum_2021) / attendance_DSA_total_2021[0][0]
    ) * 100
    query8_0_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='CS' and s.student_population_year_ref='2020' group by s.student_epita_email;"
    cursor8_0_2020 = db.cursor()
    cursor8_0_2020.execute(query8_0_2020)
    attendance_CS_present_2020 = cursor8_0_2020.fetchall()
    query8_1_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='CS' and s.student_population_year_ref='2020'"
    cursor8_1_2020 = db.cursor()
    cursor8_1_2020.execute(query8_1_2020)
    attendance_CS_total_2020 = cursor8_1_2020.fetchall()
    attendance_CS_present_sum_2020 = [
        attendance_CS_present_2020[i][0] for i in range(len(attendance_CS_present_2020))
    ]
    attendance_CS_2020 = (
        sum(attendance_CS_present_sum_2020) / attendance_CS_total_2020[0][0]
    ) * 100
    query8_0_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='CS' and s.student_population_year_ref='2021' group by s.student_epita_email;"
    cursor8_0_2021 = db.cursor()
    cursor8_0_2021.execute(query8_0_2021)
    attendance_CS_present_2021 = cursor8_0_2021.fetchall()
    query8_1_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='CS' and s.student_population_year_ref='2021'"
    cursor8_1_2021 = db.cursor()
    cursor8_1_2021.execute(query8_1_2021)
    attendance_CS_total_2021 = cursor8_1_2021.fetchall()
    attendance_CS_present_sum_2021 = [
        attendance_CS_present_2021[i][0] for i in range(len(attendance_CS_present_2021))
    ]
    attendance_CS_2021 = (
        sum(attendance_CS_present_sum_2021) / attendance_CS_total_2021[0][0]
    ) * 100
    query9_0_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='SE' and s.student_population_year_ref='2020' group by s.student_epita_email;"
    cursor9_0_2020 = db.cursor()
    cursor9_0_2020.execute(query9_0_2020)
    attendance_SE_present_2020 = cursor9_0_2020.fetchall()
    query9_1_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='SE' and s.student_population_year_ref='2020'"
    cursor9_1_2020 = db.cursor()
    cursor9_1_2020.execute(query9_1_2020)
    attendance_SE_total_2020 = cursor9_1_2020.fetchall()
    attendance_SE_present_sum_2020 = [
        attendance_SE_present_2020[i][0] for i in range(len(attendance_SE_present_2020))
    ]
    attendance_SE_2020 = (
        sum(attendance_SE_present_sum_2020) / attendance_SE_total_2020[0][0]
    ) * 100
    query9_0_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='SE' and s.student_population_year_ref='2021' group by s.student_epita_email;"
    cursor9_0_2021 = db.cursor()
    cursor9_0_2021.execute(query9_0_2021)
    attendance_SE_present_2021 = cursor9_0_2021.fetchall()
    query9_1_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='SE' and s.student_population_year_ref='2021'"
    cursor9_1_2021 = db.cursor()
    cursor9_1_2021.execute(query9_1_2021)
    attendance_SE_total_2021 = cursor9_1_2021.fetchall()
    attendance_SE_present_sum_2021 = [
        attendance_SE_present_2021[i][0] for i in range(len(attendance_SE_present_2021))
    ]
    attendance_SE_2021 = (
        sum(attendance_SE_present_sum_2021) / attendance_SE_total_2021[0][0]
    ) * 100
    query10_0_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='AIs' and s.student_population_year_ref='2020' group by s.student_epita_email;"
    cursor10_0_2020 = db.cursor()
    cursor10_0_2020.execute(query10_0_2020)
    attendance_AIs_present_2020 = cursor10_0_2020.fetchall()
    query10_1_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='AIs' and s.student_population_year_ref='2020'"
    cursor10_1_2020 = db.cursor()
    cursor10_1_2020.execute(query10_1_2020)
    attendance_AIs_total_2020 = cursor10_1_2020.fetchall()
    attendance_AIs_present_sum_2020 = [
        attendance_AIs_present_2020[i][0]
        for i in range(len(attendance_AIs_present_2020))
    ]
    attendance_AIs_2020 = (
        sum(attendance_AIs_present_sum_2020) / attendance_AIs_total_2020[0][0]
    ) * 100
    query10_0_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='AIs' and s.student_population_year_ref='2021' group by s.student_epita_email;"
    cursor10_0_2021 = db.cursor()
    cursor10_0_2021.execute(query10_0_2021)
    attendance_AIs_present_2021 = cursor10_0_2021.fetchall()
    query10_1_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='AIs' and s.student_population_year_ref='2021'"
    cursor10_1_2021 = db.cursor()
    cursor10_1_2021.execute(query10_1_2021)
    attendance_AIs_total_2021 = cursor10_1_2021.fetchall()
    attendance_AIs_present_sum_2021 = [
        attendance_AIs_present_2021[i][0]
        for i in range(len(attendance_AIs_present_2021))
    ]
    attendance_AIs_2021 = (
        sum(attendance_AIs_present_sum_2021) / attendance_AIs_total_2021[0][0]
    ) * 100
    attendance = [
        [
            attendance_ISM_2020,
            attendance_DSA_2020,
            attendance_CS_2020,
            attendance_SE_2020,
            attendance_AIs_2020,
        ],
        [
            attendance_ISM_2021,
            attendance_DSA_2021,
            attendance_CS_2021,
            attendance_SE_2021,
            attendance_AIs_2021,
        ],
    ]
    return render_template("index.html", todos=todos, attendance=attendance)


@app.route("/attendance")
def piechart_data():
    query1 = "select count(*) from students where student_population_code_ref='ISM' group by student_population_year_ref "
    cursor1 = db.cursor()
    cursor1.execute(query1)
    ISM_count = cursor1.fetchall()
    query2 = "select count(*) from students where student_population_code_ref='DSA' group by student_population_year_ref "
    cursor2 = db.cursor()
    cursor2.execute(query2)
    DSA_count = cursor2.fetchall()
    query3 = "select count(*) from students where student_population_code_ref='CS' group by student_population_year_ref "
    cursor3 = db.cursor()
    cursor3.execute(query3)
    CS_count = cursor3.fetchall()
    query4 = "select count(*) from students where student_population_code_ref='SE' group by student_population_year_ref "
    cursor4 = db.cursor()
    cursor4.execute(query4)
    SE_count = cursor4.fetchall()
    query5 = "select count(*) from students where student_population_code_ref='AIs' group by student_population_year_ref "
    cursor5 = db.cursor()
    cursor5.execute(query5)
    AIs_count = cursor5.fetchall()
    todos = [
        [
            ISM_count[0][0],
            DSA_count[0][0],
            CS_count[0][0],
            SE_count[0][0],
            AIs_count[0][0],
        ],
        [
            ISM_count[1][0],
            DSA_count[1][0],
            CS_count[1][0],
            SE_count[1][0],
            AIs_count[1][0],
        ],
    ]
    return todos


@app.route("/population_2020_ISM.html")
def population_2020_ISM():
    return render_template("population_2020_ISM.html")


@app.route("/population_2020_DSA.html")
def population_2020_DSA():
    return render_template("population_2020_DSA.html")


@app.route("/population_2020_CS.html")
def population_2020_CS():
    return render_template("population_2020_CS.html")


@app.route("/population_2020_SE.html")
def population_2020_SE():
    return render_template("population_2020_SE.html")


@app.route("/population_2020_AIs.html")
def population_2020_AIs():
    return render_template("population_2020_AIs.html")


@app.route("/population_2021_ISM.html")
def population_2021_ISM():
    return render_template("population_2021_ISM.html")


@app.route("/population_2021_DSA.html")
def population_2021_DSA():
    return render_template("population_2021_DSA.html")


@app.route("/population_2021_CS.html")
def population_2021_CS():
    return render_template("population_2021_CS.html")


@app.route("/population_2021_SE.html")
def population_2021_SE():
    return render_template("population_2021_SE.html")


@app.route("/population_2021_AIs.html")
def population_2021_AIs():
    return render_template("population_2021_AIs.html")


@app.route("/population/2020/ISM")
def population_2020_ISM_fetch():
    query = "select s.student_epita_email,COUNT(CASE WHEN g.grade_score > 9 THEN 1 ELSE NULL END) from grades g LEFT JOIN students s ON s.student_epita_email = g.grade_student_epita_email_ref WHERE s.student_population_code_ref = 'ISM' and s.student_population_year_ref='2020' GROUP BY g.grade_student_epita_email_ref"
    cursor = db.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas


@app.route("/population/2020/DSA")
def population_2020_DSA_fetch():
    query = "select s.student_epita_email,COUNT(CASE WHEN g.grade_score > 9 THEN 1 ELSE NULL END) from grades g LEFT JOIN students s ON s.student_epita_email = g.grade_student_epita_email_ref WHERE s.student_population_code_ref = 'DSA' and s.student_population_year_ref='2020' GROUP BY g.grade_student_epita_email_ref"
    cursor = db.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas


@app.route("/population/2020/CS")
def population_2020_CS_fetch():
    query = "select s.student_epita_email,COUNT(CASE WHEN g.grade_score > 9 THEN 1 ELSE NULL END) from grades g LEFT JOIN students s ON s.student_epita_email = g.grade_student_epita_email_ref WHERE s.student_population_code_ref = 'CS' and s.student_population_year_ref='2020' GROUP BY g.grade_student_epita_email_ref"
    cursor = db.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas


@app.route("/population/2020/SE")
def population_2020_SE_fetch():
    query = "select s.student_epita_email,COUNT(CASE WHEN g.grade_score > 9 THEN 1 ELSE NULL END) from grades g LEFT JOIN students s ON s.student_epita_email = g.grade_student_epita_email_ref WHERE s.student_population_code_ref = 'SE' and s.student_population_year_ref='2020' GROUP BY g.grade_student_epita_email_ref"
    cursor = db.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas


@app.route("/population/2020/AIs")
def population_2020_AIs_fetch():
    query = "select s.student_epita_email,COUNT(CASE WHEN g.grade_score > 9 THEN 1 ELSE NULL END) from grades g LEFT JOIN students s ON s.student_epita_email = g.grade_student_epita_email_ref WHERE s.student_population_code_ref = 'AIs' and s.student_population_year_ref='2020' GROUP BY g.grade_student_epita_email_ref"
    cursor = db.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas


@app.route("/population/2021/ISM")
def population_2021_ISM_fetch():
    query = "select s.student_epita_email,COUNT(CASE WHEN g.grade_score > 9 THEN 1 ELSE NULL END) from grades g LEFT JOIN students s ON s.student_epita_email = g.grade_student_epita_email_ref WHERE s.student_population_code_ref = 'ISM' and s.student_population_year_ref='2021' GROUP BY g.grade_student_epita_email_ref"
    cursor = db.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas


@app.route("/population/2021/DSA")
def population_2021_DSA_fetch():
    query = "select s.student_epita_email,COUNT(CASE WHEN g.grade_score > 9 THEN 1 ELSE NULL END) from grades g LEFT JOIN students s ON s.student_epita_email = g.grade_student_epita_email_ref WHERE s.student_population_code_ref = 'DSA' and s.student_population_year_ref='2021' GROUP BY g.grade_student_epita_email_ref"
    cursor = db.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas


@app.route("/population/2021/CS")
def population_2021_CS_fetch():
    query = "select s.student_epita_email,COUNT(CASE WHEN g.grade_score > 9 THEN 1 ELSE NULL END) from grades g LEFT JOIN students s ON s.student_epita_email = g.grade_student_epita_email_ref WHERE s.student_population_code_ref = 'CS' and s.student_population_year_ref='2021' GROUP BY g.grade_student_epita_email_ref"
    cursor = db.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas


@app.route("/population/2021/SE")
def population_2021_SE_fetch():
    query = "select s.student_epita_email,COUNT(CASE WHEN g.grade_score > 9 THEN 1 ELSE NULL END) from grades g LEFT JOIN students s ON s.student_epita_email = g.grade_student_epita_email_ref WHERE s.student_population_code_ref = 'SE' and s.student_population_year_ref='2021' GROUP BY g.grade_student_epita_email_ref"
    cursor = db.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas


@app.route("/population/2021/AIs")
def population_2021_AIs_fetch():
    query = "select s.student_epita_email,COUNT(CASE WHEN g.grade_score > 9 THEN 1 ELSE NULL END) from grades g LEFT JOIN students s ON s.student_epita_email = g.grade_student_epita_email_ref WHERE s.student_population_code_ref = 'AIs' and s.student_population_year_ref='2021' GROUP BY g.grade_student_epita_email_ref"
    cursor = db.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas


@app.route("/course/ISM")
def courses_ISM():
    query = "select c.course_name,c.duration  from programs p left join courses c on p.program_course_code_ref=c.course_code where p.program_assignment='ISM' ;"
    cursor = db.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas


@app.route("/course/DSA")
def courses_DSA():
    query = "select c.course_name,c.duration  from programs p left join courses c on p.program_course_code_ref=c.course_code where p.program_assignment='DSA' ;"
    cursor = db.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas


@app.route("/course/CS")
def courses_CS():
    query = "select c.course_name,c.duration  from programs p left join courses c on p.program_course_code_ref=c.course_code where p.program_assignment='CS' ;"
    cursor = db.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas


@app.route("/course/SE")
def courses_SE():
    query = "select c.course_name,c.duration  from programs p left join courses c on p.program_course_code_ref=c.course_code where p.program_assignment='SE' ;"
    cursor = db.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas


@app.route("/course/AIs")
def courses_AIs():
    query = "select c.course_name,c.duration  from programs p left join courses c on p.program_course_code_ref=c.course_code where p.program_assignment='AIs' ;"
    cursor = db.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas


@app.route("/student.html")
def student():
    return render_template("student.html")


@app.route("/student", methods=["GET"])
def student_fetch():
    email = request.args.get("email")
    query = f"select s.student_epita_email,c.course_name,g.grade_score  from programs p left join grades g on g.grade_course_rev_ref = p.program_course_rev_ref left join courses c on p.program_course_code_ref=c.course_code left join students s on s.student_population_code_ref = p.program_assignment where s.student_epita_email='{email}'; "
    cursor = db.cursor()
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas


if __name__ == "__main__":
    app.run(debug=True)
