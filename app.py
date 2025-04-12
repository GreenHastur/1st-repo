import os
from flask import Flask, request, abort

app = Flask(__name__)

# Konfiguracja (np. z zmiennych środowiskowych)
DEBUG_MODE = os.environ.get('DEBUG', 'False').lower() == 'true'
SECRET_KEY = os.environ.get('SECRET_KEY', 'domyslny_sekretny_klucz') # Zmień na losowy i bezpieczny klucz w produkcji!
app.secret_key = SECRET_KEY

@app.route('/')
def hello_world():
    return 'Witaj ze świata Flask!'

@app.route('/env')
def show_environment_variable():
    variable_name = request.args.get('name')
    if variable_name:
        value = os.environ.get(variable_name)
        if value is not None:
            return f"Wartość zmiennej środowiskowej '{variable_name}': {value}"
        else:
            return f"Zmienna środowiskowa '{variable_name}' nie jest ustawiona.", 404
    else:
        return "Podaj nazwę zmiennej środowiskowej jako parametr 'name' w URL.", 400

@app.route('/error')
def trigger_error():
    """Celowo wywołuje błąd, aby zademonstrować obsługę błędów."""
    try:
        result = 1 / 0
        return str(result)
    except ZeroDivisionError:
        # Logowanie błędu (lepsze niż tylko zwracanie tekstu)
        app.logger.error("Próba dzielenia przez zero!")
        abort(500, "Wystąpił błąd serwera.")

@app.errorhandler(400)
def bad_request(error):
    return f"Błąd 400: Nieprawidłowe żądanie. {error}", 400

@app.errorhandler(404)
def not_found(error):
    return f"Błąd 404: Nie znaleziono. {error}", 404

@app.errorhandler(500)
def internal_server_error(error):
    return f"Błąd 500: Wewnętrzny błąd serwera. {error}", 500

if __name__ == '__main__':
    app.run(debug=DEBUG_MODE, host='0.0.0.0', port=8080)