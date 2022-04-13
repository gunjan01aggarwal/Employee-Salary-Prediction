import pickle
from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn


app = Flask(__name__)
model = pickle.load(open("Emp_salary_prediction.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("employee.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        #On which profile are working->
         Profile = request.form["Job Type"]
         if Profile == "CEO":
             CEO=1
             CFO=0
             CTO=0
             VICE_PRESIDENT=0
             MANAGER=0
             JUNIOR=0
             JANITOR=0

         elif Profile == "CFO":
             CEO=0
             CFO=1
             CTO=0
             VICE_PRESIDENT=0
             MANAGER=0
             JUNIOR=0
             JANITOR=0
         elif Profile == "CTO":
             CEO=0
             CFO=0
             CTO=1
             VICE_PRESIDENT=0
             MANAGER=0
             JUNIOR=0
             JANITOR=0
         elif Profile == "VICE_PRESIDENT":
             CEO=0
             CFO=0
             CTO=0
             VICE_PRESIDENT=1
             MANAGER=0
             JUNIOR=0
             JANITOR=0
         elif Profile == "MANAGER":
             CEO=0
             CFO=0
             CTO=0
             VICE_PRESIDENT=0
             MANAGER=1
             JUNIOR=0
             JANITOR=0
         elif Profile == "JUNIOR":
             CEO=0
             CFO=0
             CTO=0
             VICE_PRESIDENT=0
             MANAGER=0
             JUNIOR=1
             JANITOR=0
         else:
             CEO=0
             CFO=0
             CTO=0
             VICE_PRESIDENT=0
             MANAGER=0
             JUNIOR=0
             JANITOR=1

        #what's the highest qualifications?
         degree = request.form["Degree"]
         if degree == "DOCTORAL":
             DOCTORAL = 1
             MASTERS = 0
             BACHELORS = 0
             HIGH_SCHOOL = 0
             NONE=0
         elif degree == "MASTERS":
              DOCTORAL = 0
              MASTERS = 1
              BACHELORS = 0
              HIGH_SCHOOL = 0
              NONE = 0
         elif degree == "BACHELORS":
              DOCTORAL=0
              MASTERS=0
              BACHELORS = 1
              HIGH_SCHOOL = 0
              NONE = 0
         elif degree == "HIGH_SCHOOL":
              DOCTORAL=0
              MASTERS=0
              BACHELORS=0
              HIGH_SCHOOL=1
              NONE=0
         else:
              DOCTORAL=0
              MASTERS=0
              BACHELORS=0
              HIGH_SCHOOL=0
              NONE=1
        #How many experience do you have->
         Experience = int(request.form["Experience(in yrs)"])


        # Distance from metropolis->
         Distance = int(request.form["Distance from Metropolis (in miles)"])

        # Majority->
         Major= request.form["Major"]
         if Major =="MATH":
             MATH=1
             PHYSICS=0
             CHEMISTRY=0
             COMPSCI=0
             BIOLOGY=0
             LITERATURE=0
             BUSINESS=0
             ENGINEERING=0
             NONE=0
         elif Major =="PHYSICS":
             MATH=0
             PHYSICS=1
             CHEMISTRY=0
             COMPSCI=0
             BIOLOGY=0
             LITERATURE=0
             BUSINESS=0
             ENGINEERING=0
             NONE=0
         elif Major =="CHEMISTRY":
             MATH=0
             PHYSICS=0
             CHEMISTRY=1
             COMPSCI=0
             BIOLOGY=0
             LITERATURE=0
             BUSINESS=0
             ENGINEERING=0
             NONE=0
         elif Major =="COMPSCI":
             MATH=0
             PHYSICS=0
             CHEMISTRY=0
             COMPSCI=1
             BIOLOGY=0
             LITERATURE=0
             BUSINESS=0
             ENGINEERING=0
             NONE=0
         elif Major =="BIOLOGY":
             MATH=0
             PHYSICS=0
             CHEMISTRY=0
             COMPSCI=0
             BIOLOGY=1
             LITERATURE=0
             BUSINESS=0
             ENGINEERING=0
             NONE=0
         elif Major =="LITERATURE":
             MATH=0
             PHYSICS=0
             CHEMISTRY=0
             COMPSCI=0
             BIOLOGY=0
             LITERATURE=1
             BUSINESS=0
             ENGINEERING=0
             NONE=0
         elif Major =="BUSINESS":
             MATH=0
             PHYSICS=0
             CHEMISTRY=0
             COMPSCI=0
             BIOLOGY=1
             LITERATURE=0
             BUSINESS=0
             ENGINEERING=0
             NONE=0
         elif Major =="ENGINEERING":
             MATH=0
             PHYSICS=0
             CHEMISTRY=0
             COMPSCI=0
             BIOLOGY=0
             LITERATURE=0
             BUSINESS=0
             ENGINEERING=1
             NONE=0
         else:
             MATH=0
             PHYSICS=0
             CHEMISTRY=0
             COMPSCI=0
             BIOLOGY=0
             LITERATURE=0
             BUSINESS=0
             ENGINEERING=0
             NONE=1

    # In which industry working->
         Industry= request.form["Industry"]
         if Industry =="HEALTH":
             HEALTH=1
             WEB=0
             AUTO=0
             FINANCE=0
             EDUCATION=0
             OIL=0
             SERVICE=0
         elif Industry =="WEB":
             HEALTH=0
             WEB=1
             AUTO=0
             FINANCE=0
             EDUCATION=0
             OIL=0
             SERVICE=0
         elif Industry =="AUTO":
             HEALTH=0
             WEB=0
             AUTO=1
             FINANCE=0
             EDUCATION=0
             OIL=0
             SERVICE=0
         elif Industry == "FINANCE":
             HEALTH=0
             WEB=0
             AUTO=0
             FINANCE=1
             EDUCATION=0
             OIL=0
             SERVICE=0
         elif Industry == "EDUCATION":
              HEALTH=0
              WEB=0
              AUTO=0
              FINANCE=0
              EDUCATION=1
              OIL=0
              SERVICE=0
         elif Industry =="OIL":
              HEALTH=0
              WEB=0
              AUTO=0
              FINANCE=0
              EDUCATION=0
              OIL=1
              SERVICE=0
         else:
             HEALTH=0
             WEB=0
             AUTO=0
             FINANCE=0
             EDUCATION=0
             OIL=0
             SERVICE=1

         prediction=model.predict([[Profile,
             degree,
             Experience,
             Distance,
             MATH,
             PHYSICS,
             CHEMISTRY,
             BIOLOGY,
             COMPSCI,
             LITERATURE,
             BUSINESS,
             ENGINEERING,
             NONE,
             HEALTH,
             WEB,
             AUTO,
             FINANCE,
             EDUCATION,
             OIL,
             SERVICE
         ]])

         output=round(prediction[0],2)

         return render_template("employee.html", prediction_text="Predicted Salary : $ {}k".format(output))

    return render_template("employee.html")




if __name__ == "__main__":
    app.run(debug=True)

















