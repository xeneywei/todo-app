from flask import Flask, render_template, jsonify
from app import app, db, Todo
from datetime import datetime

# 添加新路由用于数据库管理界面
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