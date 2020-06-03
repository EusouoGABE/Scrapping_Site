from app import app, db
from flask import render_template,redirect,url_for, request
from app.models.forms import ExtrairForm
from app.models.tables import Noticia, Mega
from app.controllers.scrapping import scrap
from app.controllers.scrapping import linkVet, tituloVet, dataVet
from app.controllers.scrappingMegaCurioso import vetorLink,vetorTitulo,vetorCategoria, scrapMega

a = ""

@app.route("/", methods=["GET", "POST"])
def extrair():
    form = ExtrairForm()
    if request.method == 'POST':
        a = form.link.data
        if (a == 'Tecmundo'):
            a = 'https://www.tecmundo.com.br/novidades'
            linkVet.clear()
            tituloVet.clear()
            dataVet.clear()
            scrap(a)
            cont = 0
            while cont <= 19:
                r = ""
                r = Noticia.query.filter_by(link=linkVet[cont]).first()
                if (r is None):
                    r = Noticia(linkVet[cont], tituloVet[cont], dataVet[cont])
                    db.session.add(r)
                    db.session.commit()
                else:
                    r.titulo = tituloVet[cont]
                    r.data   = dataVet[cont]
                    db.session.add(r)
                    db.session.commit()
                cont = cont + 1
            r = Noticia.query.all()
            arquivo = open('app/static/arquivos_txt/arqTec.txt', 'w')
            tam = len(r);
            for i in range(tam):
                arquivo.write(str(r[i]))
                arquivo.write("\n")
            arquivo.close()
            return render_template('tecmundo.html', linkVet=linkVet, tituloVet=tituloVet, dataVet=dataVet)
        else:
            if (a == 'MegaCurioso'):
                a = 'https://www.megacurioso.com.br/novidades/'
                vetorLink.clear()
                vetorTitulo.clear()
                vetorCategoria.clear()
                scrapMega(a)
                cont = 0                    
                while cont <= 19:
                    r = ""
                    r = Mega.query.filter_by(link=vetorLink[cont]).first()
                    if (r is None):
                        r = Mega(vetorLink[cont], vetorTitulo[cont], vetorCategoria[cont])
                        db.session.add(r)
                        db.session.commit()
                    else:
                        r.titulo = vetorTitulo[cont]
                        r.categoria = vetorCategoria[cont]
                        db.session.add(r)
                        db.session.commit()
                    cont = cont + 1
                r = Mega.query.all()
                arquivo = open('app/static/arquivos_txt/arqMega.txt', 'w')
                tam = len(r);
                for i in range(tam):
                    arquivo.write(str(r[i]))
                    arquivo.write("\n")
                arquivo.close()
                return render_template('megacurioso.html', vetorLink=vetorLink, vetorTitulo=vetorTitulo, vetorCategoria=vetorCategoria)
    return render_template('extrair.html',
                       form=form)



@app.route('/tecmundo', methods=['GET','POST'])
def tecmundo():
    return render_template('tecmundo.html', linkVet=linkVet, tituloVet=tituloVet, dataVet=dataVet)

@app.route('/megacurioso', methods=['GET','POST'])
def megacurioso():
    return render_template('megacurioso.html', vetorLink=vetorLink, vetorTitulo=vetorTitulo, vetorCategoria=vetorCategoria)






