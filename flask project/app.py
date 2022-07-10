from distutils.log import info
from re import T
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")
database={"sidd":"123","jeams":"456"}

@app.route('/login',methods=['POST','GET'])

def login():
    name=request.form['username']
    pwd=request.form['password']
    if name not in database:
        return render_template("index.html",info="Invalid user")
    else:
        if database[name]!=pwd:
            return render_template("index.html",info='Invalid password')
        else:
            return render_template('home.html',name=name)
    
@app.route('/login/BMI',methods=['GET','POST'])
def BMI():
    bmi=""
    if request.method=="POST" and "weight" in request.form and "height" in request.form:
        w=float(request.form.get("weight"))
        h=float(request.form.get("height"))
        bmi=w/((h/100)**2)
    return render_template("g.html",bmi=bmi)

@app.route('/login/Accelaration gravity',methods=['GET','POST'])
def Accelarationgravity():
    g=""
    if request.method=='POST' and "Mass of the object" in request.form and "The distance from the center of mass of the large body" in request.form:
        M=float(request.form.get("Mass of the object"))
        r=float(request.form.get("The distance from the center of mass of the large body"))
        G=6.67E-11
        g=(G*M)/(r**2)
    return render_template("A.html",g=g)
@app.route('/login/surfacetension',methods=['GET','POST'])
def surfacetension():
    surfacetension=""
    if request.method=='POST' and "density" in request.form and "highht" in request.form and "readious" in request.form:
        density=float(request.form.get("density"))
        highht=float(request.form.get("highht"))
        readious=float(request.form.get("readious"))
        G=9.8
        z=density*highht*readious*G
        surfacetension=z/2

    return render_template("s.html",surfacetension=surfacetension)

    
    

if __name__=="__main__":
    app.run(debug=True)