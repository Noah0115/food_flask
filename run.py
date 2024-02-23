from app import create_app, socketio
# 导入Socket事件处理器
import app.controller.socket_controller

if __name__ == '__main__':
    app = create_app()
    # app.run(host='0.0.0.0', port=5000, debug=True)
    socketio.run(app=app,host='0.0.0.0', port=5000, debug=True,allow_unsafe_werkzeug=True)
