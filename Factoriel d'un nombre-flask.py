from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Factorial Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }
        
        .container {
            width: 300px;
            margin: 50px auto;
            background-color: #fff;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        
        .input-field {
            width: 95%;
            height: 40px;
            margin-bottom: 20px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        
        .button {
            width: 100%;
            height: 40px;
            background-color: #4CAF50;
            color: #fff;
            padding: 10px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        
        .button:hover {
            background-color: #3e8e41;
        }
        
        .result {
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Factorial Calculator</h2>
        <form action="/factorial" method="get">
            <input type="number" name="num" class="input-field" placeholder="Enter a number" required>
            <button class="button" type="submit">Calculate</button>
        </form>
        <p class="result">{% if result is not none %}Result: {{ result }}{% endif %}</p>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index(): 
    return render_template_string(html_template, result=None)

@app.route('/factorial', methods=['GET'])
def factorial():
    try:
        num = request.args.get('num', type=int)

        if num is None:
            return render_template_string(html_template, result="Veuillez entrer un nombre.")

        if num < 0:
            return render_template_string(html_template, result="Erreur : Le nombre doit être non négatif.")

        # Calcul du factoriel
        result = 1
        for i in range(2, num + 1):
            result *= i

        return render_template_string(html_template, result=result)

    except Exception as e:
        return render_template_string(html_template, result="Erreur: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)

