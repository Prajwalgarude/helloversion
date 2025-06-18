from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page ('/')
@app.route('/')
def hello_version_v1():
    """
    This function handles requests to the root URL and returns
    the string "Hello version v1".
    """
    return 'Hello version v1'

# This block ensures the Flask development server runs only when the script
# is executed directly (not when imported as a module).
if __name__ == '__main__':
    # Run the Flask application.
    # host="0.0.0.0" makes the server accessible from any IP,
    # which is useful in containerized environments.
    # debug=True enables debug mode, providing a debugger and auto-reloading
    # on code changes.
    app.run(host="0.0.0.0", debug=True)
