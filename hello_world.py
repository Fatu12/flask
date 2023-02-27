from flask import Flask
# Create a new instance of the Flask class called "app"
app = Flask(__name__)

# The "@" decorator associates this route with the function immediately following


@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


# import statements, maybe some other routes
'''  it a variable name we assign to a request.the job of this root is to communicate
to the server what kind of information the client needs
every route has two parts
1. HTTP method (GET,POST,PUT,PATCH,DELETE)
2. URL'''


@app.route('/dojo')
def dojo():
    return "Dojo!"


@app.route('/hi/<name>')
def hi(name):
    print(name)
    return 'Hi, ' + name


@app.route('/say/<first_name>')
def say(first_name):
    # print(first_name)
    return "say, " + first_name


@app.route('/repeat/<int:num>/<string:text>')
def repeat(num, text):
    # from solution, make the output in line
    output = ''
    for i in range(0, num):
        output += f"<h3>{text}</h3>"
    return output


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
