from flask import Flask, render_template, request, jsonify, session
from datetime import datetime
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    # تحقق إذا كان المستخدم جديدًا بناءً على الـ IP
    user_ip = request.remote_addr
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())  # إنشاء ID فريد للمستخدم الجديد
        session['joined_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        session['ip'] = user_ip
        return render_template('chat.html', user_id=session['user_id'], new_user=True, ip=user_ip)
    return render_template('chat.html', user_id=session['user_id'], new_user=False, ip=user_ip)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    return jsonify({'message': message, 'user_id': session['user_id'], 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

if __name__ == '__main__':
    app.run(debug=True)