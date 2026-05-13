from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Relatório Produção</title>

<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

<script>
function copiarRelatorio() {
    let texto = document.getElementById("textoRelatorio").innerText;
    navigator.clipboard.writeText(texto);
    alert("Relatório copiado!");
}
</script>

</head>

<body>

<div class="container">

<h1>📋 Gerador de Relatório</h1>

<div class="card">

<form method="POST">

<label>Área</label>
<input type="text" name="area" required>

<label>Responsável</label>
<input type="text" name="responsavel" required>

<label>Data</label>
<input type="date" name="data" required>

<label>Turno</label>
<select name="turno" required>
    <option disabled selected>Selecione</option>
    <option>1º Turno</option>
    <option>2º Turno</option>
    <option>3º Turno</option>
</select>

<label>Modelo</label>
<select name="modelo" required>
    <option disabled selected>Selecione</option>
    <option>Scania</option>
    <option>Mercedes</option>
    <option>DAF</option>
    <option>Volvo</option>
</select>

<label>Bloco</label>
<input type="text" name="bloco">

<label>Total de peças</label>
<input type="number" name="pecas" required>

<label>Solda</label>
<input type="number" name="solda" required>

<label>Refugo</label>
<input type="number" name="refugo" required>

<label>Recuperação</label>
<input type="number" name="recuperacao" required>

<label>Ultrassom</label>
<input type="number" name="ultrassom" required>

<label>Paradas</label>
<textarea name="paradas" rows="3"></textarea>

<label>Observações</label>
<textarea name="observacoes" rows="4"></textarea>

<button type="submit">Gerar Relatório</button>

</form>

</div>

{% if relatorio %}
<div class="relatorio" id="textoRelatorio">
{{ relatorio }}
</div>

<button class="copy" onclick="copiarRelatorio()">
Copiar Relatório
</button>
{% endif %}

</div>

</body>
</html>
"""

def plural(valor):
    try:
        return "peça" if int(valor) == 1 else "peças"
    except:
        return "peças"

@app.route("/", methods=["GET", "POST"])
def home():

    relatorio = ""

    if request.method == "POST":

        area = request.form["area"]
        responsavel = request.form["responsavel"]

        data_original = request.form["data"]
        data_formatada = datetime.strptime(data_original, "%Y-%m-%d").strftime("%d/%m/%Y")

        turno = request.form["turno"]
        modelo = request.form["modelo"]
        bloco = request.form["bloco"]

        pecas = request.form["pecas"]
        solda = request.form["solda"]
        refugo = request.form["refugo"]
        recuperacao = request.form["recuperacao"]
        ultrassom = request.form["ultrassom"]

        paradas = request.form["paradas"]
        observacoes = request.form["observacoes"]

        relatorio = f"""
📋 RELATÓRIO DE PRODUÇÃO

Área: {area}

Responsável: {responsavel}

📅 {data_formatada} — {turno}

Bloco {modelo} — {bloco}

• Total de peças: {pecas} {plural(pecas)}
• Solda: {solda} {plural(solda)}
• Refugo: {refugo} {plural(refugo)}
• Recuperação: {recuperacao} {plural(recuperacao)}
• Ultrassom: {ultrassom} {plural(ultrassom)}

Paradas:
{paradas}

Observações:
{observacoes}
"""

    return render_template_string(HTML, relatorio=relatorio)

if __name__ == "__main__":
    app.run(debug=True)
    app.run(debug=True)
