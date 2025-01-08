from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# 数据库配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "database.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化数据库
db = SQLAlchemy(app)

# 定义 Todo 模型
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'task': self.task,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

# 创建数据库表
with app.app_context():
    db.create_all()

# 路由：主页
@app.route('/')
def index():
    return render_template('index.html')

# API：获取所有待办事项
@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return jsonify([todo.to_dict() for todo in todos])

# API：添加新的待办事项
@app.route('/api/todos', methods=['POST'])
def add_todo():
    task = request.json.get('task')
    if not task:
        return jsonify({'error': '任务内容不能为空'}), 400
    
    todo = Todo(task=task)
    db.session.add(todo)
    db.session.commit()
    
    return jsonify(todo.to_dict())

# API：更新待办事项状态
@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    status = request.json.get('status')
    if status not in ['pending', 'completed']:
        return jsonify({'error': '无效的状态'}), 400
    
    todo = Todo.query.get_or_404(todo_id)
    todo.status = status
    db.session.commit()
    
    return jsonify({'message': '更新成功'})

# API：删除待办事项
@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    
    return jsonify({'message': '删除成功'})

# 添加管理界面路由
@app.route('/admin')
def admin():
    return render_template('admin.html')

# API端点获取实时数据
@app.route('/api/admin/todos')
def get_all_todos():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return jsonify([{
        'id': todo.id,
        'task': todo.task,
        'status': todo.status,
        'created_at': todo.created_at.strftime('%Y-%m-%d %H:%M:%S')
    } for todo in todos])

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': '404 - Not Found'}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': '500 - Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True) 