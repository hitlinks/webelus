from flask import Flask, make_response
# initial velocity in m/s
initialVelocity = 0

# final velocity in m/s
finalVelocity = 9.8

# Time In Second
time = 1

acceleration = (finalVelocity - initialVelocity) / time
#  Acceleration information
print("Acceleration = ", acceleration)
#  Delete cookies using flask 
app = Flask(__name__)

@app.route('/delete_cookie')
def delete_cookie():
    response = make_response("Cookie deleted")
    response.delete_cookie('cookie_name')
    return response

if __name__ == '__main__':
    app.run(debug=True)
