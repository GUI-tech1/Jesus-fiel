from main import app
from flask import render_template, request, redirect, url_for
from decimal import Decimal
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



#formulas
@app.route("/velocidademedia")
def velocidademedia():
    return render_template("velocidademedia.html")
@app.route("/densidade")
def densidade():
    return render_template("densidade.html")
@app.route("/dilataçaotermica")
def dilatacao_termica():
    return render_template("dilataçaotermica.html")
@app.route("/bhaskara")
def bhaskara():
    return render_template("bhaskara.html")
@app.route("/2leinewton")
def lei_newton2():
    return render_template("2leinewton.html")
@app.route("/mru")
def mru():
    return render_template("mru.html")
@app.route("/areatriangulo")
def areatriangulo():
    return render_template("areatriangulo.html")




#cauculos
#velocidade media
@app.route("/calculo_velocidademedia", methods=["POST"])
def calculo_velocidademedia():
    distancia = Decimal(request.form.get("distancia"))
    tempo = Decimal(request.form.get("tempo"))
    if distancia != 0 and tempo != 0:
        velocidademedia = distancia / tempo
        velocidademedia_f = format(velocidademedia, 'f')
        return render_template("velocidademedia.html", vmedia="Velocidade média: " + str(velocidademedia_f) + " m/s")
    else:
        return render_template("velocidademedia.html", vmedia="Erro: Preencha os campos corretamente.")
#Calcular a densidade 
@app.route("/calculo_densidade", methods=["POST"])
def calculo_densidade():
    massa=Decimal(request.form.get("massa"))
    volume=Decimal(request.form.get("volume"))
    densidade=Decimal(request.form.get("densidade"))
    if densidade==0 and volume!=0 and massa!=0:
        densidade1 = massa / volume
        densidade1_f = format(densidade1, 'f')
        return render_template("densidade.html", vdensidade="Densidade: " + str(densidade1_f)+"( Kg/m³)")
    elif massa==0 and volume!=0 and densidade!=0:
        massa1 = densidade * volume
        massa1_f = format(massa1, 'f')
        return render_template("densidade.html", vdensidade="Massa: " + str(massa1_f)+" kg")
    elif volume==0 and massa!=0 and densidade!=0:
        volume1 = massa / densidade
        volume1_f = format(volume1, 'f')
        return render_template("densidade.html", vdensidade="Volume: " + str(volume1_f)+" m³")
    else:
        return render_template("densidade.html", vdensidade="Erro: Preencha os campos corretamente.")
#dilatação Termica
@app.route("/calculo_dilataçaotermica", methods=["POST"])
def calculo_dilataçao():
    icomprimento=Decimal(request.form.get("icomprimento"))
    vtemperatura=Decimal(request.form.get("vtemperatura"))
    coeficientedilataçaotermica=Decimal(request.form.get("coeficientedilataçaotermica"))
    vcomprimento=Decimal(request.form.get("vcomprimento"))
    if vcomprimento==0 and icomprimento!=0 and coeficientedilataçaotermica!=0 and vtemperatura!=0:
        vcomprimento1 = icomprimento * coeficientedilataçaotermica * vtemperatura
        vcomprimento1_f = format(vcomprimento1, 'f')
        return render_template("dilataçaotermica.html", dtermica="Comprimento: " + str(vcomprimento1_f)+" m")
    elif icomprimento==0 and vcomprimento!=0 and coeficientedilataçaotermica!=0 and vtemperatura!=0:
        icomprimento1 = vcomprimento / (coeficientedilataçaotermica * vtemperatura)
        icomprimento1_f = format(icomprimento1, 'f')
        return render_template("dilataçaotermica.html", dtermica="Comprimento inicial: " + str(icomprimento1_f)+" m")
    elif coeficientedilataçaotermica==0 and icomprimento!=0 and vcomprimento!=0 and vtemperatura!=0:
        coeficientedilataçaotermica1 = vcomprimento / (icomprimento * vtemperatura)
        coeficientedilataçaotermica1_f = format(coeficientedilataçaotermica1, 'f')
        return render_template("dilataçaotermica.html", dtermica="Coeficiente de dilatação termica: " + str(coeficientedilataçaotermica1_f) )
    elif vtemperatura==0 and icomprimento!=0 and coeficientedilataçaotermica!=0 and vcomprimento!=0:
        vtemperatura1 = vcomprimento / (icomprimento * coeficientedilataçaotermica)
        vtemperatura1_f = format(vtemperatura1, 'f')
        return render_template("dilataçaotermica.html", dtermica="Variação de temperatura: " + str(vtemperatura1_f) + " °C")
    else:
        return render_template("dilataçaotermica.html", dtermica="Erro: Preencha os campos corretamente.")
#bhaskara
@app.route("/calculo_bhaskara", methods=["POST"])
#obs: importante tomar cuidade para não repitir o nome da função
def calculo_bhaskara():
    a = Decimal(request.form.get("a"))
    b = Decimal(request.form.get("b"))
    c = Decimal(request.form.get("c"))
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
    massa = Decimal(request.form.get("massa"))
    acel = Decimal(request.form.get("acel"))
    forca = Decimal(request.form.get("força"))
    if forca==0 and massa!=0 and acel!=0:
        forca1 = massa * acel
        return render_template("2leinewton.html", newton2="Força: " + str(forca1) + "N")
    elif massa==0 and forca!=0 and acel!=0:
        massa1 = forca / acel
        return render_template("2leinewton.html", newton2="Massa: " + str(massa1) + "kg")
    elif acel==0 and massa!=0 and forca!=0:
        acel1 = forca / massa
        return render_template("2leinewton.html", newton2="Aceleração: " + str(acel1) + "m/s²")
    else:
        return render_template("2leinewton.html", newton2="Erro: Preencha os campos corretamente.")
#MRU
@app.route("/calculo_mru", methods=["POST"])
def calculo_mru():
    dpercorrida= Decimal(request.form.get("dpercorrida"))
    tempo= Decimal(request.form.get("tempo"))
    velocidade= Decimal(request.form.get("velocidade"))
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
#Area do triangulo
@app.route("/calculo_areatriangulo", methods=["POST"])
def cauculo_areatriangulo():
    base=Decimal(request.form.get("base"))
    altura=Decimal(request.form.get("altura"))
    if base!=0 and altura!=0:
        area1=(base*altura)/2
        return render_template("areatriangulo.html", areaT= "A área do triângulo é:" + str(area1))
    else:
        return render_template("areatriangulo.html", areaT= "Erro: Preencha os campos corretamente.")


