from main import app
from flask import render_template, request, redirect, url_for
#quando na rota só tem o "/" é pq é a pagina inicial do site
#para o render template funcionar, tem que ter o arquivo .html na pasta templates


#paginas
#abas
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/formulas")
def formulas():
    return render_template("formulas.html")
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")
@app.route("/contato")
def contato():
    return render_template("contato.html")
@app.route("/mru")
def mru():
    return render_template("mru.html")
#formulas
@app.route("/densidade")
def densidade():
    return render_template("densidade.html")
@app.route("/dilataçaolinear")
def dilatacao_linear():
    return render_template("dilataçaolinear.html")
@app.route("/bhaskara")
def bhaskara():
    return render_template("bhaskara.html")
@app.route("/2leinewton")
def lei_newton2():
    return render_template("2leinewton.html")
@app.route("/areatriangulo")
def areatriangulo():
    return render_template("areatriangulo.html")




#cauculos
#Calcular a densidade 
@app.route("/calculo_densidade", methods=["POST"])
def calculo_densidade():
    massa=float(request.form.get("massa"))
    volume=float(request.form.get("volume"))
    densidade=float(request.form.get("densidade"))
    if densidade==0 and volume!=0 and massa!=0:
        densidade1 = massa / volume
        return render_template("densidade.html", batata="Densidade: " + str(densidade1)+"(Kg/m³)")
    elif massa==0 and volume!=0 and densidade!=0:
        massa1 = densidade * volume
        return render_template("densidade.html", batata="Massa: " + str(massa1)+"kg")
    elif volume==0 and massa!=0 and densidade!=0:
        volume1 = massa / densidade
        return render_template("densidade.html", batata="Volume: " + str(volume1)+"m³")
    else:
        return render_template("densidade.html", batata="Erro: Preencha os campos corretamente.")
#dilatação linear
@app.route("/calculo_dilataçaolinear", methods=["POST"])
def calculo_dilataçao():
    icomprimento=float(request.form.get("icomprimento"))
    vtemperatura=float(request.form.get("vtemperatura"))
    coeficientedilataçaolinear=float(request.form.get("coeficientedilataçaolinear"))
    vcomprimento=float(request.form.get("vcomprimento"))
    if vcomprimento==0 and icomprimento!=0 and coeficientedilataçaolinear!=0 and vtemperatura!=0:
        vcomprimento1 = icomprimento * coeficientedilataçaolinear * vtemperatura
        return render_template("dilataçaolinear.html", placa="Comprimento: " + str(vcomprimento1)+"m")
    elif icomprimento==0 and vcomprimento!=0 and coeficientedilataçaolinear!=0 and vtemperatura!=0:
        icomprimento1 = vcomprimento / (coeficientedilataçaolinear * vtemperatura)
        return render_template("dilataçaolinear.html", placa="Comprimento inicial: " + str(icomprimento1)+"m")
    elif coeficientedilataçaolinear==0 and icomprimento!=0 and vcomprimento!=0 and vtemperatura!=0:
        coeficientedilataçaolinear1 = vcomprimento / (icomprimento * vtemperatura)
        return render_template("dilataçaolinear.html", placa="Coeficiente de dilatação linear: " + str(coeficientedilataçaolinear1))
    elif vtemperatura==0 and icomprimento!=0 and coeficientedilataçaolinear!=0 and vcomprimento!=0:
        vtemperatura1 = vcomprimento / (icomprimento * coeficientedilataçaolinear)
        return render_template("dilataçaolinear.html", placa="Variação de temperatura: " + str(vtemperatura1))
    else:
        return render_template("dilataçaolinear.html", placa="Erro: Preencha os campos corretamente.")
#bhaskara
@app.route("/calculo_bhaskara", methods=["POST"])
#obs: importante tomar cuidade para não repitir o nome da função
def calculo_bhaskara():
    a = float(request.form.get("a"))
    b = float(request.form.get("b"))
    c = float(request.form.get("c"))
    delta = (b**2) - (4*a*c)
    raiz = delta**(1/2)
    if a==0:
        x1 = (-b + raiz)
        x2 = (-b - raiz)
        return render_template("bhaskara.html", xs="X1: " + str(x1) + " e X2: " + str(x2))
    else:
        x1 = (-b + raiz) / (2*a)
        x2 = (-b - raiz) / (2*a)
        return render_template("bhaskara.html", xs="X1: " + str(x1) + " e X2: " + str(x2))
#2lei de newton
@app.route("/calculo_2leinewton", methods=["POST"])
def calculo_leinewton2():
    massa = float(request.form.get("massa"))
    acel = float(request.form.get("acel"))
    forca = float(request.form.get("força"))
    if forca==0 and massa!=0 and acel!=0:
        forca1 = massa * acel
        return render_template("2leinewton.html", maça="Força: " + str(forca1) + "N")
    elif massa==0 and forca!=0 and acel!=0:
        massa1 = forca / acel
        return render_template("2leinewton.html", maça="Massa: " + str(massa1) + "kg")
    elif acel==0 and massa!=0 and forca!=0:
        acel1 = forca / massa
        return render_template("2leinewton.html", maça="Aceleração: " + str(acel1) + "m/s²")
    else:
        return render_template("2leinewton.html", maça="Erro: Preencha os campos corretamente.")
<<<<<<< HEAD
#MRU
@app.route("/calculo_mru", methods=["POST"])
def calculo_mru():
    dpercorrida= float(request.form.get("dpercorrida"))
    tempo= float(request.form.get("tempo"))
    velocidade= float(request.form.get("velocidade"))
    if dpercorrida==0 and tempo!=0 and velocidade!=0:
        pfinal1 = velocidade * tempo
        return render_template("mru.html", mru="Distância percorrida: " + str(pfinal1) + "m")
    elif tempo==0 and dpercorrida!=0 and velocidade!=0:
        tempo1 = dpercorrida / velocidade
        return render_template("mru.html", mru="Tempo: " + str(tempo1) + "s")
    elif velocidade==0 and dpercorrida!=0 and tempo!=0:
        velocidade1 = dpercorrida / tempo
        return render_template("mru.html", mru="Velocidade: " + str(velocidade1) + "m/s")
    else:
        return render_template("mru.html", mru="Erro: Preencha os campos corretamente.")
=======
#Area do triangulo
@app.route("/calculo_areatriangulo", methods=["POST"])
def cauculo_areatriangulo():
    base=float(request.form.get("base"))
    altura=float(request.form.get("altura"))
    if base!=0 or altura!=0:
        area1=(base*altura)/2
        return render_template("areatriangulo.html", area= "A área do triângulo é:" + str(area1))
    else:
        return render_template("areatriangulo.html", area= "Erro: Preencha os campos corretamente.")


>>>>>>> d8698fa75662ccca53f5c66393e408c617f7e323
