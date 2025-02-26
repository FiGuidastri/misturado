from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'segredo'  # Necessário para usar sessão

# Banco de palavras
palavras = {
    "frutas": ["abacaxi", "banana", "laranja", "manga"],
    "animais": ["leão", "elefante", "tigre", "gato"],
    "objetos": ["cadeira", "mesa", "computador", "janela"]
}

@app.route('/')
def home():
    # Escolher uma categoria aleatória
    categoria = random.choice(list(palavras.keys()))
    palavra_original = random.choice(palavras[categoria])
    palavra_embaralhada = ''.join(random.sample(palavra_original, len(palavra_original)))
    
    # Salvar as variáveis em sessão para usar na verificação
    session['categoria'] = categoria
    session['palavra_original'] = palavra_original
    
    return render_template('index.html', palavra_embaralhada=palavra_embaralhada)

@app.route('/verificar', methods=['POST'])
def verificar():
    resposta_usuario = request.form['resposta']
    
    # Recuperar a palavra original da sessão
    palavra_original = session.get('palavra_original', '')
    
    if resposta_usuario.lower() == palavra_original.lower():
        return jsonify({'resultado': 'Correto!', 'nova_palavra': palavra_original})
    else:
        return jsonify({'resultado': 'Errado, tente novamente!', 'nova_palavra': palavra_original})

if __name__ == '__main__':
    app.run(debug=True)
