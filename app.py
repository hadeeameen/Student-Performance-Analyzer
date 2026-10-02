from flask import Flask,render_template,request
import pandas as pd

app = Flask(__name__)


def grade(mark):
    if mark >= 270:
        return "A"
    elif mark >= 240:
        return "B"
    elif mark >= 200:
        return "C"
    elif mark >= 150:
        return "D"
    else:
        return "F"
    

@app.route("/")
def form():
    return render_template("form.html")

# bnbb


@app.route("/register", methods=["POST"])
def read_csv():

    
    file=request.files["file"]
    df=pd.read_csv(file)

    df["total"]=df["maths"]+df["science"]+df["english"]

    df["average"] = df["total"]/3

    df["grade"]=df["total"].apply(grade)

    print(df)

    class_average = df["average"].mean()
    print("Class Average:", class_average)

    class_performer = df.loc[df["average"].idxmax(),"name"]
    print("Class Performer:", class_performer)

    pass_percentage = (df["total"]>=150).mean()*100
    print("Pass Percentage:", pass_percentage)

    students=df.to_dict(orient="records")

    return render_template("result.html", students=students, class_average=class_average, class_performer=class_performer, pass_percentage=pass_percentage)
if __name__ == "__main__":
    app.run(debug=True)