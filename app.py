from flask import Flask,render_template,request,jsonify
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


@app.route("/register", methods=["POST"])
def read_csv():
       
    if "file" not in request.files:
        return "No file uploaded"
    
    file=request.files["file"]

    if file.filename == "":
        return "Please select a file"

    if not file.filename.lower().endswith(".csv"):
        return "Only CSV files are allowed"

    try:
        df = pd.read_csv(file)
        if df.empty:
            return "CSV file is empty"
        
        required_columns = ["name", "maths", "science", "english"]

        for column in required_columns:
            if column not in df.columns:
                return f"Missing column: {column}"

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

        return render_template(
        "result.html", students=students,
        class_average=class_average,
        class_performer=class_performer,
        pass_percentage=pass_percentage
        )
    
    except pd.errors.EmptyDataError:
        return "CSV file is empty"

    except pd.errors.ParserError:
        return "Invalid CSV file"

    except Exception as e:
        return f"Error: {e}"
    


@app.route("/api/analyze", methods=["POST"])
def api_analyze():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No data provided"
        }), 400

    df = pd.DataFrame(data)

    df["total"] = df["maths"] + df["science"] + df["english"]

    df["average"] = df["total"] / 3

    df["grade"] = df["total"].apply(grade)

    class_average = df["average"].mean()

    class_performer = df.loc[
        df["average"].idxmax(),
        "name"
    ]

    pass_percentage = (df["total"] >= 150).mean() * 100

    return jsonify({
        "class_average": class_average,
        "class_performer": class_performer,
        "pass_percentage": pass_percentage
    })


if __name__ == "__main__":
    app.run(debug=True)