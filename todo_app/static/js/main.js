let currentFilter = 'all';
let allTodos = [];

// 获取所有待办事项
async function fetchTodos() {
    try {
        const response = await fetch('/api/todos');
        allTodos = await response.json();
        updateStats();
        displayTodos();
    } catch (error) {
        console.error('获取待办事项失败:', error);
    }
}

// 更新统计数据
function updateStats() {
    const total = allTodos.length;
    const completed = allTodos.filter(todo => todo.status === 'completed').length;
    const pending = total - completed;

    document.getElementById('totalTasks').textContent = total;
    document.getElementById('completedTasks').textContent = completed;
    document.getElementById('pendingTasks').textContent = pending;
}

// 显示待办事项
function displayTodos(searchTerm = '') {
    const todoList = document.getElementById('todoList');
    todoList.innerHTML = '';
    
    let filteredTodos = allTodos;
    
    // 应用过滤器
    if (currentFilter !== 'all') {
        filteredTodos = allTodos.filter(todo => todo.status === currentFilter);
    }

    // 应用搜索
    if (searchTerm) {
        filteredTodos = filteredTodos.filter(todo => 
            todo.task.toLowerCase().includes(searchTerm.toLowerCase())
        );
    }
    
    filteredTodos.forEach(todo => {
        const todoItem = document.createElement('div');
        todoItem.className = `todo-item ${todo.status === 'completed' ? 'completed' : ''}`;
        
        todoItem.innerHTML = `
            <input type="checkbox" 
                   ${todo.status === 'completed' ? 'checked' : ''}
                   onchange="updateTodoStatus(${todo.id}, this.checked)">
            <span class="task-text">${todo.task}</span>
            <button class="delete-btn" onclick="deleteTodo(${todo.id})">删除</button>
        `;
        
        todoList.appendChild(todoItem);
    });
}

// 添加新的待办事项
async function addTodo() {
    const input = document.getElementById('newTodo');
    const task = input.value.trim();
    
    if (!task) {
        alert('请输入待办事项内容！');
        return;
    }
    
    try {
        const response = await fetch('/api/todos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ task })
        });
        
        if (response.ok) {
            input.value = '';
            await fetchTodos();
        }
    } catch (error) {
        console.error('添加待办事项失败:', error);
    }
}

// 更新待办事项状态
async function updateTodoStatus(id, completed) {
    try {
        await fetch(`/api/todos/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                status: completed ? 'completed' : 'pending'
            })
        });
        
        await fetchTodos();
    } catch (error) {
        console.error('更新待办事项状态失败:', error);
    }
}

// 删除待办事项
async function deleteTodo(id) {
    if (!confirm('确定要删除这个待办事项吗？')) {
        return;
    }
    
    try {
        await fetch(`/api/todos/${id}`, {
            method: 'DELETE'
        });
        
        await fetchTodos();
    } catch (error) {
        console.error('删除待办事项失败:', error);
    }
}

// 过滤待办事项
function filterTodos(filter) {
    currentFilter = filter;
    
    // 更新过滤按钮状态
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    document.getElementById(`${filter}Filter`).classList.add('active');
    
    displayTodos();
}

// 搜索待办事项
function searchTodos() {
    const searchTerm = document.getElementById('searchInput').value;
    displayTodos(searchTerm);
}

// 支持回车添加待办事项
document.getElementById('newTodo').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        addTodo();
    }
});

// 页面加载时获取待办事项
document.addEventListener('DOMContentLoaded', fetchTodos); 