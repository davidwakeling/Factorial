from flask import Flask, request

app = Flask(__name__)

@app.route("/factorial",methods=["POST"])
def endpoint():
  js = request.get_json()
  argument = js.get("argument")
  if argument != None:
    result = calculate(argument)
    return {"result":result},200 # OK
  else:
    return "",400 # Bad Request

def calculate(n):
  result = 1
  while n > 0:
    result = result * n
    n = n - 1
  return n

if __name__ == "__main__":
  app.run(host="localhost",port=3000)
