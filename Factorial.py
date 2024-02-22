from flask import Flask, request

app = Flask(__name__)

@app.route("/factorial/<int:n>",methods=["GET"])
def factorial(n):
  r = calculate(n)
  return {"result":r},200 # OK

def calculate(n):
  if n <= 0:
    return 1
  else:
    return n * calculate(n-1)

if __name__ == "__main__":
  app.run(host="localhost",port=3000)
