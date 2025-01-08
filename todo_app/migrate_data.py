import sqlite3
from app import db, Todo
from datetime import datetime

def migrate_old_data():
    try:
        # 连接旧数据库
        old_conn = sqlite3.connect('database.db.old')
        old_cursor = old_conn.cursor()
        
        # 首先检查表是否存在
        old_cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='todos'")
        if not old_cursor.fetchone():
            print("旧数据库中没有找到 todos 表")
            print("正在检查可用的表...")
            old_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = old_cursor.fetchall()
            if tables:
                print("找到的表:", [table[0] for table in tables])
            else:
                print("数据库中没有任何表")
            return

        # 获取表结构
        old_cursor.execute('PRAGMA table_info(todos)')
        columns = old_cursor.fetchall()
        print("表结构:", columns)
        
        # 获取旧数据
        old_cursor.execute('SELECT * FROM todos')
        old_todos = old_cursor.fetchall()
        print(f"找到 {len(old_todos)} 条记录")
        
        # 打印第一条记录作为示例
        if old_todos:
            print("第一条记录示例:", old_todos[0])
        
        # 迁移到新数据库
        for old_todo in old_todos:
            todo = Todo(
                task=old_todo[1],  # 假设第二列是 task
                status=old_todo[2] if len(old_todo) > 2 else 'pending',  # 假设第三列是 status
                created_at=datetime.now()  # 使用当前时间
            )
            db.session.add(todo)
        
        db.session.commit()
        old_conn.close()
        print("数据迁移成功！")
        
    except Exception as e:
        print(f"迁移失败: {str(e)}")
        import traceback
        print(traceback.format_exc())

if __name__ == '__main__':
    # 确保在应用上下文中执行
    from app import app
    with app.app_context():
        migrate_old_data() 