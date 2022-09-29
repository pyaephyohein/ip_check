from flask import Flask, render_template, request, jsonify
import check_ping
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    ping_ip = request.form['ping_ip']
    ping_ip, message = check_ping.ping(ping_ip)
    message = message
    return ping_ip+" "+ message


@app.route('/ping/<ping_ip>')
def ping_route(ping_ip):
    ping_ip, message = check_ping.ping(ping_ip)
    data = {
            "host" : ping_ip,
            "message": message,
        }
    return jsonify(data)

@app.route('/get_my_ip')
def get_my_ip():
    return render_template('public_ip.html')   

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8081")